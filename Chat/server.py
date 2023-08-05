import socket
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []


def remove_client(client):

    if client in clients:
        clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    connected = True
    while connected:
        message_len = conn.recv(HEADER).decode(FORMAT)
        if message_len:
            message_len = int(message_len)
            message = conn.recv(message_len).decode(FORMAT)
            message = f'{conn}: ' + message

            for client in clients:
                if client is not conn:
                    client.send(message.encode(FORMAT))

            if message == DISCONNECT_MESSAGE:
                connected = False

            print(f'{message}')

    conn.close()
    remove_client(conn)


def start():
    server.listen()
    print(f'Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print(f'Starting a Server')
start()
