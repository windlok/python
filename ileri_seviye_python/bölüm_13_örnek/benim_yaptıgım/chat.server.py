import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


HOST = socket.gethostbyname(socket.gethostname())

PORT = 12345

server_socket.bind((HOST, PORT))

server_socket.listen()

while True:
    print("sohbete baglanmanız için bekleniyor")

    client_socket , client_addres = server_socket.accept()

    print(f"{client_addres} adresli kullanıcı bağlandı...")

    mesaj = input("mesaj yazınız: ")

    client_socket.send(mesaj.encode("utf-8"))
    if mesaj == "exit":
        client_socket.send("Sohbetten çıkılıyor...".encode("utf-8"))
        break
    else:
        client_socket.send(mesaj.encode("utf-8"))
    
    gelen_mesaj=client_socket.recv(1024).decode("utf-8")
    
    print(f"kullanıcıdan gelen mesaj: {gelen_mesaj}")
server_socket.close()