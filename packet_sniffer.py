from scapy.all import *

try:

	def send_packet(src_MAC,src_IP,dst_IP,iFace,payload):
		pkt=Ether(src=src_MAC)/IP(src=src_IP,dst=dst_IP)/TCP()/Raw(load=payload)
		ans,unans=srp(pkt,iface=iFace,timeout=3,verbose=0)
		for sent,received in ans:
			print("Response received from {received[IP].src}")
			src_MAC=input("[+]Enter MAC address: ")
			src_IP=input("[+]Enter source IP address: ")
			dst_IP=input("[+]Enter destination IP address: ")
			iFace=input("[+]Enter iface: ")
			payload=input("[+]Enter payload: ")

	send_packet(src_MAC,src_IP,dst_IP,iFace,payload)

	while True:
		more=input("Do you want to send more packets?(y/n): ")
		if more.lower()=="y":
			req=input("Want to ammend changes in packets(y/n): ")
			if req.lower()=="y":
				src_MAC=input("[+]Enter MAC address: ")
				src_IP=input("[+]Enter source IP address: ")
				dst_IP=input("[+]Enter destination IP address: ")
				iface=input("[+]Enter iface: ")
				payload=input("[+]Enter payload: ")
			else:
				payload=input("[+]Enter payload: ")
			send_packet(src_MAC,src_IP,dst_IP,iFace,payload)
		else:
			break 
except KeyboardInterrupt:
	print("Sniffer program shutting down")
	
				
