import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

rooms = {}


def broadcast(room, msg):
    for r in rooms[room]:
        if isinstance(msg, str):
            msg = msg.encode()

        r.send(msg)


def sendMessage(name, room, client):
    while True:
        message = client.recv(1024)
        message = f'{name}: {message.decode()}\n'
        broadcast(room, message)


while True:
    client, addr = server.accept()
    client.send(b'SALA')
    name = client.recv(1024).decode()
    room = client.recv(1024).decode()

    if room not in rooms.keys():
        rooms[room] = []

    rooms[room].append(client)
    print(f'{name} entrou na sala {room}. INFO {addr}')
    print(rooms)
    broadcast(room, f'{name} entrou na sala.\n')
    thread = threading.Thread(target=sendMessage, args=(name, room, client))
    thread.start()