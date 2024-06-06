import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print("server çalışıyor...\n")

client_socket, client_address = server.accept()
client_socket.send("server bağlantınız yapıldı.\n".encode(FORMAT))

while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send("quit".encode(FORMAT))
        print("çıkış yapıldı...")
        break
    else:
        print(f"{message}\n")
        message = input("mesaj: ")
        client_socket.send(message.encode(FORMAT))

server.close()
client_socket.close() 





