import socket

PORT = 50005
BUFFER_SIZE = 1024
IP = "10.1.53.69"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP, PORT))
    while True:
        data = input('Please input > ')

        s.send(data.encode())
        print(s.recv(BUFFER_SIZE).decode())
