# gdb

- 先确定了端口为25000
然后make qemu-nox-gdb

- gdb进入gdb

- file _uniq2 载入uniq2的信息，其实不载入也能调试，但是_uniq2里面有固定的这个elf的segment会被载入到虚拟内存的哪些个地方，以及含有这个函数的C源码。这样gdb才能通过内存的位置来载入断点什么的

- target remote localhost:25000

- Continue，在Makefile中指定了make qemu-nox-gdb 在一开始是会冻住，等gdb来Continue的


|操作|结果|
|---|---|
|p a|print出a的值|
|layout split|可以同步显示C代码和Asm|
|x /16i $pc|打印出pc指向地址后面的16行,i代表instruction|
|x /16x $esp|打印出栈顶的后16个元素，x代表hex|
|x /16c $a|打印出指针变量a纸箱地址的后16位变量，c代表char|
|bt | backtrace: show stack functions and args|
|p /x a| 打印a的16进制
|p /d a||
|p /c a||


set follow-fork-mode child
gef config context
xinfo
xfiles


## pwn

context.terminal = ['tmux', 'splitw', '-h']

s=process('./a')
gdb.attach(s)
通过IDA找到需要breakpoint的点

然后b *0xdeadbeaf

先sendline,再c

还可以follow-exec mode-

