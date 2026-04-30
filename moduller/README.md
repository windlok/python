# moduller — Standart kütüphane ile çalışmak (import pratikleri)

Bu klasör, Python'un hazır modüllerini nasıl import edip kullanacağını gösterir.
Gerçek hayatta çoğu işi sıfırdan yazmak yerine standart kütüphaneyi kullanırsın.

## Nasıl çalıştırılır?

```bash
python moduller/math.py
python moduller/random.py
```

> Not: `random.py` dosya adı, standart kütüphanedeki `random` modülü ile aynı. Bu, import tarafında kafa karıştırabilir (aşağıdaki nota bak).

## `math.py` — Matematik fonksiyonları

Gösterilen import stilleri:

- `import math as islem` (modülü alias ile çağırma)
- `from math import factorial, sqrt` (sadece ihtiyacın olanı alma)
- `from math import *` (her şeyi içe aktarır; öğrenmede görülür ama gerçek projede önerilmez)

Örnek kullanım:

- `factorial(3)`
- `islem.sqrt(49)`

## `random.py` — Rastgelelik araçları

Bu dosya `dir(random)` ve `help(random)` çıktısını basar.

- `dir`: modülde neler var?
- `help`: docstring + kullanım bilgisi (çıktısı uzun olabilir)

### Önemli isim çakışması notu

`moduller/random.py` dosyasını çalıştırırken içeride `import random` yazdığı için, Python bazen standart kütüphanedeki `random` yerine bu dosyayı import etmeye çalışabilir.
Bu durumda doğru çözüm:

- Dosya adını `random_demo.py` gibi değiştirmek, veya
- Import edilen modül adını çakışmayacak şekilde tasarlamak.

Bu, Python'da çok sık görülen bir başlangıç hatasıdır ve bu klasör bunu fark etmene yardımcı olur.

## Alıştırmalar

- `random.randint(1, 6)` ile zar atma simülasyonu yap.
- `math` ile dairenin alanını hesaplayan fonksiyon yaz.
- `from ... import *` yerine seçici import kullanmayı alışkanlık haline getir.
