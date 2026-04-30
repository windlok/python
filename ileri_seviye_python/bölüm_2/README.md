# bölüm_2 — Koşullar + List Comprehension

Bu bölüm iki şeyi yan yana gösterir:

- Klasik `for` + `if` ile filtreleme/dönüştürme
- Aynı işi daha kısa yazan list comprehension

Amaç “kısa yazmak” değil; **aynı problemi iki farklı yaklaşım ile görüp** list comprehension'ın nerede güçlü olduğunu anlamaktır.

## Çalıştırma

```bash
python "ileri_seviye_python/bölüm_2/kosul.py"
python "ileri_seviye_python/bölüm_2/list_comp.py"
```

## Dosya dosya

### `kosul.py`

Bu dosya aynı fikri birkaç farklı örnekle tekrar eder:

1) `1..10` arası çift sayıları yazdırma

- Döngü + `if` ile `print(i)`
- Aynı işi comprehension ile: `[i for i in range(1,11) if i % 2 == 0]`

2) Bir listeyi filtrelemek: `sayilar` -> `cift_sayilar`

- `append` ile doldurma vs comprehension.

3) Comprehension içinde `if/else` (ternary)

- `[i if i % 2 == 0 else "Tek" for i in range(1,11)]`

Burada liste elemanı bazen `int`, bazen `str` olur. Bu bilerek yapılmış bir örnek: “tek satırda etiket üretme” mantığını gösterir.

4) Eşik (threshold) uygulamak / “clamp”

- `urunfiyatlari` üzerinden iki yaklaşım:
	- Döngüde: `0.3` üstü için "vergiler yüksek" yazısı
	- Comprehension ile: `0.3` altını `0.3`'e çekme (`0.3 if vergi < 0.3 else vergi`)

Ek not:

- `vergiler_lc1` sadece `0.3` altı olanlar için `0.3` üretir (liste uzunluğu filtreye göre değişir).

### `list_comp.py`

- `0..9` karelerini önce döngüyle, sonra list comprehension ile üretir.
- `kurum = "SkyLog"` string'ini harf harf gezip `upper()` ile büyütür.

## Ne zaman list comprehension kullanmalı?

- Tek satırda okunabilen dönüştürme/filtreleme varsa.
- Yan etki (dosya yazma, ekrana basma, DB işlemi) gerekiyorsa klasik döngü daha temizdir.

## Alıştırmalar

- `kosul.py` içindeki “çift sayıları bulma” işini fonksiyonlaştır: `even_numbers(start, end)`.
- `vergiler` örneğinde, string yerine vergi oranı hesapla (örn. `0.18` veya `0.08`).
- `list_comp.py` örneğini generator expression ile yazıp farkı gözlemle: `(i**2 for i in range(10))`.
