# class — Nesne Yönelimli Programlama (OOP)

Bu klasör, Python'da sınıf/nesne mantığını 3 küçük dosya ile öğretir:

- Bir sınıf nasıl tanımlanır?
- Nesne (instance) nasıl üretilir ve kullanılır?
- Kalıtım (inheritance) ile davranış nasıl paylaşılır?
- `__str__`, `__len__` gibi özel metotlarla sınıf “Python gibi” nasıl davranır?

## Nasıl çalıştırılır?

Proje kökünden:
```bash
python class/class.py
python class/inheritance.py
python class/specials.py
```

## Dosya dosya

### 1) `class.py` — `Person` ve `Circle`

Bu dosya iki temel örnek içerir.

#### `Person` sınıfı

- `address` bir *class attribute* (tüm instance'lar için ortak).
- `name` ve `year` *object attribute* (her nesnenin kendi değeri).
- `__init__` yapıcı metot: nesne üretilirken çalışır.
- `intro()` instance metodu: nesnenin kendi verisini kullanır.
- `calculateAge(currentYear)` metodu: verilen yıla göre yaş hesaplar.

Çıktı tarafında `init calisti` mesajını iki kez görmen normal: iki farklı kişi nesnesi oluşturuluyor.

#### `Circle` sınıfı

- `pi` class attribute.
- `yaricap` (radius) parametresi default olarak 1.
- `cevre_hesap()` ve `alan_hesaplama()` ile formüller uygulanıyor.

> Mini not: `pi` değerini class attribute yapmak, tüm dairelerde ortak bir sabit kullanma fikrini anlatır.

**Alıştırmalar**

- `Person` içine `__str__` ekleyip `print(p1)` çıktısını anlamlı hale getir.
- `Circle` içine `cap()` metodu ekle (diameter).
- `calculateAge` fonksiyonunda `currentYear` verilmezse `datetime.now().year` kullan.

### 2) `inheritance.py` — Kalıtım

- `Animals` temel sınıfı `name` ve `type` alıyor.
- `Dogs(Animals)` alt sınıfı, üst sınıfın `__init__` metodunu çağırıyor (`Animals.__init__(...)`).
- `angre()` metodu hem üstte hem altta kullanılabiliyor (miras).

Bu örnek, “aynı metodu alt sınıf da kullanabilir” fikrini oturtmak için minimal tutulmuş.

**Alıştırmalar**

- `Dogs` içine `bark()` metodu ekle.
- `Animals` içine `sleep()` ekle ve `Dogs` sınıfında override et.

### 3) `specials.py` — Özel (dunder) metotlar

`movies` sınıfı ile:

- `__str__`: `str(obj)` ve `print(obj)` davranışını belirler.
- `__len__`: `len(obj)` çağrısını yönetir.
- `__del__`: nesne silinirken çalışan metot (her zaman kesin sırada çalışmayabilir).

Bu tarz metotlar, sınıfları Python'un yerleşik davranışına entegre eder.

**Alıştırmalar**

- `__repr__` ekleyip debug çıktısını iyileştir.
- `duraction` alan adını `duration` olarak düzeltip tüm kullanımları güncelle (refactor pratiği).
