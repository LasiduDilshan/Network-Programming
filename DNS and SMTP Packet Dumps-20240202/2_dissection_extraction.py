from scapy.all import *

packet_dump_file = "dns_pkts_analysis.pcap"
#packet_dump_file = "pkts_en2150_2_dns.pcap"
#packet_dump_file = "pkts_en2150_2_mail.pcap"
packets = rdpcap(packet_dump_file)

def dissect_packet(packet):
    #print(packet.summary())
    packet.show()
    if Ether in packet:
        print("Source MAC: ", packet[Ether].src)
        print("Destination MAC: ", packet[Ether].dst)
    if IP in packet:
        print("Source IP: ", packet[IP].src)
        print("Destination IP: ", packet[IP].dst)
    if TCP in packet:
        print("Source Port: ", packet[TCP].sport)
        print("Destination Port: ", packet[TCP].dport)
        print("Window: ", packet[TCP].window)

for i, packet in enumerate(packets[:20]):
    print(f"Packet {i + 1}:")
    #packet.show()
    dissect_packet(packet)
    print()
