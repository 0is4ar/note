# file table

three tables are there

filedescriptortable file descriptor table

```text
"{0: {'position': 2, 'inode': 3, 'flags': 2, 'lock': <emulmisc.emulated_lock object at 0x7fa817df5e18>}}\n

{0: {'position': 2, 'inode': 3, 'flags': 2, 'lock': <emulmisc.emulated_lock object at 0x7fa817df5e18>}, 
1: {'position': 2, 'inode': 3, 'flags': 2, 'lock': <emulmisc.emulated_lock object at 0x7fa817df5e18>}}
```

这是通过utf输出的结果，utf输出的结果是一个tuple,第二个元素好像总是None,第一个是一个str，就算测试的单元有多次输出，会被utf合并成一个str，不同的输出以\n隔开

filesystemmetadatatable file system meta data

fileobjecttable

## open

在syscall\_open 中可以看到

fileobjecttable\[inode\] = openfile\(FILEDATAPREFIX+str\(inode\),True\)

fileobjecttable是一个字典，empty dictionary can be added by use dicname\[key\]=value，so every inode is a repy file object, and the name can be

linddata.inode\_number

### 随记

即使底层可以对参数进行检查并且报错，但是我们依旧在高层检查的目的是，将错误拦截在这一层，

### 流程

open\_syscall\(path, flags, mode\)

* 通过`_get_absolute_parent_path`解析path 中的 .. 什么的 --&gt; true path

然后分支 if true path not in fastinodelookuptable

* 如果file不存在：
  * 判断parent是不是一个文件夹，不是则报错
  * 是文件夹： newinode = filesystemmetadata\['nextinode'\] filesystemmetadata\['nextinode'\] += 1

    然后初始化newinode![](../../.gitbook/assets/15414486134550.jpg)

    然后再parent inode中添加该文件的inode `filesystemmetadata['inodetable'][parentinode]['filename_to_inode_dict'][filename] = newinode` filename应该是这个新文件的文件名，通过这样在file\_to\_inode\_dict中添加条目

其实在真是文件中的系统命名和文件句柄并没有与表关联起来，只是通过真是文件系统中的命名中含有的"inode号" 从而建立联系

* 如果存在file

将inode对应的源文件删了，然后新openfile

对表的影响：

* 如果不存在file的话： 更新filesystemmetadata,将parent在meta表中的信息，更新， 更新fastinodelookuptable, 将参数path转换成的true\_path 与 新的inode号 对应
* 如果存在file的话： 文件在filesystemmetadata或者fast表中都有信息了，直接在 fileobjecttable中，覆盖

最后在filedescriptortable和fileobjecttable中跟新新的inode信息

`filedescriptortable[thisfd] = {'position':position, 'inode':inode, 'lock':createlock(), 'flags':flags&O_RDWRFLAGS}`

`fileobjecttable[inode] = thisfo`

