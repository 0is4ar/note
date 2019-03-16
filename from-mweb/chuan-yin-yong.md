# 传引用

```c
char*
strchr(const char *s, char c)
{
  for(; *s; s++)
    if(*s == c)
      return (char*)s;
  return 0;
}

strchr(p, '\n');
```

这里s是形参，所以说改变s的值并不会改变指针p的位置，但是改变\*s的值，p指向的地址的值就会改变了。

