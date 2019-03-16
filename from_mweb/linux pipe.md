# linux pipe

很多函数调用都是传引用， 直接对参数指针指向的内容进行操作，返回值只是一个错误代码

#### SYSCALL_DEFINE2

```
    struct file *files[2];
    int fd[2];
```
    
- error = **__do_pipe_flags**(fd, **files**, flags);
- fd_install(fd[0], files[0]);
- fd_install(fd[1], files[1]);

#### __do_pipe_flags(int \*fd, struct file **files, int flags)

- error = **create_pipe_files**(files, flags);
- error = get_unused_fd_flags(flags);

#### int create_pipe_files(struct file **res, int flags)

`struct path path;`

- struct inode \*inode =**get_pipe_inode**();
- path.dentry = d_alloc_pseudo(pipe_mnt->mnt_sb, &name);
- d_instantiate(path.dentry, inode);
- f = alloc_file(&path, FMODE_WRITE, &pipefifo_fops);
- f->private_data = inode->i_pipe;

##### static struct inode * get_pipe_inode(void)

- struct inode \*inode = **new_inode_pseudo**(pipe_mnt->mnt_sb);
- struct pipe_inode_info *pipe;
- pipe = **alloc_pipe_info**();
- inode->i_pipe = pipe;
- inode->i_fop = &pipefifo_fops;


#### struct pipe_inode_info *alloc_pipe_info(void)

- pipe = kzalloc(sizeof(struct pipe_inode_info), GFP_KERNEL);
- pipe->bufs = kzalloc(sizeof(struct pipe_buffer) * PIPE_DEF_BUFFERS, GFP_KERNEL);

