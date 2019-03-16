# UDP socket programming

## configuration

![](media/15405269475515/15405621501089.jpg)

## UDP Ping client

![-w250](media/15405269475515/15405621833952.jpg)

It will send 10 packets one by one, and report time out event. After ten packets, it reports average RTT, minimum RTT, max RTT and loss rate.

## HeartBeat
![-w250](media/15405269475515/15405628205902.jpg)

Client send a packet with sequence number every second.

after send ten packet, we pretend Client to go offline, and we see Server report client's not online.

