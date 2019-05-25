# heap (overflow)

> standard linux distrubution is now using ptmalloc2(glibc), which allocates heap by using malloc/free functions. 

when allocating, no physical memory is mapped to the virtual memory given to user, it will be mapped only when user gets to use it.

## basic

### malloc

`malloc(size_t n)`

> If n is zero, malloc returns a minumum-sized chunk. (The minimum size is 16 bytes on most 32bit systems, and 24 or 32 bytes on 64bit systems.) 

because `size_t` is actually unsigned for most of OS, that means it's a fairly large number when it's a negative number.


When first time invoking `malloc`, even though only 1000 bytes is requested, the OS will allocate 132KB, this is called **arena**. 

arena created by main thread is called **main arena**

### free

`free(void* p)`

- no operation when p is null.
- arbitrary effects if p has already been freed(double free).


## syscall behind 

`(s)brk`, `mmap`, `munmap` are three syscalls behind functions like `malloc` and `free`.

`int brk(void *end_data_segment);`
`void *sbrk(intptr_t increment);`


### (s)brk 

brk is a system call, sbrk is a function from glibc.

`start_brk` and `brk` are two pointers point to start and end of the heap.

`sbrk(0)` will give the current `brk` pointer. 


the `brk` syscall moves `brk` poitner to `end_data_segment`


### how syscalls are used

malloc may use brk or mmap.

the locations of memory allocated by brk and mmap are different. 



## arena 

arena is a big range of memory given to glibc by OS. It is allocated at the first time a thread request heap chunk.

A example is that, when allocate **main arena**(for main thread), brk is used, and when allocating **thread arena**, mmap is used. 

even though all chunks requested by a thread have been freed, the arena of that thread still exists, and is managed by glibc.

- application’s arena limit is based on number of cores present in the system.
    - 32bit system: 2*#core
    - 64bit system: 8*#core



## data structure


```C
struct malloc_chunk {

  INTERNAL_SIZE_T      prev_size;  /* Size of previous chunk (if free).  */
  INTERNAL_SIZE_T      size;       /* Size in bytes, including overhead. */

  struct malloc_chunk* fd;         /* double links -- used only if free. */
  struct malloc_chunk* bk;

  /* Only used for large blocks: pointer to next larger size.  */
  struct malloc_chunk* fd_nextsize; /* double links -- used only if free. */
  struct malloc_chunk* bk_nextsize;
};
```

>When I'm thinking this data structure, I imagine that the heap area all densed with all kinds of `malloc_chunk` with different sizes. There's no rule for **physical** neighbor chunks, and `prev_size` and `size` are used to describe physical neighbor. However, there're linked list for different `bins`, pointeres `fd` and `bk` are used to link malloc_chunks belong to the same bin but not physical neighbor.


- The first two elements are called **header**. the other four are called **user data**

- The last tree bits of size are flags. 
    - PREV_INUSE – Set when previous chunk is allocated
    - IS_MMAPPED – Set when chunk is mmap’d (for larger allocations)
    - NON_MAIN_ARENA – When	using a thread specific arena



---

https://azeria-labs.com/heap-exploitation-part-2-glibc-heap-free-bins/

```
Bin[0] = N/A
Bin[1] = unsorted bin
bin[2] to bin[64] = small bin
bin[65] to bin[127] = large bin
```

- If the chunk has the M bit set in the metadata, the allocation was allocated off-heap and should be munmaped.
- Otherwise, if the chunk before this one is free, the chunk is merged backwards to create a bigger free chunk.
- Similarly, if the chunk after this one is free, the chunk is merged forwards to create a bigger free chunk.
- If this potentially-larger chunk borders the “top” of the heap, the whole chunk is absorbed into the end of the heap, rather than stored in a “bin”.
- Otherwise, the chunk is marked as free and placed in an appropriate bin.k



micro size recently freed chunk goes to fast bin(less than 64 bytes)
small recently freed chunk goes to fast bin

* chunk in fastbin always has '1' in 'prev_in_use' of next chunk.



- If the size corresponds with a tcache bin and there is a tcache chunk available, return that immediately.
- If the request is enormous allocate a chunk off-heap via mmap.
- Otherwise we obtain the arena heap lock and then perform the following strategies, in order:
    - Try the fastbin/smallbin recycling strategy
        - If a corresponding fast bin exists, try and find a chunk from there (and also opportunistically prefill the tcache with entries from the fast bin).
        - Otherwise, if a corresponding small bin exists, allocate from there (opportunistically prefilling the tcache as we go).
    - Resolve all the deferred frees
        - Otherwise “truly free” the entries in the fast-bins and move their consolidated chunks to the unsorted bin.
        - Go through each entry in the unsorted bin. If it is suitable, stop. Otherwise, put the unsorted entry on its corresponding small/large bin as we go (possibly promoting small entries to the tcache as we go).
    - Default back to the basic recycling strategy
        - If the chunk size corresponds with a large bin, search the corresponding large bin now.
- Create a new chunk from scratch
    - Otherwise, there are no chunks available, so try and get a chunk from the top of the heap.
    - If the top of the heap is not big enough, extend it using sbrk.
    - If the top of the heap can’t be extended because we ran into something else in the address space, create a discontinuous extension using mmap and allocate from there
- If all else fails, return NULL.



#### free


- If the pointer is NULL, the C standard defines the behavior as “do nothing”.
- Otherwise, convert the pointer back to a chunk by subtracting the size of the chunk metadata.
- Perform a few sanity checks on the chunk, and abort if the sanity checks fail.
- If the chunk fits into a tcache bin, store it there.
- If the chunk has the M bit set, give it back to the operating system via munmap.
- Otherwise we obtain the arena heap lock and then:
    - If the chunk fits into a fastbin, put it on the corresponding fastbin, and we’re done.
    - If the chunk is > 64KB, consolidate the fastbins immediately and put the resulting merged chunks on the unsorted bin.
    - Merge the chunk backwards and forwards with neighboring freed chunks in the small, large, and unsorted bins.
    - If the resulting chunk lies at the top of the heap, merge it into the top of the heap rather than storing it in a bin.
    - Otherwise store it in the unsorted bin. (Malloc will later do the work to put entries from the unsorted bin into the small or large bins).
