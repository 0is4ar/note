# During Traceroute lab

mac 系统的 traceroute 发出是用UDP包，不断增加time to live 来实现的， 每一个hop收到一个packet, 会拆开看IP header，查看ttl是不是0，不是的话ttl-=1，然后再forward给下一个hop。当hop发现ttl is zero, then drop the packet and send a ICMP Time Exceeded\(type 11\) message back to the source of IP packet.

But for traceroute in other system, the packet send is not UDP but ICMP type '8'

