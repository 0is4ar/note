# HTTPS自己理解版

1. client发送请求的时候附带client_random，支持的**加密算法**和数据压缩算法

2. 服务器返回证书（附带公钥【*如果公钥带在外面会被篡改*】）什么的加上server_random。

3. 
    1. client通过server_random计算出premaster_key. 再通过premaster、client_random、server_random计算出master_key

    2. 在利用master_key,server_random和client_random计算出密钥块（包括两个方向分别的[session_key]）

    3. 通过之前的公钥加密之后，将premater_key发送给server，这时候server和3.1中client的信息相同，计算出相同的各种key



>"不管是客户端还是服务器，都需要随机数，这样生成的密钥才不会每次都一样。由于SSL协议中证书是静态的，因此十分有必要引入一种随机因素来保证协商出来的密钥的随机性。

>对于RSA密钥交换算法来说，pre-master-key本身就是一个随机数，再加上hello消息中的随机，三个随机数通过一个密钥导出器最终导出一个对称密钥。

>pre master的存在在于SSL协议不信任每个主机都能产生完全随机的随机数，如果随机数不随机，那么pre master secret就有可能被猜出来，那么仅适用pre master secret作为密钥就不合适了，因此必须引入新的随机因素，那么客户端和服务器加上pre master secret三个随机数一同生成的密钥就不容易被猜出了，一个伪随机可能完全不随机，可是是三个伪随机就十分接近随机了，每增加一个自由度，随机性增加的可不是一。"




##关于1.1中协商加密算法
> * 密钥交换算法，用于决定客户端与服务器之间在握手的过程中如何认证，用到的算法包括RSA，Diffie-Hellman，ECDH，PSK等

> * 加密算法，用于加密消息流，该名称后通常会带有两个数字，分别表示密钥的长度和初始向量的长度，比如DES 56/56, RC2 56/128, RC4 128/128, AES 128/128, AES 256/256

> * 报文认证信息码（MAC）算法，用于创建报文摘要，确保消息的完整性（没有被篡改），算法包括MD5，SHA等。

> * PRF（伪随机数函数），用于生成“master secret”。


![20170509104722086](media/15229088944991/20170509104722086.jpeg)


