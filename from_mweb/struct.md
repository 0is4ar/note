# struct

struct.pack("bbHHh",ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
struct.unpack

![-w350](media/15432670796526/15432672101798.jpg)
![-w200](media/15432670796526/15432672779291.jpg)



pack之后的就是bytes了
unpack 之后返回一个tuple，按照'bbHHh'的顺序赋值即可得到

```python
        type, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)

```

```
struct.calcsize("i")
4
```

说明类型int 是4个bytes

