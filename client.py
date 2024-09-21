import socket


def client_program():
    host = 'localhost'
    port = 9999

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print("Connected to the server.")
    except ConnectionError as e:
        print(f"Error connecting to the server: {e}")
        return

    # Receive welcome message
    welcome_message = client_socket.recv(1024).decode()
    print(f"Server: {welcome_message}")

    # Receive options
    options_message = client_socket.recv(1024).decode()
    print(f"Server:\n{options_message}")

    while True:
        choice = input("Enter your choice (1-4): ")

        # Input validation
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        client_socket.send(choice.encode())

        if choice == '4':
            goodbye_message = client_socket.recv(1024).decode()
            print(f"Server: {goodbye_message}")
            break

        # Receive response based on the choice
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")

    client_socket.close()


if __name__ == '__main__':
    client_program()
