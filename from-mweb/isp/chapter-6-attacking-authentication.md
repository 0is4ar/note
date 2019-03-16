# Chapter 6 Attacking Authentication

## Common Vul

### Completely Unprotected

A admin page is just protected by using a hard guess url. like `/menus/secure/ff457/addNewPortalUser2.jsp`

no reference to this page in site.

#### compromise

audit the javascript carefully, and may find some like:

```text
var isAdmin = false; ... 
if (isAdmin) 
{
     adminMenu.addItem(“/menus/secure/ff457/addNewPortalUser2.jsp”,“create a new user");

}
```

### Direct Access to Methods

`http://wahh-app.com/public/securityCheck/getCurrentUserRoles`

you should check for the existence of other similarly named methods such as getAllUserRoles, getAllRoles, getAllUsers, and getCurrentUserPermissions

### identifier-based functions

When a function of an application is used to gain access to a specifi c resource, it is common to see an identifi er for the requested resource being passed to the server in a request parameter

[https://wahh-app.com/ViewDocument.php?docid=1280149120](https://wahh-app.com/ViewDocument.php?docid=1280149120)

doc id这个链接只有在拥有它的user 登录时才会显示。 而这个链接本身并不check permission

need guest "ViewDocument.php" and docid

docid basically is random number

> tips: access log can be gold information to get some docid

### Multistage Function

有些函数有几个步骤，几个步骤都是实际上应该需要管理员权限的，但是只在第一个步骤处验证用户是否有管理员权限，if attacker proceed directly to 后面的步骤，就绕过了权限验证了

### static file

for example, buying a ebook. After payment, download `https://wahh-books.com/download/9780636628104.pdf`

this is a completely static file. If it is hosted on a traditional web server. 可以直接被拿到

### misconfiguration

if an administrative function to create a new user uses the POST method, the platform may have a deny rule that disallows the POST method and allows all other methods. However, if the application-level code does not verify that all requests for this function are in fact using the POST method, an attacker may be able to circumvent the control by submitting the same request using the GET method. Since most application-level APIs for retrieving request parameters are agnostic as to the request method, the attacker can simply sup- ply the required parameters within the URL query string of the GET request to make unauthorized use of the function

如果get 和 post 都被ban了， 甚至可以用HEAD方法，按照规定，收到HEAD的服务器进行和收到GET一样的操作，但是只会返回一个Header，HTTP包不会有其他内容。但是这样已经可以达到操作的目的了。

另外，还有一些服务器甚至将所有 其它 请求方法当做GET来处理

### insecure access control method

#### parameter-based access control

[https://wahh-app.com/login/home.jsp?admin=true](https://wahh-app.com/login/home.jsp?admin=true)

### Referer-Based Access Control

### Location-Based Access Control

## Attacking Access Control

### Testing with Different User Accounts

使用管理员用户和普通用户来get site map 看有没有可能普通用户看得到不该看的东西

Burp Suite lets you map the contents of an application using two different user contexts. Then you can compare the results to see exactly where the content accessed by each user is the same or different

### Testing Multistage Processes

