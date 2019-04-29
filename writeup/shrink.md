# shrink

### Basic function

Basically gives a menu offering functions like create, edit, delete "boot".

create use fgets, no overflow there, while edit is improperly using read, one null byte is able to overflow.

* Two global variables, 

  * boot\_index records how many boots exist  
  * boots are a array storing pointers to `boot` struct.

```c
struct boot{
    char* buffer;
    unsigned int length;
}
```

both struct boot and buffer stores in heap, every entry is 20 bytes which contains 0x10 bytes data and 0x10 bytes metadata.

When length is the length user gave when creating boot. `edit` cannot change length, and use length as parameter for `fets` and `read`

### Background of off-by-one

When `read(0, buf, 20)` , it reads 20 bytes data from standard input, then adds a '\0' to the end of data. So it overflow one null byte than expected. 

There's a lot of amazing ideas of how to exploit this null byte. This exploit only use a common one.

A and C should be 0x108 bytes here. 

![](../.gitbook/assets/image%20%284%29.png)

After B is freed, the chunk normally goes to unsorted bin\(if no tcache\), and the chunk itself has data like

```text
| A's last 8 bytes | 0x211 |
| 0x7fd1a3e3bb37| 0x7fd1a3e3bb78|
| BBBBBBBB....|
.....
```

the first 8 bytes is A's data. the second 8 bytes is B's chunks size plus 3 **bits** flag\(0 0 1\), only prev\_in\_use flag. 

* why ask for 0x208 bytes B? not 0x200 nor 0x210?

        because allocator will give 0x210 bytes chunk, first 0x10 bytes are unusable metadata, so 0x200 bytes usable data in chunk B, and 0x8 bytes in chunk C's prev\_size field.

        If 0x200 bytes, it still gives 0x210 bytes chunk for aligning, but cannot use prev\_size of C. C's prev\_size will be 0 if not used.

        if 0x210 bytes, it allocates 0x220 bytes data, buffer will not use prev\_size of C, either. 

When freeing B, C's `prev_size` will be updated to 0x210.

After A's data overflow B's metadata, chunk B's `size` filed will be overwritten to `0x200` , 

when allocating B1, allocator needs to update metadata `prev_size` in C. allocator navigates among chunks by shifting pointers **only** by using information of`prev_size` and `size` .  

1. Allocator gets the pointer to chunk B\( by examine unsorted bin\)
2. size = pointer\_B + 0x8
3. pointer\_C = pointer\_B + size
4. \*\(pointer\_C+8\) -= sizeof\(B1\)

> Before step 4, glibc after 2.23\(roughly\) checks whether \*\(pointer\_C+8\) == size, or it throws "size vs prev\_size" error. And later glibc have one additional check if \(B-&gt;fd-&gt;bk == B and B-&gt; bk -&gt; fd ==B\) or throws "double linked\_list" error.

The quote explains why I need to have "0x200" in chunk B when first time create it. Pay attention that the place I put "0x200" is not at the correct C's prev\_size field. Instead, it should be the "wrong" place that pointer\_B + 0x200

Above is a very rough description of what allocator does. Because there's wrong `size` in chunk B, the allocator turns out gets a wrong pointer\_C. So it wrote 0x200-sizeof\(B1\) to pointer\_B+0x200 instead of the correct place pointer\_B+0x210\(real chunk C's prev\_size\)

So, C's prev\_size remains unchanged. When C is being freed later, the allocator checks C's prev\_in\_use, find it's 0, so will try to merge C to `pointer_C-0x210`  . In this way, the B2 chunk becomes the "ghost" in this big chunk. 

Next, we could ask for a big chunk which uses this big vacuum. B2 is still in it.

### Exploit

In order to exploit off by one, we need three physically consecutive buffers. However buffers of  three consecutive boots will be split by their struct boot. 

To overcome that, before the real exploit, request three boots with 0x10 bytes data. Then free them all. That allows us to have six 0x20 bytes chunks in fastbin. All boot information chunks will use those chunks in fastbin, so their buffers get to be consecutive.  



```text
create(16, 'A'*20)
create(16, 'A'*20)
create(16, 'A'*20)


delete(0)
delete(0)
delete(0)


create(0x108, 'A')
print "first 110 created"
create(0x208, 'B'*0x1f0+p64(0x208)+p64(0x200)+p64(0x200))
print "second 210 created"
create(0x108, 'C')
print "third 110 created"
# A B C

delete(1)
# A C
edit(0, 'A'*0x108)
create(0x100, 'D'*0x100)
create(0x80, 'E'*0x80)
# 0A 2D 3E 1C
create(0x10,'F'*0x20)
create(0x10,'P'*0x20)
gg()
delete(2) #delete D
delete(1) #delete C

create(0x200, 'O'*0x1a0)
```

after line 23, the remainder chunk in unsorted bin has 0x60 bytes. I want to store a boot struct into that place, because chunk in this area will be overwritten by 'O'. In this way, I can overwrite the address of content to GOT\['free'\]

before I can malloc chunks in that area, there were still two 0x20 fastbin chunks at the beginning of arena. So I use 25, which actually malloc two chunks, one for boot struct and the one for content. 

> why line 22 and line 23 got 0x110 and 0x90 bytes.

boots table after line 26:

![](../.gitbook/assets/image%20%283%29.png)

they are: A, D\(B1\), E\(B2\), C, F, P

After D was deleted, P jumps to its place\(just index\) according to `edit_boot`

![](../.gitbook/assets/image%20%287%29.png)

0x603380 is the chunk P's boot struct



-------



* How to exploit the ghost chunk to get shell?

if allocate a `boot` struct in heap, we change the `buffer` pointer, so when editing this boot, we could write to **arbitrary** place. So overwrite a GOT is a good choice. 

We'd better write a GOT function that invoked with parameter could be easily controlled by us. free becomes a good choice. because when delete a boot. it will `free(buffer)` . 

We stores `/bin/sh` to that buffer, invoke free, got shell.

