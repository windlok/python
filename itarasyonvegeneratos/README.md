# itarasyonvegeneratos — Iterable / Iterator / Generator

Bu klasör “for döngüsünün arkasında ne var?” sorusunu cevaplar:

- Iterable: üzerinde dolaşılabilen şey (liste, string, range…)
- Iterator: `__next__` ile sıradaki elemanı veren nesne
- Generator: `yield` ile değerleri ihtiyaç oldukça üreten özel iterator

## Nasıl çalıştırılır?

```bash
python itarasyonvegeneratos/iterators.py
python itarasyonvegeneratos/generators.py
```

> `generators.py` çok sayıda çıktı üretebilir (500 satır). Terminalde uzun çıktı normal.

## `iterators.py` — Iterator kavramı

1) Liste üzerinde for döngüsü
2) `iter(list)` ile iterator oluşturma
3) `next(iterator)` ile tek tek eleman çekme
4) `StopIteration` yakalayarak while döngüsü ile bitene kadar okuma
5) Kendi iterator sınıfımız:

- `__iter__` -> iterator döndürür
- `__next__` -> sıradaki değeri döndürür, bittiğinde `StopIteration` fırlatır

## `generators.py` — `yield` ve generator

- `cube()` fonksiyonu `yield` kullanarak küpleri üretir.
- Generator bir kez tüketilir: `for` ile dolaştıktan sonra başa dönmez; yeniden üretmek gerekir.

Önemli fark:

- Generator expression: `(i ** 3 for i in range(500))`
- List comprehension: `[i ** 3 for i in range(500)]`

İkisi aynı görünür ama biri **lazy** (tembel), diğeri tüm listeyi RAM'e alır.

## Alıştırmalar

- `myNumbers` iterator'ına `step` parametresi ekle.
- `cube()` yerine “asal sayıları üreten” bir generator yaz.
- Büyük bir range üzerinde list yerine generator kullanarak bellek farkını gözlemle.
