# linux pipe

很多函数调用都是传引用， 直接对参数指针指向的内容进行操作，返回值只是一个错误代码

## SYSCALL\_DEFINE2

```text
    struct file *files[2];
    int fd[2];
```

* error = **\_\_do\_pipe\_flags**\(fd, **files**, flags\);
* fd\_install\(fd\[0\], files\[0\]\);
* fd\_install\(fd\[1\], files\[1\]\);

## \_\_do\_pipe\_flags\(int \*fd, struct file \*\*files, int flags\)

* error = **create\_pipe\_files**\(files, flags\);
* error = get\_unused\_fd\_flags\(flags\);

## int create\_pipe\_files\(struct file \*\*res, int flags\)

`struct path path;`

* struct inode \*inode =**get\_pipe\_inode**\(\);
* path.dentry = d\_alloc\_pseudo\(pipe\_mnt-&gt;mnt\_sb, &name\);
* d\_instantiate\(path.dentry, inode\);
* f = alloc\_file\(&path, FMODE\_WRITE, &pipefifo\_fops\);
* f-&gt;private\_data = inode-&gt;i\_pipe;

### static struct inode \* get\_pipe\_inode\(void\)

* struct inode \*inode = **new\_inode\_pseudo**\(pipe\_mnt-&gt;mnt\_sb\);
* struct pipe\_inode\_info \*pipe;
* pipe = **alloc\_pipe\_info**\(\);
* inode-&gt;i\_pipe = pipe;
* inode-&gt;i\_fop = &pipefifo\_fops;

## struct pipe\_inode\_info \*alloc\_pipe\_info\(void\)

* pipe = kzalloc\(sizeof\(struct pipe\_inode\_info\), GFP\_KERNEL\);
* pipe-&gt;bufs = kzalloc\(sizeof\(struct pipe\_buffer\) \* PIPE\_DEF\_BUFFERS, GFP\_KERNEL\);

