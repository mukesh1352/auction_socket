import socket
import mysql.connector
import threading
import time

initial_purse_amount = 10000
extra_purse_amount = 10000
def database():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "venasaur123",
            database = "player_info"
        )
        cursor = conn.cursor()
        return conn,cursor
    except mysql.connector.Error as err:
        print(f"Database error:{err}")
        exit(1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost',8888 )) #binding with the host

s.listen(5) #listen to 5 clients

def handle_client(c,addr):
    print(f"Connected with the client at {addr}")
    print(f"Welcome to the IPL AUCTION\n".encode())

def accept_connection():
    while True:
        c,addr = s.accept()
        client_thread = threading.Thread(target=handle_client,args=(c,addr))
        client_thread.start()

accept_connection()