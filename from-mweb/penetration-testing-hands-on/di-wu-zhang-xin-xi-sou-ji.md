# 第五章 信息搜集

`nc -vv 192.168.20.10 25`通过nc手动测试连接25端口

## nmap

`nmap -sS 192.168.20.10-12 -oA booknmap` 用SYN方式扫描10-12的主机，并将结果以所有格式记录到booknmap  
-sT 是full TCP connection -sV 是版本探测 -sU UDP 使用udp协议的端口用TCP探测不出来 -p 可以指定某个端口

默认情况下nmap只会扫描一个主机1000个最有可能的端口

