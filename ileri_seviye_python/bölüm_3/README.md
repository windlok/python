# bölüm_3 — Fonksiyonel araçlar: any/all, map/filter, lambda, sorted, min/max, sum/round

Bu bölüm; listeleri döngü ile gezmek yerine, “niyetini” daha net ifade eden hazır fonksiyonları tanıtır.
Hedef: daha kısa yazmak değil; **daha okunur ve daha az hata çıkaran** kalıpları öğrenmek.

## Çalıştırma

```bash
python "ileri_seviye_python/bölüm_3/any_all.py"
python "ileri_seviye_python/bölüm_3/lambda.py"
python "ileri_seviye_python/bölüm_3/map.py"
python "ileri_seviye_python/bölüm_3/filter.py"
python "ileri_seviye_python/bölüm_3/min_max.py"
python "ileri_seviye_python/bölüm_3/som_round.py"
python "ileri_seviye_python/bölüm_3/sorted.py"
```

## Dosya dosya

### `any_all.py` — Toplu doğrulama

- `all([...])`: tüm elemanlar True mu?
- `any([...])`: en az bir eleman True mu?

Generator expression ile kullanım:

- `all(sayi > 4 for sayi in sayilar)`
- `any(sayi > 3 for sayi in sayilar)`

Dosyada bir de isim listesi üzerinde “ilk harfi a mı?” kontrolü var.

> Not: Kodda liste ve döngü değişkeni aynı isimle (`user`) kullanılmış; çalışsa da okunabilirliği düşürür.

### `lambda.py` — Anonim fonksiyon + closure

- Normal fonksiyon: `def kareAl(a): ...`
- Lambda ile tek satır eşdeğeri
- Çok parametreli lambda: `lambda a, b, c: a + b + c`
- Closure örneği: `myFunc(n)` fonksiyonu `lambda a: a * n` döndürür.

### `map.py` — Dönüştürme (transform)

- Döngüyle kare alma vs `map(kareal, sayilar)`
- `map(lambda x: x**2, sayilar)`
- Tip dönüşümü: `map(int, sayilar_Str)`
- Method referansı: `map(str.upper, isimler)`
- Dict listesinde alan çekme: `map(lambda k: k["ad"], kullanicilar)`

> Not: `map(...)` bir iterator döndürür. Yazdırmak için çoğu zaman `list(map_obj)` gerekir. Dosyanın sonunda `print(sonuc4)` çıktısı bunun “tembel” olduğuna örnek.

### `filter.py` — Filtreleme (select)

- Çift sayıları seçme: `filter(lambda x: x % 2 == 0, sayilar)`
- İsmi uzun olanları seçme: `len(x) > 3`
- Sonucu `map(..., ...)` ile birleştirip uppercase yapmak
- Nested veri: kullanıcı listesinde `name == "Ali"` olanı filtreleyip `posts` alanını çekmek

### `min_max.py` — En küçük/en büyük + `key` kullanımı

- Sayı ve string listelerinde `min/max`
- Uzunluklara göre min/max (generator expression)

> Not: Dosyada `min(len(harfler) for harf in harfler)` satırı var; amaç muhtemelen `len(harf)` idi.

Dict listesinde en pahalı ürünü bulma:

- `max(urunler, key=lambda urun: urun["fiyat"])`

### `som_round.py` — Toplam, ortalama ve yuvarlama

- Ortalama: `sum(sayilar) / len(sayilar)`
- `sum(iterable, start)` ile başlangıç değeri kullanma
- `products` içinde fiyatı 0 olanları hariç tutup ortalama fiyat hesaplama
- `round()` örnekleri: `.5` davranışı, basamak sayısı

### `sorted.py` — Sıralama

- `.sort()` listeyi yerinde değiştirir; `sorted()` yeni liste döndürür.
- `reverse=True` ile tersten sıralama

Dict listesinde sıralama:

- Deneme amaçlı bir sıralama: `sorted(users, key=len, ...)` (dict uzunluğu = key sayısı)
- Doğru yaklaşım: `key=lambda user: len(user["posts "])`

Sıralayıp sadece `username` almak:

- `map(lambda user: user["username"], sorted(...))`

> Not: Örnek `users` dict'lerinde `"posts "` anahtarının sonunda boşluk var. Bu yüzden kod `user["posts "]` kullanıyor.

## Alıştırmalar

- `filter` ile seçip `map` ile dönüştürdüğün bir pipeline yaz (örn. fiyatı 0 olmayan ürünleri %10 zamlı listele).
- `sorted` ile “en çok post atan kullanıcıyı” bul.
- `any/all` ile “tüm email'ler @ içeriyor mu?” kontrolü yaz.
