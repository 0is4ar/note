# domain workgroup netbios smb samba kerbos ldap AD

## workgroup, domain

workgroup is similiar to domain
one can only join a workgroup OR a domain

one join several domains has only "one share directory"

when setup a computer, you can join a domain/workgroup, or windows will create a default workgroup named WORKGROUP(only you in it)

users in a domain get authenticated by a central controller

users in a workgroup authenticate their own


## AD


Active Directory 

Active Directory (AD) is a directory service that Microsoft developed for the Windows domain

A server running Active Directory Domain Services (AD DS) is called a domain controller



## LDAP, kernbos


AD is a directory services database, and LDAP is one of the protocols you can use to talk to it.

In an AD, Kerberos is used to authenticate users, machines, and services.

## SMB and NetBIOS

NetBIOS in 139 is implementation of API

SMB can use NetBIOS,
OR SMB can directly over TCP(445)

SMB is an application-layer network protocol mainly used for providing shared access to files, printers, serial ports, and miscellaneous communications between nodes on a network.

## RPC

RPC can over SMB

or directly over TCP on 135

One common use case for SMB is to make remote procedure calls (RPC) to another machine on a local network. 

## Samba

samba is linux implementation of SMB, it connects windows and linux

SMB is the same as "domain"

## dialect

The set of message packets that defines a particular version of the protocol is called a dialect. The Common Internet File System (CIFS) Protocol is a dialect of SMB

## samba

As of version 3 (2003), Samba provides file and print services for Microsoft Windows clients and can integrate with a Windows NT 4.0 server domain, either as a Primary Domain Controller (PDC) or as a domain member. Samba4 installations can act as an Active Directory domain controller or member server, at Windows 2008 domain and forest functional levels

