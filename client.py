import socket
import threading

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',9999))
