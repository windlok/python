# hata_yönetimi — try/except/finally ve bilinçli hata üretme

Bu klasörün hedefi: program hata aldığında “çat diye kapanmasın”, kontrollü davransın.

## Nasıl çalıştırılır?

```bash
python hata_yönetimi/hata.py
python hata_yönetimi/raise.py
```

## Temel fikir

- `try`: riskli kod
- `except`: hata olursa ne yapacağın
- `else`: hata yoksa çalışacak bölüm
- `finally`: her durumda çalışacak bölüm (dosya kapatma, bağlantı kapatma gibi)

## Dosya dosya

### `hata.py` — Hata yakalama kalıpları

Dosyada farklı örnekler var; çoğu yorum satırı.
Aktif olan kısım:

- Sonsuz döngü (`while True`) içinde kullanıcıdan iki sayı alır.
- `int()` dönüşümü veya `a/b` işlemi hata verirse `except Exception as hata` ile yakalar.
- Hata yoksa `else` bloğunda sonucu yazar ve `break` ile çıkar.
- Her tur `finally` çalışır: “islem tamamlandi”.

Öğrendirdikleri:

- Hata olduğunda yeniden deneme döngüsü kurmak
- `finally` ile temizlik

Alıştırma:

- `ZeroDivisionError` için özel mesaj göster, diğer hataları ayrı yakala.
- Kullanıcı `q` yazarsa programdan çık.

### `raise.py` — Kural koymak ve `raise`

- `check_password(psw)` fonksiyonu parola kuralları kontrol eder.
- Kural bozulursa `raise Exception("...")` ile hata üretir.
- Dışarıda `try/except` ile mesajı yakalayıp kullanıcıya basar.

Kullanılan teknik:

- `re.search('[a-z]', psw)` ile regex kontrolü (küçük harf var mı?)

Alıştırma:

- Büyük harf, sayı ve özel karakter kontrolü ekle.
- `Exception` yerine özel bir hata sınıfı tanımla (`class PasswordError(Exception): ...`).
