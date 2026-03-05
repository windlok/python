import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MESSAGE = "quit"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADRESS)

while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send(DISCONNECT_MESSAGE.encode(FORMAT))
        break
    else:
        print(f"Server'dan gelen mesaj: {message}")
        message = input("Mesajınızı giriniz: ")
        client_socket.send(message.encode(FORMAT))

        if message == DISCONNECT_MESSAGE:
            print("Bağlantıyı sonlandırıyorsunuz...")
            break

client_socket.close()        