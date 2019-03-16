# 结构

dispatcher 中的 lind\_net\_send在seattlelib/net\_send.repy中定义

* 调用  seattlelib/lind\_net\_lib.py 的 send\_syscall
* 调用  相同文件中 的 sendto\_syscall
* 调用 repy/emulcomm.py中的sendmessage
* 调用相同文件的get\_socket 
* 再下一步就是使用socket.socket了

