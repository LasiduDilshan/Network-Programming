from scapy.all import *

packet_dump_file = "dns_pkts_analysis.pcap"
#packet_dump_file = "pkts_en2150_2_dns.pcap"
#packet_dump_file = "pkts_en2150_2_mail.pcap"
packets = rdpcap(packet_dump_file)

for i, packet in enumerate(packets[:20]):
    print(f"Packet {i + 1}:")
    packet.show()
