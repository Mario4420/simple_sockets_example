#!/usr/bin/python

import socket
import threading


HEADER = 64
PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
ENCODING = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    """
    handles incoming client connections
    """

    print(f"new connection: {addr}")

    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(ENCODING)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(ENCODING)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(addr, end=": ")
            print(msg)
    conn.close()


def start():
    """
    Starts the server
    """

    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"acitve conns: {threading.active_count() - 1}")


print(f"runnin' the server on address {ADDR[0]}")
start()
