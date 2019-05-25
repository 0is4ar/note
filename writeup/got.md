# got



![](../.gitbook/assets/image%20%281%29.png)

```text
printf('welcomde')
printf('date is')
run_cmd('/bin/date')
fgets(rbp-0x20,0x18)   //local_20h
mov [[rbp-0x10]], [rbp-0x20]
mov [[rbp-0x8]], [rbp-0x18]
puts([rbp-0x20])
```

rbp--0x10 stores a pointer, put the pointer in rcx.

rbp-0x20 --&gt; \[rbp-0x10\]

rbp-0x18 --&gt; \[rbp-0x10\]+0x8

because rbp-0x20 will be used as parameter of puts later, and there's only one thing needs to be written that puts' address, so simply fill rbp-0x20 with "/bin//sh", 

this '/bin//sh' will be written to 0x601010\(we need /bin//sh next phase, but this code of this phase wants to write this to somewhere\), so rbp-0x18 could overwrite 0x601018

![](../.gitbook/assets/image%20%288%29.png)

since fgets doesn't use 00 to determine the end of string. So my input could contain 00.

because I input 24 bytes, and /bin/sh is the first eight bytes. fgets only add 00 on the end of \*\*all\*\* my input. So the parameter of system will be /bin/sh@\#\)... I need to manually add \x00.

At first I tried to replace puts in got with system's address in libc. But the address that libc being loaded into the binary is always changing. So I can't  things like 0x7ffff7e20380 in above image is always changing. If there's stackoverflow, maybe I could expose the address of libc's address at that time of executing by ROP. But the fact is I didn't have enough usable resource to expose it. But I found that the previous code in main invokes run\_cmd. And run\_cmd calls system. So I simply replace the puts' address with the `call system` in `run_cmd`



#### about randomization

OS's ASLR requires PIE of program\(-no-pie to disable\).

After disable PIE when compiling. even though the address of stack unchange, because the order of loading different share library is always changing, the base address of libc changes correspondingly. 

When use gdb, even the address of libc doesn't change. I guess this is because gdb restrict the order of libraries being loaded. This should take notice of.  

 

