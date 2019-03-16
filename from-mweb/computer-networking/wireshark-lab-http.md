# Wireshark Lab: HTTP

\[TOC\]

## My network configuration

![](../../.gitbook/assets/15385030326321.jpg)

## Basic HTTP GET/response

### Print

* Request

  ![](../../.gitbook/assets/15385026395859.jpg)

* Response

  ![](../../.gitbook/assets/15385026649278.jpg)

### Answer

1. Both my browser and server run HTTP 1.1
2. en-US and en
3. * My computer: 192.168.1.228
     * Server: 128.119.245.12
4. 200
5. Tue, 02 Oct 2018 05:59:02 GMT
6. 128 bytes
7. Yes, Ethernet protocol's header

## HTTP Conditional GET/response

### Print

* Request 1 ![](../../.gitbook/assets/15385034031905.jpg)
* Response 1

![](../../.gitbook/assets/15385037418051.jpg)

* Request 2

  ![](../../.gitbook/assets/15385037585935.jpg)

* Response 2

  ![](../../.gitbook/assets/15385042187061.jpg)

### Answer

8.No, I don't see.

9.Yes, because there're line-based text data in the packet, and I can explicitly see the file lines text in the packet.

10.Yes, I see. It follows by the Last-Modified time of the packet that responses to my last request for this page.

11.304 Not Modified, no explicit return contents. I can't explicitly see data or any other contents other than headers in this packet. Once server returns 304 Not Modified, browser just use the cache\(last received response packet's contents\) to render pages.

## Retrieving long documents

### Print

* Request 

  ![](../../.gitbook/assets/15385058680552.jpg)

* Response

![](../../.gitbook/assets/15385058971781.jpg)

### Answer

12.Only one. Number 1\(Frame 12\).

13.Frame 14

14.200 OK

15.Four segments

## HTML Documents with Embedded Objects

### Print

![](../../.gitbook/assets/15385064375054.jpg)

### Answer

16.I sent three requests.

* gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
* gaia.cs.umass.edu/pearson.png
* manic.cs.umass.edu/~kurose/cover\_5th\_ed.jpg

17.Serially, for the third request for conver\_5th\_ed.jpg was sent after the second request's response was received.

## HTTP Authentication

18.401 Unauthorized

19.`Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=\r\n`

