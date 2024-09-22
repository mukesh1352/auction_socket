import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost',8888))

s.listen(3)
print("Waiting for connections.\n")

while True:
    c,addr = s.accept()
    print(f"Connected with the client at add:{addr}")
    c.send(bytes(f"Welcome to the IPL AUCTION.\n".encode()))
    