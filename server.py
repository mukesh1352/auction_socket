import socket
import mysql.connector
import threading

initial_purse_amount = 10000
extra_purse_amount = 10000
max_connections = 10
active_clients = []  # List to manage connected clients

def database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="venasaur123",
            database="player_info"
        )
        cursor = conn.cursor()
        return conn, cursor
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        exit(1)

# Set up server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 9999))
s.listen(max_connections)

def handle_client(c, addr):
    print(f"Connected with the client at {addr}")
    active_clients.append((c, addr))  # Add to active clients list

    welcome_message = "Welcome to the IPL Auction!"
    options_message = (
        "Choose one of the below options:\n"
        "1. Buy Player\n"
        "2. See remaining players list\n"
        "3. Check team status\n"
        "4. Exit\n"
    )

    c.send(welcome_message.encode())
    c.send(options_message.encode())

    try:
        while True:
            client_choice = c.recv(1024).decode()

            if client_choice == '1':
                buy_player(c)
            elif client_choice == '2':
                remaining_players(c)
            elif client_choice == '3':
                check_team_status(c)
            elif client_choice == '4':
                c.send("Thank you for participating in the auction. Goodbye!".encode())
                break
            else:
                c.send("Invalid choice. Please select again.".encode())
    except ConnectionError as e:
        print(f"Client at {addr} disconnected: {e}")
    finally:
        active_clients.remove((c, addr))  # Remove from active clients list
        c.close()

def buy_player(c):
    # Logic for buying a player
    c.send("You chose to buy a player.\n".encode())

def remaining_players(c):
    conn, cursor = database()
    cursor.execute("SELECT name FROM players WHERE sold price IS NULL")
    players = cursor.fetchall()

    player_list = "Remaining Players:\n" + "\n".join([player[0] for player in players])
    c.send(player_list.encode())
    conn.close()

def check_team_status(c):
    # Logic for checking team status
    c.send("You chose to check your team status.\n".encode())

def accept_connection():
    print("Server is running and waiting for connections...")
    while True:
        if len(active_clients) < max_connections:  # Check for max connections
            c, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(c, addr))
            client_thread.start()
        else:
            print("Max connection limit reached. Waiting for a slot...")

accept_connection()
