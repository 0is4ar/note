import collections
from pwn import *


list = []

#for i in range(10):
process = remote('95.213.235.103',8801)

process.recv(1024)
list += process.recvlines(10)

for i in list:
    print hex(int(i))

print [item for item, count in collections.Counter(list).items() if count > 1]

print len(list) - len(set(list))
