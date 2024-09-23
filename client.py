import socket

c = socket.socket()
c.connect(('localhost', 8888))

try:
    while True:
        message = c.recv(1024).decode()
        if not message:
            break  # Break the loop if no message is received
        print(message)
except KeyboardInterrupt:
    print("Client closed.")
finally:
    c.close()
