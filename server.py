import socket
import threading
import mysql.connector

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',9999))
s.listen()
clients = [] #For storing the client information

def broadcast(message):
    for client in clients:
        client.send(message)
        
#def handle_client():
    
def recieve():
    while True:
        print("Server is running and listening ...")
        c,addr = s.accept()
        print(f"connection is established with {addr}")
        clients.append(c)
        #thread = threading.Thread(target=handle_client,args=(c,))
        #thread.start() #Starting the thread

if __name__ == "__main__":
    recieve()