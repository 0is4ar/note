# offsec\_mid

## Web

![Image](https://github.com/0is4car/note/tree/17cbec7cbb3c704511fc7b3519339650958ba070/writeup/offsec/img/1553034031-23460.png)

The page is like this, no other very suspecious things except for the `?path=` in url.

It looks like a LFI, in order to test, I tried ../../../../../../etc/passwd, however, due to nyu's waf, this is not allowed by nyu. so I tried other thigns like this:

* `?path=./welcome` return normal
* `?path=../welcome` cannot return anything.

So this implies this should have local file inclusion vulnerability

because there's no other valuable files up to that time. So the only valuable things seem to be the PHP source code. But I can't see the source code by simply include it for the code will be interpreted and executed. So

1. use php file filter to encode it to base64, 
2. got the base64 encoded code, and decode it in shell.

`?path=php://filter/convert.base64-encode/resource=./admin` no php as prefix, because the source code itself should be : `require($_GET['path']).'php'`

in this way, I got the source code,

The source code mentioned "db.sql", because this is sql and will not be interpreted, so I directly include it without any encode. Then I got the password of admin.

### after admin.

admin can upload a file, the file would not go through any check. So I uploaded a one-liner PHP webshell directly. Then got a shell, and got flag.txt

## Programming

### description

when connecting to the server, it returns a lot of characters.

sometimes it's apparently some ascii hex. sometimes base64 encoded things.

And every time it is different.

### how idea

It's for sure that Base64 encoded code should be decoded. But it's just some bytes not even ascii.

So I suspected if is was binary file. Then wrote them into a file `test`.

Then `file test` said it is a bzip2 compressed data. So I use bunzip2 to decompress it. And I got some characters again.

every time I got binary with ![Image](https://github.com/0is4car/note/tree/17cbec7cbb3c704511fc7b3519339650958ba070/writeup/offsec/img/1553035055-5749.png) on top, I use bunzip to unzip it again.

at last, my command was like hundreds of

`base64 -d test.txt|base64 -d|bunzip2|base64 -d|bunzip2|xxd -r -p|tr -d "'"|base64 -d`

`xxd -r -p` is equal to binascii.unhexlify, but it will add single quote to output, so use `tr -d "''`to trim the single quote.

## Binary

![Image](https://github.com/0is4car/note/tree/17cbec7cbb3c704511fc7b3519339650958ba070/writeup/offsec/img/1553035372-27447.png)

There's a get\_time function, which invode system with `/bin/date` or `/bin/sh` according to parameters.

simply ret to 0x004006bb got shell

## Reverse Engineer

### description

Input characters could be 'L' or 'R' or else. and theres a obj list,

every obj contains a value and two pointers to other objs.

if the character is 'L', jump to the first pointer, second if 'R', no jump if anything else.

Every step will add value to rsp-0xc. And finally compares the value with 0x257b

obj list like this:

![Image](https://github.com/0is4car/note/tree/17cbec7cbb3c704511fc7b3519339650958ba070/writeup/offsec/img/1553035817-28374.png)

### solution

think about use angr, but finally use z3. manually add a lot of rules for those nodes.

