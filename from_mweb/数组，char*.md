# 数组，char*

这两个在大多数时间相等
但是

```c
char a[]={'hahaha'};
char *b = 'hahaha';
```

此时sizeof(a)就是7
sizeof(b)是4 即地址的长度(0x12345678)4bytes
sizeof(*b)就是'h'的长度1

对于一个char *a
print("%s", a) print的是它指向位置直到'\0'的字符串
而不是以%s将它储存的地址打出来，有点tricky

