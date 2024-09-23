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
    """Fetch and send the list of remaining players to the client."""
    try:
        # Connect to the database (assuming you already have a connection function)
        db_connection = database()
        if not db_connection:
            raise Exception("Database connection failed")

        cursor = db_connection.cursor()

        # Query to select remaining players (where `price` is NULL, indicating unsold)
        query = "SELECT player_name, nationality, role FROM players WHERE price IS NULL;"
        cursor.execute(query)

        # Fetch all remaining players
        remaining_players = cursor.fetchall()

        if remaining_players:
            response = "Remaining Players:\n"
            for player in remaining_players:
                response += f"Name: {player[0]}, Nationality: {player[1]}, Role: {player[2]}\n"
        else:
            response = "No remaining players available.\n"

        # Send the list of players to the client
        c.sendall(response.encode())

    except mysql.connector.Error as e:
        error_message = f"Database error: {str(e)}"
        print(error_message)
        c.sendall(b"An error occurred while fetching the player data from the database.\n")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        c.sendall(b"An error occurred while fetching the player details.\n")

    finally:
        # Clean up
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()


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
