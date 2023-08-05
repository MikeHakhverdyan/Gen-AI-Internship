import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = 'ENTER IP ADDRESS'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive():
    connected = True
    while connected:
        message = client.recv(1024).decode(FORMAT)
        print(message)


def send():
    active = True
    while active:
        message = input().encode(FORMAT)
        # message = "!DISCONNECT".encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)

        if message == DISCONNECT_MESSAGE:
            active = False

    client.close()


t = threading.Thread(target=send)
t.start()
receive()