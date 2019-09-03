from scapy.all import sniff, wrpcap
import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('192.168.182.1', 2333))
sk.listen(10)
s = sniff(filter='127.0.1.1', count=10)
wrpcap('pc.pcap', s)
print('successful catch the packet')
