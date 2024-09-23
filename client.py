import socket

c = socket.socket()
c.connect(('localhost', 8888))

try:
    while True:
        
        message = c.recv(1024).decode()
        if not message:
            break  
        print(message)  

       
        if "Choose one of the below options:" in message:
            choice = input("Enter your choice:\n")  
            c.send(choice.encode())  

        #This is the implementation of the 2nd option.
        elif "Remaining Players" in message or "No remaining players" in message:
            print(message)  

except KeyboardInterrupt:
    print("Client closed.")
finally:
    c.close()
