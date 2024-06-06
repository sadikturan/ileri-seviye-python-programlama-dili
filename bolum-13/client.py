import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

client_socket.connect((HOST, PORT))

message = client_socket.recv(1024)

print(message.decode("utf-8"))

client_socket.close()

