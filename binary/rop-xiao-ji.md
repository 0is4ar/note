# ROP小计

第一个参数是buffer的地址0xbffff51c 第二个参数是string的地址0xbffff7a0，\*\(0xbffff7a0\) = "AAAA"

0xbffff51c存放的是buffer指针，也是一个地址，指向0xbffff57c但感觉只是一个初始化的值， 因为当strcpy\(buffer,string\)的时候，覆盖的是0xbffff551c的内容

当执行完了strcpy之后，esp和ebp都并没有改变，或者说又变回来了

不同的是ebp的内容变成了0x42424242，原本应该是caller的ebp 当vunlerable\_function 返回的时候。

not\_called变成了 以为的 caller 而42424242变成了 not\_called的栈的ebp

leave等价于：

movl %ebp %esp popl %ebp

ret就等价于 pop $eip（丢弃掉刚才返回地址的值）

即jump到esp指向的值

当执行完了leave之后，esp的值变成了之前ebp的值+4，是因为mov之后又pop了

所以说当一个caller接受刚call完的函数时，栈是好的

当vulnerable\_function的汇编执行到ret的时候$ebp还是0x42424242

正常来说，调用一个函数返回后，栈是callee帮你还原了，你直接继续用还原后的栈执行下面的代码， ！！但是！！

由于ret 到了 not\_called函数的开头，每个函数的开头会有 push %ebp mov %esp,%ebp 的操作

而此时刚刚进入not\_called，esp的值是一个正常的值\(紧接着上一个函数栈的\)，所以先把ebp--0x42424242这个值push到栈顶，然后ebp变成esp，这样0x42424242这个异常的ebp实际上并没有被使用

