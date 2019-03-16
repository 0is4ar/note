# PHP反序列化

相关magic函数：

- _construct
    对象在构建时执行
- _destruct
    对象被销毁（e.g.程序结束运行)时执行
- _sleep 序列化时执行
- _wakeup  反序列化时执行


反序列化漏洞的厉害之处在于，
一个程序员接受了一个\$haha
并且这个haha被设计为是前端传过来的一个User对象的序列化，
他以为传入会是`O:4:"User":2:{s:3:"age";i:20;s:4:"name";s:4:"John";}`
就正常使用\$user = unserilize(\$haha)


但是unserilize这个函数是众生平等的，你告诉他这是什么class就会成什么class，所以在hacker传入参数时，告诉他是另外一个class,那么就可能可以执行内部的一些关键的类_destruct或_wakeup函数，比如读取文件的类什么的


`O:9:"FileClass":1:{s:8:"filename";s:5:"1.txt";}`

这是一个序列化的例子O:9代表名字为九个字符长的class

unserilize这个函数是众生平等的，你告诉他这是什么class就会成什么class，所以在hacker传入参数时，告诉他是另外一个class,那么就可能可以执行内部的一些关键的类_destruct或_wakeup函数，比如读取文件的类什么的



