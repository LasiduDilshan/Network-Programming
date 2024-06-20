import socket
from scapy.all import *


def process_packet(packet):
    print(packet.summary())
    #packet.show()
    print()

if __name__ == "__main__":
    packets = sniff(filter="tcp", prn=process_packet, store=20)
    wrpcap("captured_packets.pcap", packets)
 
