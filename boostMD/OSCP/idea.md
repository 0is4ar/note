# example hack

## coughs

- system administrator may mix up which service is listening on which port  
- there might be service on a very high port
- don't forget UDP scan, default nmap doesn't cover UDP
- user already gahtered user list to brute force SSH key
- remember to check vulnerability of web server

## reconnaissance

### dns

```
for i in 10.11.1.{0..255}
do
host $i
done
```

then find a interesting one   
**make sure this one does not require any others to complete it**


### hint 

through domain, we know the name of the machine
go to IRC channel
`!alpha`

## information gathering

### light scan

**first thing to do is revert the machine**

`nmap 10.11.1.71 --top-ports 10 --open`

**service in result is default service on that port!!**

### heavy scan

`nmap 10.11.1.71 -p- -sV --reason --dns-server XXX`

-p- means complete scan (TCP 1-65535)  

--reason  lets nmap to show why it thinks that service and version on certain port

nmap recognize domain things by host's reponse relating to its resolve.conf  
but we can use --dns-server to specify which dns-server to use manually  
in course material, we learn how to know the dns server

**heavy network load may influence result of nmap, which is unacceptable**

### service

#### TCP 22

SSH may not be the low hanging fruit

`nc -nv 10.11.1.71 22`  
use nc to connect may get SSH and system version in banner

use the SSH version also provides information about linux version  
it's not like for a Windows machine to use SSH

SSH may use password and privatekey for authentication

password prompt means it's very likely to use password for some users to authenticate  
No password prompt doesn't mean it does not use password for authentication

`ssh root@10.11.1.71`
we can the ECDSA key 

>Now what happens if you see multiple SSH services on different ports which have the same key? What could it mean if they are different? Why would you see the same key on another box? All questions to think about... As this is not the case here, we will not answer that  (*cough* but it is in the labs *cough*).

##### use nmap script to determine SSH fingerprint

`ls -lh /usr/share/nmap/scripts/*ssh*`
`nmap 10.11.1.71 -p -sV --script=ssh-hostkey`

then we can know all information in the last section

![](_v_images/20190113134605572_2015648132.png =696x)

##### SSH brute force

Recommend SSH brute force tools: A custom wordlist for the target (using another vulnerability or CeWL/wordhound),
Hydra (don't forget about "-e [VALUES]"),
Patator (Password fuzzer rather than brute force),
Crowbar (great for brute forcing private keys),
Metasploit's ssh_login.

#### HTTP

basic HTTP authentication may only exist on a "landing page" like admin.php
but other page can be access from admin.php may not need authentication,  
so we may brute force those pages to bypass authentication

`curl -i 10.11.1.71`  
-i means include header of response

`curl -i -L 10.11.1.71`  
-L means follow redirection

a few things to check

##### Internal and External links

`curl 10.11.1.71 -s -L |grep "title\|href"`

-s means silent

##### comment

----

how it looks like( html2text makes it's like seen by browser)

`curl 10.11.1.71 -s -L | html2text -width '99' | uniq`

##### CMS version

`curl 10.11.1.71/README.md`

#### HTTP(hidden)

`curl 10.11.1.71/robots.txt -s | html2text `

> useful tool: parsero

##### url brute force

> the lab is desgined so shold not brute force anything for more than 30 minutes

tools:

DirB, wfuzz, Burp Suite, Gobuster

SecList: wordlist

`gobuster -u http://10.11.1.71 -w /usr/share/seclists/Discovery/Web_Content/comman.txt -s '200,204,301,302,307,403,500' -e`

-w means path to wordlist
-s means which response codes mean "successful"
-e means expand, output full length path instead of "/phpadmin"

##### url brute force(cgi)

`gobuser -w /Web_Contect/cgis.txt ......`