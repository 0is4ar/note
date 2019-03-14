# new_note


## News resource

Recent news: CVE-2019-5736

Ghidra is coming soon

### reddit
netsecstudents
hacking
blackhat
reverseEngineering
netsec

### news

threatpost

### forums

Hack Forums

### twitter

Andy gaio

X0rz


## XSS 

#### reflected XSS

`error.php?message=<script>alert('1')</script>`

#### Blog 



#### DOM XSS

Basically is similar to reflected XSS, but the malicious code won't go through backend. Just go Javascript

Can be the same as the example in reflected XSS, but using Javascript, like

`var message = url.substring(url.indexOf(‘message=’) + 8, url`


### prevent XSS

identify every instance within the application where user-controllable data is being copied into responses

reflected XSS : Use X-XSS-Protection header(not supported by Firefox)

CSP: header that a whitelist of document capabilities. and disable inline javascript by default

could be 

#### validate output

Using HTML encoding 
`browswer` will know this is not a `key work` when redering pages.

#### limited HTML

not only limiting tag like `<script>`, things like
`<b style=behavior:url(#default#time2) onbegin=alert(1)>` also triggers XSS

#### prevent DOM XSS

using JavaScript to santinize strings. (client side is more efficient, server side santinization also works tho)


## Same-Origin

![Image](img/1551416287-29360.png)


Cross-Origin Resource Sharing. (CORS)
use OPTIONS, then get
`Access-Control-Allow-Origin: http://foo.example`


```

text.replace(“<script>”, “#”)
<script>alert(“hello”)</script>
<img src=a onerror=alert(“hello”)>
<img src=a onload=alert(“hello”)>
<svg/onload=alert(hello')>
javascript:alert(“hello”)
data:text/plain,alert(“hello”)
<iframe src=javascript:alert(“hello”)>
/*--></title></style></textarea></script></xmp><svg/onload='+/"/+/onmouseover=1/+/[*/
[]/+alert(1)//'>
```

## CSRF

![Image](img/1551421218-22226.png)

??simple request
??what custom headers
??bypassing check referer
??origin headers

`Referer` is a special header(like 'Host") that can not be set inside the browser

1.Require a custom header 

The existence of custom header is enough, because Non-standard header cannot be set in a CSRF attack.

- How to let browser request with non-standard header when normally used?


2.Check referer

No referrer, only referer

### Why not use referer

1.A lot of browser does not send referer header. 

2.if your website has an open redirect vulnerability, referer checks can be bypassed for GET requests. Of course, GET requests should not change state


### CORS

When performing cross-domain Ajax requests. Modern browsers will insert(mutely) an extra "preflight", which is an OPTIONS request


!victim's browser decide how to deal with non-same origin requests.
if victim's browser found that website is willing to AJAX from ther site, the browser request that site and retrive data, sends it back. 


## sign 

|symbol|name|
---|---
'|single quote
"|double quote
[|square bracket
{|bracket
(|parentheses
,|comma
.|period
\_|underscore
!|exclamation point
?|question mark
&|ampersand
\#|numder sign
*|asterisk
;|semicolon
:|colon


## SSL/TLS

Transport Layer Security/Secure Sockets Layer

Use asymmetric to exchange key(sesison key), use symmetric cryptography to encrpt content to be transmitted. 

### attack

```
OPENSSL的heart bleeding
POODLE 攻击
FREAK攻击
对伪随机数生成器的攻击
利用证书的时间差进行攻击
```

### relationship

SSL is now deprecated predecessor of TLS

when exchange key, we use ECDHE more now, because parameters for key exchange of ECDHE will not transmit on channel
but ECDHE is slower

### Certification

#### how it works

priv_key(hash(certification)) is added to the end of certification, the priv_key is from the one giving out the certification.

This way, the attacker can't forge the hash, because he can't forge a encryped hash which could be decrpted to a correct hash of the certification

#### CA

The certification issued by a CA will contain a `signature` of that CA. 
client could check the CA by checking the signarue with `intermediate` CA.
root CA can't be forge because it is natively installed in browswer and operating system.

![Image](img/1551454170-14507.png)

#### key exchange

![Image](img/1551454640-11835.png)




## Difference TCP UDP

1. TCP is persistent connection with three way handshake
2. TCP is reliable of its sequence ordering and retransmission mechanism(acknowledge) which is not present in UDP. (UDP checksum simply discard)
3. TCP has flow control, detect network quality


## Cookie

Cookie is simply some strings, server send Set-Cookie in header to let client browser store at local, and when request the same domain, broswer will send the Cookie for that domain in HTTP header.

And the most important usage for Cookie is Session management.

Like PHP, browser sends packet with PHPSESSIONID in cookie, in PHP, there's a `superglobal` named `$_SESSION`, 

PHP's session management is a 'table', `$_SESSION` return the items in dictionary with key value `PHPSESSIONID` of that thread.

and this `item` is also a dictionary. Can be used like `$_SESSION['name']`


## PHP serilization

`__construct`
`__destruct` the destructor, which will be invoked when the object will be kill.


## How I hack the web application

When I first got into the link, the website looks very simple. So I was think that this must be a web application NCC Group created with a lot of vulnerbilities. And I tried to get familiar with the functions of the web application, by browsign like a normal user. How to create issues something. And take notice of inputs that may go through database, or that may be revealed on the webpage content later(XSS), or some weird action or parameters like `path=`. After this, because I believe there might be a lot of vulnerability and the web application doesn't have many textarea. I simply tried to create a issue and filled with XSS test in all textareas. And I find XSS. Then create issues with SQL injection test, then got error, so it's an insert SQL injection

In order to get familiar with the web application more. I ran gobuster and use a comman wordlist to scan directories in background.

And me myself just did some basic tests. Like request `.robots.txt` `.git` `index.php.swp`. `../../../`, fortunately or unfortunately for me, there low hanging fruit doesn't exist.


After I got the result of gobuster. There's a directory named doc. So I found the real name of the web application. This could be a great breakthrough. Then I just googled the vulnerabilities of this web application in CVE details as well as exploit db. 

This is where I got a lot of vulnerabilities.

One of them is the code injection. Based on code injection, I got to know more about the construction of the web application, and I read the default password for the administrator, by the way, this is a weak password, then I could test more vulnerabilities since only administrator could manager projects, users.

Also by using the code injection, I found the source code of this project. I'm not sure quite sure about what you want candidates to do with the source code. But I just can't pretended to be like never seeing it. So I downloaded the source code, then I review the code, this is the white-box part of the test. By this, I find the second-order SQL injection. Which is really deep, because I think the button for copying a issue from a project to another is intentionally deleted by you.



## DNSSEC

Clinet -> local DNS -> root

in normal DNS, root return the ip address of ns.com, it could easily be spoofed

DNSSEC protects DNS resolvers by digitally signning all NDSSEC replies



- RRSIG – a hash of the other RRs that is encrypt using the private key by the authoritative name server
- DNSKEY – the public key associated with the private key used to encrypt the RRSIG, a DNS resolver then using this public key to decypt the RRSIG and check that the plaintext is a hash of the other RRs
- DS – a hash of the DNSKEY used in the zone that the DNS resolver is about to query so that the resolver can check that the response from the next name server query has not had the DNSKEY altered because it can check the DNSKEY received with DS received from the last name server.

### DNS spoofing

DNS packet **ID**, client generates a random number as the ID, then sent it to the server, server return this id

DNS client do not care about where is the DNS return packet from. **ONLY care about ID**

may first use arp spoofing to pretend to be DNS server.
Then return 

### DNS Zone Transfer

popular tool: DNSRecon, NDSenum

zone transfer is to copy DNS record database from one DNS server to another, including copying the zone file from server A to B. This `zone file` contains all DNS names configured for that zone. 

server B must be authorized for zone transfer, but due to misconfiguration.

when use `host -l <domain name> <dns server name>`


## Hacking a vending machine

1. I will naturally google if there has existed a way to do so. Or at least get some inspiration. If there's no such things, I'll try to find out the model of the vending machine and try to find out the manual of the vending machine.

2. If there's no external source I can refer to. I will try myself.

3. First I try to find out what kind of input I could have to that machine. Like power button, number input, touch screen, serial port for debug, money or card insertation.

4. If I found ways I could be more familiar with, like maybe I can use a app in phone to top money for that machine, reverse engineering the app and oberseve how it communicates with the machine would be on my todo list.

5. I may try to use a computer to connect to the debug serial.

6. use debug buttom

7. In the input are very human friendly, like having touchscreen, I may wandering what kind of Operating system it use and what kind of APP it use then try to do sandbox escape through things like making the CPU overload by touching something, so crash, or exploit input method something.

8. If it just has number pad, I may try to input all kinds of number to see if error happens.

9. If all above ways don't work. I will consider using the power button to restart the machine to see what will happen.
