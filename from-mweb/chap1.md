# Chap1

* kernel mode and user mode is hardware supported by processor

## Start

bootloader 将 kernel 加载在0x100000的地方，然后kernel从entry开始运行，做两个映射：

* 0:0x400000 -&gt; 0:0x400000
* KERNBASE:KERNBASE+400000 -&gt; 0:0x400000 \(entry运行完之后启用\)，这样正好kernel经常寻找东西的地方0x8010000正好在0x100000\(bootloader将kernel加载的地方\)

processor 在过程中一直在Low address执行代码，当page 一开启，Processor寻址就会变成虚拟地址，但由于“惯性”他还是会按照一开始的物理地址（low address\)寻址，可是虚拟地址中的low address啥都没有，就崩了。但是没有崩，是因为一开始entry0 设置了0:0x400000 -&gt; 0:0x400000

当所有变量都迁移到高地址之后，jump到高地址执行

