import socket
import threading 
import mysql.connector

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',8888))
s.listen()
clients = [] #This contains the clients who are available 

def client_connect():
    while True:
        print(f"Server is running.\n")
        c,addr = s.accept()
        print(f"Connection is connected at {addr}")
        clients.append(c)
        Thread = threading.Thread(target=handle_client,*args=(c,))
        thread.start()
if __name__ == "__main__":
    client_connect()