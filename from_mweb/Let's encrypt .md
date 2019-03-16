# Let's encrypt 

## How does it work

When first time interact with Let's Encrypt, a key pair is generated.

Three processes to authorize a server with key pair has domain www.A.com:

(1) Let's Encrypt

- Let's Encrypt sends a nonce to server.
- Let's require server to put a specified content in a specified url, like 'aoisjdf' in www.A.com/vjico

(2) Server 

- use privacy key of the key pair to sign the nonce, then send back signature.
- put 'aoisjdf' in www.A.com/vjico

(3) Let's Encrypt

- Varify signature
- Varify content in www.A.com/vjico

---
Then it's all-set. The server can get the certificate for www.A.com

## Contrast it with PKI

In my opinion, it is not at opposite side of PKI. Instead, Let's Encrypt as a CA is a part of the PKI system.

The difference is Let's Encrypt simplify and automize the process of getting a certificate from a RA and then activating it from a CA.

So, compare to traditional CA, it's free, more flat(may less intermediate CA). But only support certificate for Domain Validation, not yet for Organization Validation.





