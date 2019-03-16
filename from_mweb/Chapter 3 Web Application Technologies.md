# Chapter 3 Web Application Technologies

## HTTP

### Proxy

#### HTTP Proxy

in unencrypted http, proxy 中转请求

#### HTTPS Proxy

首先Client 用 CONNET HTTP请求Proxy
Proxy reply with 200
then build a TCP connection for data transfer

so it's actually a TCP proxy

it's sort of like a pipe.

### REST

>the term “REST-style URL” is often used to signify a URL that contains its parameters within the URL file path

`http://wahh-app.com/search?make=ford&model=pinto`

REST style:
`http://wahh-app.com/search/ford/pinto`

## Server-Side Functionality

### Java Platform

### XML

### Web Services

Web services use Simple Object Access Protocol (SOAP) to exchange data. ꩀĠ怀SOAP typically uses the HTTP protocol to transmit messages and represents data using the XML format


SOAP being used by the server-side application to communicate with various back-end systems

If user-supplied data is incorporated directly into back-end SOAP messages, similar vulnerabilities can arise as for SQL.

#### SOAP vs WSDL

A SOAP message is a XML document which is used to transmit your data. WSDL is an XML document which describes how to connect and make requests to your web service.

Basically SOAP messages are the data you transmit, WSDL tells you what you can do and how to make the calls.

A quick search in Google will yield many sources for additional reading (previous book link now dead, to combat this will put any new recommendations in comments)

Just noting your specific questions:

Are all SOAP messages WSDL's? No, they are not the same thing at all.

Is SOAP a protocol that accepts its own 'SOAP messages' or 'WSDL's? No - reading required as this is far off.

If they are different, then when should I use SOAP messages and when should I use WSDL's? Soap is structure you apply to your message/data for transfer. WSDLs are used only to determine how to make calls to the service in the first place. Often this is a one time thing when you first add code to make a call to a particular webservice.

