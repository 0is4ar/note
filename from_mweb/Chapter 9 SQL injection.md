# Chapter 9 SQL injection

## inject to sql
### some basic statements

#### INSERT

`INSERT INTO users (username, password, ID, privs) VALUES (‘daf’, ‘secret’, 2248, 1)`

可能这是一个正常的注册程序，但是在username 处可以 注入用户权限，然后再把后面的闭合
payload: `foo', 'bar', 9999, 0) -- 

但是需要注意的是必须要知道 how many parameters are required, what types they are.

can test with

foo’)-- 
foo’, 1)-- 
foo’, 1, 1)-- 
foo’, 1, 1, 1)--

because 1 will be automatically convert to string if it is.

if 1 is still rejected, try value 200

#### UPDATE

`UPDATE users SET password=’newsecret’ WHERE user = ‘marcus’ and password = ‘secret’`

`UPDATE users SET password=’newsecret’ WHERE user = ‘admin’ or 1=1`

this resets the value of every users' password

### Finding SQL

#### TIPS

be sure to walk through to completion any multistage processes 

有些multistage，在第一个stage输入的数据可能在最后stage之后，才会一起处理

#### inject into string

##### 测试


1. 一个 ' 闭合前面。'' 就escape 第二个 ' 了。输入这两种看有没有变化

2. 输入concatenation 符号，看是不是连接了

select 'input'

Oracle: ‘||’FOO   
MS-SQL: ‘+’FOO   
MySQL: ‘ ‘FOO (note the space between the two quotes)

3. 输入 % (sql的wildcard 即 通配符)

