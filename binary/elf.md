# ELF

[http://learn.tsinghua.edu.cn/kejian/data/77130/138627/html-chunk/ch18s05.html](http://learn.tsinghua.edu.cn/kejian/data/77130/138627/html-chunk/ch18s05.html)

```text
.section .data
.global data_item
data_item:
.long 3,67,28
.section .text
.global _start
_start:
    mov $1,%eax
    mov $4,%ebx
    int $0x80
```

`readelf -h ../asm/hello`

```text
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x4000b0                                       //程序的入口地址是0x4000b0
  Start of program headers:          64 (bytes into file)                    //segment表在文件64字节偏移处
  Start of section headers:          240 (bytes into file)                     
  Flags:                             0x0
  Size of this header:               64 (bytes)                                        
  Size of program headers:           56 (bytes)                                 //segment头项的长度是56字节（32系统是32字节)   
  Number of program headers:         2
  Size of section headers:           64 (bytes)
  Number of section headers:         6
  Section header string table index: 3
```

Entry point address: 0x4000b0 //程序的入口地址是

Start of program headers: 64 \(bytes into file\) //segment表在文件64字节偏移

Size of program headers: 56 //segment头项的长度是56字节（32系统是32字节\)

Section to Segment mapping: Segment Sections... 00 .text 01 .data

我们看到程序有两个segment ，分别叫做.text 和.data

* .text的Offset是0，FileSiz是0x0,MemSiz是0xbc, VirtAddr是0x400000,Flags是R E,表示加载起将把elf文件中从0字节开始直到oxbc处的内容加载到虚拟内存中的0x400000处，占用0xbc长度的内存。设置该内存的权限是RE\(可读，可执行），这一段的内容正好是elf头，segments table,和代码段。
* 再看看elfheader 的e\_entry 的地址 0x4000b0，这个地址正好是代码段的起始地址。 **前面header看出elf header+program header=110** **虽然.text的offset是0，但是e\_entry 0x4000b0正好跳过了这110**
* .data的Offset是0，FileSiz是0xbc,MemSiz是0x0c, VirtAddr是0x6000bc,Flags是R W,表示加载起将把elf文件中从bc字节开始直到oxbc + 0xc处的内容加载到虚拟内存中的0x6000bc处，占用0x0c长度的内存。设置该内存的权限是RE\(可读，可执行）
* 为什么数据段的其实地址是0x6000bc,而不是0x6000000呢，这是由Align决定的，Align决定内存和磁盘以1M为单位进行映射，在文件中.data 和.text处于一个页面中，在映射的时候，直接把整个页面都映射到了0x6000000处，所以把数据段的偏移设置成了0x60000bc,0x600000到0x6000bc的内容不使用。

