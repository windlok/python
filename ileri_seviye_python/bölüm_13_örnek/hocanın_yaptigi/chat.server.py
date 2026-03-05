import socket 

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADRESS = (SERVER, PORT)
FORMAT = "utf-8"
BYTESIZE = 1024
DISCONNECT_MESSAGE = "quit"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADRESS)
server_socket.listen()
print(f"Server {SERVER} adresinde {PORT} portunda dinleniyor...")

client_socket, client_address = server_socket.accept()
client_socket.send("Server'a bağlandınız!".encode(FORMAT))

while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        print(f"{client_address} bağlantısı kesildi.")
        break
    else:
        print(f"{client_address} mesajı: {message}")
        response = input("Server'dan cevap giriniz: ")
        client_socket.send(response.encode(FORMAT))

        if response == DISCONNECT_MESSAGE:
            print("Sunucu bağlantıyı sonlandırdı.")
            break

server_socket.close()        

    
