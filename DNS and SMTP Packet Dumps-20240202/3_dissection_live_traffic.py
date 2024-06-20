import socket
from scapy.all import *

def process_packet(packet):
    #print(packet.summary())
    packet.show()
    print()

def capture_live_traffic():
    sniff(prn=process_packet, store=0)

if __name__ == "__main__":
    capture_live_traffic()
