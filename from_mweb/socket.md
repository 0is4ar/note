# socket

## netsocket.repy
调用lind_net_calls.py中的socket_syscall

###lind_net_calls.py

socket_syscall 调用 _socket_initializer,并返回Response类

```
        result = socket_syscall(domain, _type, protocol)
    return SuccessResponseBuilder("net_socket", result)
```
_socket_initializer只是将socket信息保存到全局的表里，并返回socket信息在表的索引newfd
##上面好像只是lind项目里面


- 在seattlelib/librepysocket.repy的openconn类
会调用openconnection

openconnection 在 repy/emulcomm.py定义

- oppenconnection 会 调用

```
sock = _timed_conn_initialize(identity, timeout)
OPEN_SOCKET_INFO[identity] = (threading.Lock(), sock)
emul_sock = EmulatedSocket(identity)
```

  并且返回emul_sock
  
  - _timed_conn_initialize
  
```  
sock = _get_tcp_socket(localip, localport)
```

- get_tcp_socket

```
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- EmulatedSocket会调用
      sock_lock, sock = OPEN_SOCKET_INFO[self.identity]
来获得sock,
OPEN_SOCKET_INFO是全局变量，一个dict

listenforconnect函数中

  identity = ("TCP", localip, localport, None, None)

      
sock = _get_tcp_socket(localip,localport)
才真正找到了socket

    OPEN_SOCKET_INFO[identity] = (threading.Lock(), sock)

才真正地进行了sock的定义



###_get_tcp_socket

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
而socket是import socket

## net_recv

net_recv.repy中的recv调用
  lind_net_syscall中的recv_syscall(fd,length,flag)，调用
    recvfrom_syscall(fd,length,flag)调用
    
``` sockobj = socketobjecttable[filedescriptortable[fd]['socketobjectid']]
    data = socketobj.recv(length)
```

最后发现socketobj的来源是通过connect_syscall等，调用open_connection, 然后插入进socketobjecttable


