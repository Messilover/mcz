import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect('192.168.182.1', 2333)
sk.send('123456789')
sk.close()