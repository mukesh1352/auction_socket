import socket

c = socket.socket()
c.connect(('localhost', 8888))

try:
    while True:
        message = c.recv(1024).decode()
        if not message:
            break  # Break the loop if no message is received
        print(message)  # Print the received message

        if "Choose one of the below options:" in message:  # Check if options are sent
            choice = input("Enter your choice:\n")  # Get the choice from the user
            c.send(choice.encode())  # Send the choice as bytes

except KeyboardInterrupt:
    print("Client closed.")
finally:
    c.close()
