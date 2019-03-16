# python flask 源码原理-1

\[TOC\]

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
request_ctx_stack = LocalStack()
app_ctx_stack = LocalStack()
```

`_request_ctx_stack.top 在mytest中其实就是当前LocalStack的top=_request_ctx_stack._local.__storage__[ident]['stack'][0]`

![](https://github.com/0is4car/note/tree/43d28368cc7aaa253766bf504b5065b0c04b2267/Users/Caking_s/Desktop/study/notebook/pic/flask_stack_top.png)

current\_app = LocalProxy\(\_find\_app\) request = LocalProxy\(partial\(\_lookup\_req\_object, 'request'\)\) session = LocalProxy\(partial\(\_lookup\_req\_object, 'session'\)\) g = LocalProxy\(partial\(\_lookup\_app\_object, 'g'\)\)

```python
def _lookup_req_object(name):
    return getattr(request_ctx_stack.top, name)
```

request\_ctx\_stack.top 是一个Request\_Context对象

> NOTE：前面双下划线的属性，会保存到 \_ClassName**variable 中。所以这里通过 “\_LocalProxy**local” 设置的值，后面可以通过 self.\_\_local 来获取。关于这个知识点，可以查看 stackoverflow 的这个问题。

#### 从request开始理顺一下

`request = LocalProxy(partial(_lookup_req_object, 'request'))`

> LocalProxy\(local,name=None\)

将request初始化为一个LocalProxy实例，其中\_local是callable `partial(_lookup_req_object, 'request'))`

> partial中直接写出一个参数的内容相当于传给函数所需的第一个参数 \_lookup\_req\_object\(name\)

那么`partial(_lookup_req_object, 'request'))`的意思就是将这个函数'包起来':

```python
def haha():
    def hehe():
        return _lookup_req_object('request')
    return hehe
```

其实是闭包起来的`getattr(request_ctx_stack.top, 'request')`

* request\_ctx\_stack.top是一个LocalStack的栈顶，一个RequestContext对象，这个对象的request属性是一个Request对象

request.\_get\_current\_object\(\)如果不是一个Local对象就会直接返回request.\_LocalProxy\_\_local\(\)。得到的是一个Request对象

## 全局？local?

**？一个LocalStack对象例如req**_**ctxstack是在进程空间中的，知识每次在使用的时候，通过代理，只会使用\_\_storage**_**中当前线程作为key的内容**

```python
>>> from werkzeug.local import LocalStack
>>> import threading

# 创建一个`LocalStack`对象
>>> local_stack = LocalStack()
# 查看local_stack中存储的信息
>>> local_stack._local.__storage__
{}

# 定义一个函数，这个函数可以向`LocalStack`中添加数据
>>> def worker(i):
        local_stack.push(i)

# 使用3个线程运行函数`worker`
>>> for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        t.start()

# 再次查看local_stack中存储的信息
>>> local_stack._local.__storage__
{<greenlet.greenlet at 0x4bee5a0>: {'stack': [2]},
 <greenlet.greenlet at 0x4bee638>: {'stack': [1]},
 <greenlet.greenlet at 0x4bee6d0>: {'stack': [0]}
}
```

LocalStack

```python
def push(self, obj):
    """Pushes a new item to the stack"""
    rv = getattr(self._local, 'stack', None)
    if rv is None:
        self._local.stack = rv = []
    rv.append(obj)
    return rv
```

再跟踪Local类的**getattr**魔术方法

```text
def __getattr__(self, name):
    try:
        return self.__storage__[self.__ident_func__()][name]
    except KeyError:
        raise AttributeError(name)
```

不难看出，虽然Local是全局的但是只会返回self.\_\_ident作为Key的stack

### class LocalProxy

> LocalProxy 是一个 Local 对象的代理，负责把所有对自己的操作转发给内部的 Local 对象.  
> LocalProxy 的构造函数介绍一个 callable 的参数，这个 callable 调用之后需要返回一个 Local 实例，后续所有的属性操作都会转发给 callable 返回的对象。

## 路由

* rule： url 规则字符串，可以是静态的 /path，也可以包含 /
* endpoint：要注册规则的 endpoint，默认是 view\_func 的名字
* view\_func：对应 url 的处理函数，也被称为视图函数

```text
>>>(Pdb) request.endpoint
'main.index'
```

### 添加

* 可以使用装饰器@app.route\('/'\)
* 可以使用语句`app.add_url_rule(rule, endpoint, f, **options)`

最后都是调用Flask.add\_url\_rule:

```python
rule = self.url_rule_class(rule,method)# Map里面都是Rule实例
self.url_map.add(rule)
self.view_functions[endpoint] = view_func
```

**感觉这个里面的rule并没有传入endpoint,不知如何联系起来**

* self.url\_map是一个werkzeug.routeing:Map类
* self.view\_function是一个werkzeug.routeing:Rule类,就是将endpoint与view\_func联系起来

关于Map的使用

```python
>>> m = Map([
...     Rule('/', endpoint='index'),
...     Rule('/downloads/', endpoint='downloads/index'),
...     Rule('/downloads/<int:id>', endpoint='downloads/show')
... ])
>>> urls = m.bind("example.com", "/")# 把路由表绑定到特定的环境（m.bind）
>>> urls.match("/", "GET")
('index', {})
>>> urls.match("/downloads/42")
('downloads/show', {'id': 42})
```

### 路由实现

```python
req = _request_ctx_stack.top.request
rule = req.url_rule
return self.view_functions[rule.endpoint](**req.view_args)
```

request.environ里面有请求的rule了，然后create\_url\_adapter\(self.request\)根据这个rule绑定map，并返回一个携带此次访问rule信息的实例，所以直接使用url\_rule=url\_adapter.match\(\)不用什么参数

* add\_url\_rule肯定会传入function的name,在没有传入endpoint的情况下，在加入map的时候，使用方法获取function的name来作为endpoint

```python
class RequestContext(object):
    def __init__(self, app, environ, request=None):
        self.app = app
        self.request = request
        self.url_adapter =  app.create_url_adapter(self.request)# 可以先不看这句
        self.match_request()

    def match_request(self):
        """Can be overridden by a subclass to hook into the matching
        of the request.
        """
        try: #通过adapter的match得到url_rule，从而在dispatch_request中通过url_rule.endpoint得到endpoint在view_function这个字典中查询得到function返回
            url_rule, self.request.view_args = \
                self.url_adapter.match(return_rule=True)
            self.request.url_rule = url_rule
        except HTTPException as e:
            self.request.routing_exception = e


class Flask(_PackageBoundObject):
    def create_url_adapter(self, request):
        """Creates a URL adapter for the given request.  The URL adapter
        is created at a point where the request context is not yet set up
        so the request is passed explicitly.
        """
        if request is not None:
            return self.url_map.bind_to_environ(request.environ,
                server_name=self.config['SERVER_NAME'])
```

### 简单总结

#### 添加路由

1.

```python
@app.route('/')
def index():
    pass
```

2.app.add\_url\_rule\('/',view\_func=index\)

```python
 rule = self.url_rule_class(rule, methods=methods, **options)
 self.url_map.add(rule) 
 self.view_functions[endpoint] = view_func
 '''endpoint默认部分代码省略，反正就是将一个rule和一个endpoint对应起来，
 加入url_map这个werkeug.local:Map对象中
 '''
```

#### 寻找路由

在应用启动流程的Flask.dispatch\_request\(self\)中 1.dispatch\_request

```python
rule = req.url_rule
return self.view_functions[rule.endpoint](**req.view_args)
```

2.

```python
class RequestContext(object):
    def __init__(self, app, environ, request=None):
        self.url_adapter = app.create_url_adapter(self.request)
        self.match_request()

    def match_request(self):
            url_rule, self.request.view_args = \
self.url_adapter.match(return_rule=True)
            self.request.url_rule = url_rule

class Flask(_PackageBoundObject):
    def create_url_adapter(self, request):
        if request is not None:
            return self.url_map.bind_to_environ(request.environ,
                server_name=self.config['SERVER_NAME'])
```

* MapAdapter.match其实就是通过遍历Map中的Rule的path,来找到path与传入参数（此处是adapter从request中获得的path\_info\)相符的Rule对象，从而返回
* 其实就是得到url\_rule\(有属性endpoint从而联系起来）
* 使用一个带有request.environ信息的adapter的match方法生成url\_rule
* adapter 是url\_map.bind\_to\_environ 其实最后返回的是一个MapAdaptor类实例，这个实例有self.path\_info属性，在调用match时没有传入path就会默认使用这个

