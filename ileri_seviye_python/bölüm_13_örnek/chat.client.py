import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


HOST = socket.gethostbyname(socket.gethostname())

PORT = 12345

client_socket.connect((HOST, PORT))

while True:
    gelen_mesaj = client_socket.recv(1024).decode("utf-8")
    print(f"kullanıcıdan gelen mesaj: {gelen_mesaj}")
    
    mesaj = input("mesaj giriniz:  //sohbetten çıkmak için exit yazınız")
    if mesaj == "exit":
        client_socket.send("Sohbetten çıkılıyor...".encode("utf-8"))
        break
    else:
        client_socket.send(mesaj.encode("utf-8"))

# Döngüden çıkınca bağlantıyı kapat
client_socket.close()