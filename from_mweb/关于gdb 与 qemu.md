# 关于gdb 与 qemu

##qemu

`$(V)$(QEMU) -S -s -parallel stdio -hda $< -serial null & ` 

* $<指定了使用第一个参数，就是ucore.img
* -S 开始后停住， -s shorthand for -gdb tcp::1234
* -parallel studio或 -monitor studio 应该是指定了"studio" 这种界面窗口

##gdb
gdb 中的文件不用再使用 file XXX




