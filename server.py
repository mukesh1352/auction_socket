import socket
import mysql.connector
from twisted.conch.insults.window import cursor


def database():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "venasaur123",
            database = "player_info"
        )
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Database error:{err}")
        exit(1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('localhost',8888 ))
