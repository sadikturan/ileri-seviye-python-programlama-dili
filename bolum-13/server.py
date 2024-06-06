import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST = "127.0.0.1"
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345

server_socket.bind((HOST, PORT))

server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()

    print(f"bağlantı yapıldı: {client_address}")
    print(client_socket, client_address)

    client_socket.send("merhaba".encode("utf-8"))
    
    server_socket.close()
    break

