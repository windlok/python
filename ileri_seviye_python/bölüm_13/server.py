import socket 

#AF_INET IP4 kullanacagım dedik SOCK_STREAM ise protolu belirlerken kullanılıyor 
server_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST ="127.0.0.1" #DİNAMİK YAPMALIYIZ

# bu işlem dinamik yapmak için bizim pcnin hostnun verir
HOST =socket.gethostbyname(socket.gethostname())

print(HOST)

PORT = 12345

server_socket.bind((HOST, PORT))

#dinleme kısmı 
server_socket.listen()

while True:
    print("Sunucu dinleniyor...")
    client_socket , client_addres = server_socket.accept()
    print(f'adresi : {client_addres} bağlantı sağlandı')

    #baglanan birime mesaj göndermek için send kullanırız. 
    # mesajı byte türüne çevirmeliyiz bu yüzden encode kullanırız
    client_socket.send("Sunucuya bağlandınız".encode("utf-8"))

    server_socket.close()
    break
