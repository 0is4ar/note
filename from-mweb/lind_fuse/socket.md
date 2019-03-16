# socket

## netsocket.repy

调用lind\_net\_calls.py中的socket\_syscall

### lind\_net\_calls.py

socket\_syscall 调用 \_socket\_initializer,并返回Response类

```text
        result = socket_syscall(domain, _type, protocol)
    return SuccessResponseBuilder("net_socket", result)
```

\_socket\_initializer只是将socket信息保存到全局的表里，并返回socket信息在表的索引newfd

## 上面好像只是lind项目里面

* 在seattlelib/librepysocket.repy的openconn类

  会调用openconnection

openconnection 在 repy/emulcomm.py定义

* oppenconnection 会 调用

```text
sock = _timed_conn_initialize(identity, timeout)
OPEN_SOCKET_INFO[identity] = (threading.Lock(), sock)
emul_sock = EmulatedSocket(identity)
```

并且返回emul\_sock

* \_timed\_conn\_initialize

```text
sock = _get_tcp_socket(localip, localport)
```

* get\_tcp\_socket

```text
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

* EmulatedSocket会调用

  ```text
  sock_lock, sock = OPEN_SOCKET_INFO[self.identity]
  ```

  来获得sock,

  OPEN\_SOCKET\_INFO是全局变量，一个dict

listenforconnect函数中

identity = \("TCP", localip, localport, None, None\)

sock = \_get\_tcp\_socket\(localip,localport\) 才真正找到了socket

```text
OPEN_SOCKET_INFO[identity] = (threading.Lock(), sock)
```

才真正地进行了sock的定义

### \_get\_tcp\_socket

s = socket.socket\(socket.AF\_INET, socket.SOCK\_STREAM\) 而socket是import socket

## net\_recv

net\_recv.repy中的recv调用 lind\_net\_syscall中的recv\_syscall\(fd,length,flag\)，调用 recvfrom\_syscall\(fd,length,flag\)调用

\`\`\` sockobj = socketobjecttable\[filedescriptortable\[fd\]\['socketobjectid'\]\] data = socketobj.recv\(length\)

\`\`\`

最后发现socketobj的来源是通过connect\_syscall等，调用open\_connection, 然后插入进socketobjecttable

