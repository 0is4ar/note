# python flask 源码原理

## 上下文

flask 有两种上下文

* 请求上下文 **\_request\_ctx\_stack**
* 应用上下文 **\_app\_ctx\_stack**

这两个对象实际上都是通过LocalStack实现的（uwsgi实现库werkzeug提供）

### class Local

这是一个类似于python 中threading.lcoal的存在

> threading.local  
> 在一个文件中定义一个全局变量实例 haha = threading.local\(\)  
> 虽然是一个全局变量（照理上所有线程的数据是共享的进程空间中的数据）,但是每个线程访问的时候得到的东西都不一样，实现了隔离  
> 在a线程给haha绑定属性a,与b线程绑定的属性a是不互通的。

Local类主要实现的是将数据保存在**storage**属性中， **storage**是一个嵌套的字典 `self.__storage__[线程的标识符][变量的名称]` 通过这样来访问

### class LocalStack

这是基于Local类中的**storage**来实现的栈  
其实主要就是将 `self.__storage__[线程标识符]['stack']` 设置成一个list,实现了栈的pop push功能

```text
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()
```

`\_request_ctx_stack.top 在mytest中其实就是当前LocalStack的top = \_request_ctx_stack._local.__storage__[ident]['stack'][0]`

![](https://github.com/0is4car/note/tree/43d28368cc7aaa253766bf504b5065b0c04b2267/Users/Caking_s/Desktop/study/notebook/pic/flask_stack_top.png)

### class LocalProxy

> LocalProxy 是一个 Local 对象的代理，负责把所有对自己的操作转发给内部的 Local 对象.  
> LocalProxy 的构造函数介绍一个 callable 的参数，这个 callable 调用之后需要返回一个 Local 实例，后续所有的属性操作都会转发给 callable 返回的对象。

