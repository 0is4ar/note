# lottery schedule

usys.S中: 当调用SYSCALL\(settickets\)时 `$SYS_ ## name`就是拼接成 `$SYS_settickets`, 这就是在syscall.h中定义的syscall编号，23:

`#define SYS_settickets 23`

```text
#define SYSCALL(name) \
  .globl name; \
  name: \
    movl $SYS_ ## name, %eax; \
    int $T_SYSCALL; \
    ret
```

proc.c settickets sysproc.c sys\_settickets \(invoke settickets by defs.h\) argint接受参数 syscall.c 中对应syscall号与sysproc.c中的sys\_settickets（自己声明）

usys.S中定义SYSCALL\(settickets\)（找到系统调用号给eax，然后int）

