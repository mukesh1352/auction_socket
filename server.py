import socket

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8888))
s.listen(3)
print("Waiting for connections.\n")

while True:
    try:
        c, addr = s.accept()
        print(f"Connected with the client at addr: {addr}")
        c.sendall(b"Welcome to the IPL AUCTION.\n")
        
        # Send options after connection
        options = (
            "Choose one of the below options:\n"
            "1. Buy Player.\n"
            "2. Check the remaining players.\n"
            "3. Check the team players.\n"
            "4. Exit!\n"
        )
        c.sendall(options.encode())
        
        clients.append(c)  # Append the client socket to the clients list

    except Exception as e:
        print(f"An error occurred: {e}")

# Close the server socket (unreachable in this infinite loop, but good practice)
s.close()
