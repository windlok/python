# hocanın_yaptigi — Ping-pong chat (referans akış)

Bu sürüm, tek client ile “sırayla mesajlaşma” (request/response) akışını daha net kurar.
Bağlantı kapatma komutu: `quit`.

## Çalıştırma

Terminal-1:
```bash
python "ileri_seviye_python/bölüm_13_örnek/hocanın_yaptigi/chat.server.py"
```

Terminal-2:
```bash
python "ileri_seviye_python/bölüm_13_örnek/hocanın_yaptigi/chat.client.py"
```

## Akış

- Server başlar, `accept()` ile bir client bekler, “Server'a bağlandınız!” mesajını gönderir.
- Döngü:
	1) Server `recv()` ile client mesajını alır.
	2) Mesaj `quit` ise bitirir.
	3) Değilse server kullanıcıdan cevap alır (`input`) ve client'a yollar.
	4) Server'ın cevabı `quit` ise bitirir.

- Client tarafı:
	1) `recv()` ile server mesajını alır.
	2) Mesaj `quit` ise (gerekirse) `quit` gönderip çıkar.
	3) Değilse kullanıcıdan mesaj alır ve server'a yollar.

Bu yüzden iki tarafta da sıralama önemlidir: biri `recv` beklerken diğeri `send` yapmalıdır.

## Sık sorunlar

- Host/port farklıysa bağlantı kurulmaz; iki dosyada da aynı olmalı.
- Port doluysa değiştir.
- `quit` yazdığında bağlantı kapanır.

## Alıştırmalar

- Mesajlara timestamp ekle.
- Mesajları log dosyasına yaz.
- Çoklu client için thread/multiplexing tasarla.
