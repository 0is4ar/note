# ld

* 编译（.S\)---&gt;汇编---&gt;链接
* **可重定位**目标文件 ld = **可执行目标文件**

符号表是由汇编器构造，.symtab符号表不包含局部变量，汇编器的符号表包含

每个程序在被连接之前，所有.data和.text段的地址都填的0x0，连接之后才会变成实际的地址，但这个实际的地址也不是实际的地址，是每个程序对应分配的虚拟地址，如果想落实到物理地址就需要os的转化，这个不用纠结了，

为什么每个程序看地址的时候都是8几几？其实每个程序在内存中的分配都是有固定分配的，从哪到哪是堆栈从哪到哪是什么

是不是.data段存在哪里是根据段寄存器来的？

XXX应该不是，段寄存器应该是在更下层的地方，靠近物理内存了，但是.data段应该还是存在虚拟内存的位置。还有页机制，所以感觉两个是有点根本不太挨着的东西。

那么这个分段有什么意思呢，在运行程序的时候直接 mov 0x8235a9f8 %eax 假设那个地址是一个数据，并没有跟segment机制产生什么实际的关系

