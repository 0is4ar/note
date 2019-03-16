# namespace

在lind\_fs\_call中看到了很多直接引用openfile却没有import 如何实现的？

lind\_fs\_call是在lind\_test\_server.py中调用的，

在调用之前，lind\_test\_server通过:\`from repy\_workaround import\* 将里面的函数都import到自己的namespace中，

在repy\_workarounds.py中，又有如下内容

```text
from emulfile import emulated_open as openfile
 from emulfile import removefile
 from emulfile import listfiles
```

推断repy.py也是通过类似的手法实现的，将restriction中的”允许“的函数引用到自己的namespace，然后exec argv\[2\]

