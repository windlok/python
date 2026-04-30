# benim_yaptıgım — Chat denemesi (server/client)

Bu sürümde amaç: iki tarafta da `send`/`recv` kullanarak mesajlaşmayı denemek.

## Çalıştırma

Terminal-1:
```bash
python "ileri_seviye_python/bölüm_13_örnek/benim_yaptıgım/chat.server.py"
```

Terminal-2:
```bash
python "ileri_seviye_python/bölüm_13_örnek/benim_yaptıgım/chat.client.py"
```

## Protokol / akış

- HOST/PORT: `gethostbyname(gethostname())` ve `12345`
- Server `accept()` eder.
- Server kullanıcıdan `input()` ile mesaj alır, client'a gönderir.
- Client `recv()` ile mesajı alır, sonra kullanıcıdan mesaj alıp server'a yollar.
- `exit` yazılırsa çıkış mesajı gönderilir.

## Bilinçli “deneme” notları

Bu dosyalar öğrenme amaçlı olduğu için akış tam “sonsuz sohbet” gibi değil:

- Server tarafında her döngüde yeniden `accept()` çağrılıyor; bu, tek bağlantı üzerinden devam etmek yerine yeni bağlantı beklemesine yol açabilir.
- Server bazı durumlarda aynı mesajı iki kez `send()` ediyor.

Bunları birer alıştırma olarak düşünebilirsin.

## Alıştırmalar (bu sürümü iyileştir)

- `accept()` çağrısını döngünün dışına al ve tek `client_socket` ile sohbeti sürdür.
- Server'ın mesajı iki kez göndermesini düzelt.
- `exit` geldiğinde hem client hem server socket'lerini düzgün kapat.
