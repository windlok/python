import socket

client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST =socket.gethostbyname(socket.gethostname())

print(HOST)

PORT = 12345

client_socket.connect((HOST, PORT))

#gelen mesajı almak için kullanıyoruz. 1024 byte kadar veri alabiliriz.
message = client_socket.recv(1024).decode('utf-8')

print("Serverdan gelen mesaj:", message.decode('utf-8'))

client_socket.close()