from scapy.all import *

try:

	a=input("Enter the types of packets to be sniffed(tcp/udp/arp): ")
	b=int(input("Enter the number of packets to be sniffed: "))

	Sniffer_packets=sniff(count=b,filter=a)
	Sniffer_packets.show()
	
	c=input("Do you want to view the layers of a packet(y/n): ")
	
	while True:
		
		if c.lower()=='y':
			d=int(input("Enter the index of the packet: "))
			Sniffer_packets[d].show()
		else:
			break
except KeyboardInterrupt:
	print("\nSniffer program shutting down: ")
