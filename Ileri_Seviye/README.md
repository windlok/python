# Ileri_Seviye — Decorator, closure ve fonksiyon tasarımı

Bu klasörde “fonksiyonlar da birer nesnedir” fikrini görüyorsun:

- Fonksiyonu parametre olarak verme
- Fonksiyondan fonksiyon döndürme (closure)
- Bir fonksiyonu başka fonksiyonla sarmalama (decorator)

## Nasıl çalıştırılır?

```bash
python Ileri_Seviye/params.py
python Ileri_Seviye/returning.py
python Ileri_Seviye/decorator.py
```

## Dosya dosya

### `params.py` — İşlem seçimi (fonksiyonları kullanma)

- `toplam`, `carpma`, `bolme`, `cikarma` gibi küçük fonksiyonlar tanımlar.
- `islem(..., islem)` parametresiyle hangi işlemin yapılacağını seçer ve sonucu basar.

Bu dosya “çok basit bir dispatcher” örneğidir.

Alıştırma:

- String yerine fonksiyonun kendisini parametre olarak ver: `islem(a, b, func=toplam)` gibi.
- Bölmede 0'a bölmeyi `try/except` ile yakala.

### `returning.py` — Fonksiyondan fonksiyon döndürme (closure)

İki örnek var:

1) `usalma(number)` -> `inner_power(power)`

- `usalma(2)` dediğinde geriye “2'nin kuvvetini alan fonksiyon” döner.
- `iki_kuvvet(3)` -> 8, `iki_kuvvet(4)` -> 16

2) `yetki_sorgula(page)` -> `inner(user)`

- `page` değişkenini closure içinde saklar.
- `user == "admin"` kontrolüne göre farklı mesaj döndürür.

Öğrendirdikleri:

- İç fonksiyon dış değişkeni “hatırlar”.

Alıştırma:

- `yetki_sorgula` içine allowed_users listesi ekle.
- `usalma` için negatif kuvvet desteği ekle.

### `decorator.py` — Decorator mantığı

- `my_decorator(func)` fonksiyonu, `func`'ı `wrapper()` ile sarar.
- `@my_decorator` ile `say_hello` fonksiyonu dekoratörle kaplanır.

Not:

- Dosyada `say_hello()` çağrısı yok; bu yüzden çalıştırınca çıktı görmeyebilirsin. Çağırmayı eklemek iyi bir pratik.

Alıştırma:

- `wrapper(*args, **kwargs)` yazıp dekoratörü genel hale getir.
- `functools.wraps` ile orijinal fonksiyon adını/docstring'ini koru.
