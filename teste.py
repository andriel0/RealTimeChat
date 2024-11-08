import socket

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = client.recv(1024)

if msg == b'SALA':
    print(msg)
    client.send(b'Andriel')
    client.send(b'Games')
