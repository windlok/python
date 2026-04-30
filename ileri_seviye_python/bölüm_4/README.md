# bölüm_4 — Classmethod, property, metaclass

Bu bölüm, sınıfların sadece `__init__` + metotlardan ibaret olmadığını gösterir:

- Alternatif constructor: `@classmethod`
- Kontrollü attribute erişimi: `@property` ve setter
- Sınıf yaratım anını yakalamak: metaclass

## Çalıştırma

```bash
python "ileri_seviye_python/bölüm_4/claas_method.py"
python "ileri_seviye_python/bölüm_4/propertıes.py"
python "ileri_seviye_python/bölüm_4/meta_class.py"
```

## Dosya dosya

### `claas_method.py` — `@classmethod` ile alternatif kurucu

- `CartItem(name, price)` normal kurucu
- `CartItem.from_string("Phone,800")` string parse edip instance üretir
- `cls` parametresi class'ın kendisidir; `return cls(...)` ile o sınıftan nesne döndürür.

Nerede işe yarar?

- CSV satırı, env var, config string gibi yerlerden model üretmek.

Alıştırma:

- Parayı da parse et: `"Phone,800,TRY"` gibi.
- String formatı bozuksa `ValueError` yakalayıp kullanıcıya mesaj ver.

### `propertıes.py` — `@property` + setter ile validasyon

- `Product.price` property olarak tanımlanmış.
- Asıl değer `_price` içinde saklanıyor (enkapsülasyon).
- Setter negatif fiyatı engelliyor ve `ValueError` fırlatıyor.

Alıştırma:

- `name` için de boş string kontrolü ekle.
- Fiyat değişince “eski -> yeni” log bas.

### `meta_class.py` — Metaclass kavramına giriş

- `Meta(type)` sınıfı, sınıf oluşturulurken çağrılır.
- `__init__(class_name, bases, attrs)` içinde `attrs` (sınıfın attribute/metotları) görülür ve ekrana basılır.
- `Person(metaclass=Meta)` ile metaclass devreye girer.

Önemli not:

- Python'da metaclass ile “class yaratımı” genelde `__new__` ile yönetilir; `__init__` içinde `return ...` yapmak doğru değildir ve çalıştırınca hata görebilirsin.
- Bu dosya, “metaclass imzası ve attrs nedir?” fikrini göstermek için minimal tutulmuş.

Alıştırma:

- Meta sınıfını `__new__` ile yeniden yazıp `age` attribute'u yoksa otomatik ekle.
- `attrs` içine otomatik bir `created_at` alanı eklemeyi dene.
