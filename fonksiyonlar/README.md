# fonksiyonlar — Fonksiyonlar, kapsam (scope) ve pratik araçlar

Bu klasör, Python'da fonksiyon yazmayı “sadece def yazmak” seviyesinden çıkarıp şu pratiklerle pekiştirir:

- Parametre çeşitleri (`*args`, `**kwargs`)
- Değişken kapsamı (global/local)
- `lambda`, `map`, `filter`
- List/dict comprehension
- `zip`, `enumerate`

## Nasıl çalıştırılır?

Örnek:
```bash
python fonksiyonlar/fonksiyon.py
python fonksiyonlar/global_local.py
```

## Dosya dosya

### `fonksiyon.py` — Parametre tipleri ve fonksiyon tasarımı

Öne çıkanlar:

- Basit `toplam(a, b)` fonksiyonu
- `*args` örneği: birden çok kişi ismini tek fonksiyonda gezmek
- Docstring kullanımı (`help(kisiler)` ile okunabilir)
- Listeyi fonksiyona gönderirken kopya (`n[:]`) vs referans farkı
- `**kwargs` ile sözlük parametreleri
- `myFunc(a, b, *c, **d)` ile hepsinin bir arada kullanımı

Alıştırma:

- `*args` ile gelen sayıları toplayan `sum_all(*nums)` yaz.
- `**kwargs` ile gelen ayarları doğrulayan bir fonksiyon yaz.

### `global_local.py` — Scope (kapsam)

- Aynı isimli değişkenin fonksiyon içinde “local”, dışarıda “global” olması.
- `global` anahtar kelimesi ile global değişkeni değiştirme.

Alıştırma:

- Global sayaç yap (arttır/azalt), sonra bunu fonksiyon içinde yönet.

### `lambda.py` — `map` / `filter` ile pratik

- `map(lambda ...)` ile her elemanı dönüştürme (kare alma)
- `filter(check_even, numbers)` ile şartı sağlayanları seçme

Not:

- `lambda` her zaman okunabilirlik için iyi olmayabilir; kısa ve net yerde kullan.

### `dongu_metotlar.py` — `zip` ve `enumerate`

- `zip(list1, list2)` ile iki listeyi eşleştirir.
- Döngüde `item1, item2` unpack eder.

Alıştırma:

- 3 listeyi zip'le (isim/yaş/şehir) ve her satırı formatla.

### `liste.py` — List comprehension

- Yıllardan yaş hesaplama (`2026 - year`)
- `if/else` ile comprehension içinde etiket üretme
- İç içe döngü ile koordinat listesi üretme

Alıştırma:

- Sadece asal sayıları üreten bir comprehension dene (zorlu).

### `list.py` — Sözlük metotları (`items()`)

- `dict.items()` ile `(key, value)` çiftlerine dönüşüm.
- Döngüde `for key, value in kullanici.items()` desenini öğretir.

> İsim notu: Dosya adı `list.py` Python'daki `list` tipinin adıyla çakışır. Gerçek projelerde bu tür isimlerden kaçınmak iyi alışkanlıktır.

### `sum_min.py` — Hazır fonksiyonlar

- `sum`, `max`, `min`, `len`, `abs`, `round` örnekleri.

Alıştırma:

- Liste içindeki sayıları normalize et (0-1 aralığına çek).
