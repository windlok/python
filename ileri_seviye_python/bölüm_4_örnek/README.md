# bölüm_4_örnek — ShoppingCart sınıf pratiği

Bu klasör, `bölüm_4`'te gördüğün sınıf kavramlarını basit bir “sepet” örneğinde pekiştirir.
Gerçek bir e-ticaret sepeti değil; sınıf tasarımı, liste yönetimi ve `copy()` gibi konuları pratik etmek için bir iskelet.

## Çalıştırma

```bash
python "ileri_seviye_python/bölüm_4_örnek/shopping_cart.py"
```

## `shopping_cart.py` ne yapıyor?

Dosyada iki ayrı sınıf var (aynı fikrin iki yaklaşımı gibi düşünebilirsin):

### 1) `ShoppingCart`

- `self.item` listesi: sepetteki öğeler
- `add_item(veri)`: gelen veriyi listeye ekler
- `calculator_totals()`: kaç öğe var yazdırır (`len(self.item)`)
- `display_items()`: sepetteki her öğeyi basar

Örnek kullanımda sepete “liste” tipinde veriler ekleniyor (`veri`, `veri1`). Bu da “list içine list” durumunu görmeyi sağlar.

### 2) `ShoppingCart1`

- Başlangıç listesi dışarıdan verilir (`file` parametresi)
- `file.copy()` ile referans paylaşımını önler
- `add_items` ile yeni öğe ekler, `display_items` ile gösterir.

## Öğrenilecek noktalar

- Sınıf içinde liste tutma ve metotlarla yönetme
- Referans/kopya farkı (`copy()`)
- Basit raporlama (`len`)

## Alıştırmalar

- `remove_item(index)` metodu ekle.
- Nested list'leri tek listeye indir (flatten).
- Öğeleri dict yap: `{ "name": "Laptop", "price": 1500 }` ve toplam fiyat hesapla.
