import socket
import mysql.connector
from mysql.connector import Error
import threading

def database():
    try:
        connection = mysql.connector.connect(
            host='localhost',      
            user='mukesh',            
            password='V3nasaur@123',  
            database='players'
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
    return None

def handle_client(c, addr):
    print(f"Connected with the client at addr: {addr}")
    c.sendall(b"Welcome to the IPL AUCTION.\n")
    
    options = (
        "Choose one of the below options:\n"
        "1. Buy Player.\n"
        "2. Check the remaining players.\n"
        "3. Check the team players.\n"
        "4. Exit!\n"
    )
    
    while True:
        c.sendall(options.encode())
        choice = c.recv(1024).decode()
        
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                buy_player(c)
            elif choice == 2:
                see_player(c)
            elif choice == 3:
                team_players(c)
            elif choice == 4:
                print(f"Client at {addr} has exited.")
                c.close()
                break
            else:
                c.sendall(b"Invalid choice. Please try again.\n")
        else:
            c.sendall(b"Invalid input. Please enter a number.\n")

def buy_player(c):
    # Implement your logic for buying a player here
    pass

def see_player(c):
    # Implement your logic for checking remaining players here
    pass

def team_players(c):
    # Implement your logic for checking team players here
    pass

# Create socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8888))
s.listen(3)
print("Waiting for connections.\n")

# Connect to the database
db_connection = database()

while True:
    try:
        c, addr = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(c, addr))
        client_thread.start()
    except Exception as e:
        print(f"An error occurred: {e}")

# Close the server socket (unreachable in this infinite loop, but good practice)
s.close()
