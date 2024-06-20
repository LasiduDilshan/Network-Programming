from scapy.all import *


def process_packet(packet):
    #print(packet.summary())
    #packet.show()
    if Ether in packet:
        print("Source MAC: ", packet[Ether].src)
        print("Destination MAC: ", packet[Ether].dst)
    if IP in packet:
        print("Source IP: ", packet[IP].src)
        print("Destination IP: ", packet[IP].dst)
        print("Proto: ", packet[IP].proto)
    if TCP in packet:
        print("Source Port: ", packet[TCP].sport)
        print("Destination Port: ", packet[TCP].dport)

    print()

def capture_live_traffic():
    sniff(filter="tcp", prn=process_packet, store=0)

if __name__ == "__main__":
    capture_live_traffic()
