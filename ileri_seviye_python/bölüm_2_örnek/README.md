# bölüm_2_örnek — List Comprehension alıştırmaları

Bu klasör, `bölüm_2`'deki list comprehension mantığını daha “gerçek veri” üzerinde uygular.

## Çalıştırma

```bash
python "ileri_seviye_python/bölüm_2_örnek/ornek.py"
python "ileri_seviye_python/bölüm_2_örnek/ornek2.py"
```

## `ornek.py` — 5 mini görev

Bu dosyada list comprehension ile 5 farklı pratik var:

1) `1..99` arasında hem 4'e hem 3'e bölünenler

- `[j for j in range(1,100) if j % 4 == 0 if j % 3 == 0]`
- Not: Bu koşullar tek `if` içinde de yazılabilir: `if j % 12 == 0`

2) Metinden rakamları çekmek

- `text` içindeki karakterleri `isdigit()` ile kontrol eder.
- Sonuç: `['1','2','3','4','5']` gibi bir liste.

3) Sıcaklık listesinde negatifleri etiketlemek

- `i if i>=0 else "buzlanma tehlikesi"`

Bu, list comprehension içinde “değer üretme” (transform) + “etiketleme” fikrini gösterir.

4) İki listeyi indeksle eşleyip dict üretmek

- Önce `(ogrenci, not)` tuple listesi üretilir.
- Sonra dict comprehension ile notu `<= 60` olanlar seçilir.

5) İç içe döngü ile kombinasyon üretimi

- `(x,y,z)` tuple'ları ile tüm kombinasyonlar üretilir.

## `ornek2.py` — Dict listesi üzerinde filtre + hesap

Veri: `ilanlar` listesi (ürün, fiyat, hasarlı mı?)

- `saglam`: hasarlı olmayan ürün isimleri
- `cift`: hasarlı olmayan + fiyatı `<= 20000` olanlar
- `kar`: `(urun, fiyat * 0.2)` tuple listesi (örnek kar marjı hesabı)

Bu dosya, birden fazla koşulun (`if`) art arda kullanılabileceğini ve sadece alan seçmekle kalmayıp yeni değer hesaplanabileceğini gösterir.

## Alıştırmalar

- `ilanlar` içinde hasarlı ürünlerin toplam fiyatını hesapla.
- `kar` listesini kara göre büyükten küçüğe sırala.
- Aynı işleri `filter` + `map` ile (bölüm_3) yazıp karşılaştır.
