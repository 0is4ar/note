# namespace

在lind_fs_call中看到了很多直接引用openfile却没有import 如何实现的？

lind_fs_call是在lind_test_server.py中调用的，

在调用之前，lind_test_server通过:`from repy_workaround import* 将里面的函数都import到自己的namespace中，

在repy_workarounds.py中，又有如下内容
```
from emulfile import emulated_open as openfile
 from emulfile import removefile
 from emulfile import listfiles

```

推断repy.py也是通过类似的手法实现的，将restriction中的”允许“的函数引用到自己的namespace，然后exec argv[2]

