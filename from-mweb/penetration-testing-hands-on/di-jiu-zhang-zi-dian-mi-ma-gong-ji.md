# 第九章 字典密码攻击

## cewl

`cewl -w bulbwords.txt -d 1 -m 5 www.bulbsecurity.com`

cewl这个工具，在目标网站上爬取各种单词，-d depth, -m min\_word\_length

## crunch

`crunch 7 8 AB` 生成最短7最长8所有由A、B组成的字符串

## Hydra

`Hydra -L userlist.txt -P passwordfile.txt 192.168.20.10 pop3`

## Offline Password Attacks

### hashdump

metapreter的hashdump应该是dump出来直接的hash值

### SAM

原始的SAM文件不能得到，但是在C:\Windows\repair文件夹有一份SAM文件的备份

但SAM文件中保存的不是直接的Hash码，需要先解密一下才是哈希吗，可能是Salt之类的，这个salt同样保存在C:\Windows\repair

提取**system**文件中的**bootkey**需要用bkhive工具: `bkhive system key.txt`即将提取出来的保存到key.txt

然后再用这个Bootkey去提取SAM中的hash，使用**samdump**工具

最后得到的结果实际上和用Hashdump得到的一样

## 物理攻击

在一台windows7的电脑上，通过U盘启动Linux，然后挂载windows的硬盘，然后得到他的SAM和system文件从而得到用户名哈希

## LM 和 NTLM

之前hashdump看到的就是LM加密和NTLM加密，如果是windows7的话并不会有LM加密，但是为了保证兼容性，LM字段的哈希值代表空

### LM

LM加密会把密码截断到14位，全部大写，不足14位会填充到14位，并且会把这14位分成7 7

`john xphashes.txt`就将LM破解了

## Linux

Linux的hash密码只能用密码本破解： `john linuxpasswords.txt --wordlist=passwordfile.txt`

