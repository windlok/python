# bölüm_13 — Socket ile istemci/sunucuya giriş

Bu bölüm, Python'un `socket` modülü ile en temel TCP bağlantısını kurar:

- Server bir portta dinler
- Client bağlanır
- Server mesaj gönderir
- Client mesajı alır

Bu örnek **tek seferlik bağlantı** içindir (1 client bağlanır, mesaj alır, server kapanır).

## Çalıştırma (2 terminal)

1) Terminal-1: server'ı başlat

```bash
python "ileri_seviye_python/bölüm_13/server.py"
```

2) Terminal-2: client'ı çalıştır

```bash
python "ileri_seviye_python/bölüm_13/client.py"
```

## `server.py` (sunucu)

- `socket.socket(AF_INET, SOCK_STREAM)` -> TCP/IPv4
- HOST: `socket.gethostbyname(socket.gethostname())` ile makinenin IP'si alınır ve ekrana basılır
- PORT: `12345`
- `bind((HOST, PORT))` ve `listen()`
- `accept()` ile bağlantı bekler
- Bağlanan client'a `send(...encode("utf-8"))` ile mesaj yollar
- Sonra server socket'i kapatıp çıkar

> Not: Örnek tek bağlantı için `break` ile bitiyor. Gerçek server'larda `accept` döngüsü sürer ve `client_socket` da kapatılır.

## `client.py` (istemci)

- Aynı HOST/PORT'a `connect` eder
- `recv(1024)` ile gelen mesajı alır ve `decode('utf-8')` eder
- Bağlantıyı kapatır

## Sık sorunlar

- Aynı port kullanımda ise (`Address already in use`) portu değiştir ve iki dosyada da aynı yap.
- HOST bazı makinelerde LAN IP döndürür; lokal deneme için ikisini de `127.0.0.1` yapmayı dene.
- Firewall, bağlantıyı engelleyebilir.

## Alıştırmalar

- Server'ı “echo server” yap: client ne gönderirse geri yollasın.
- Birden fazla client kabul etmek için `accept()` döngüsünü genişlet.
- Mesaj protokolü ekle: önce uzunluk gönder, sonra içerik.
