# ============================================================
#               PYTHON HAP BİLGİLER & KISAYOLLAR
# ============================================================


# ------------------------------------------------------------
# 1. ENUMERATE - index + değer aynı anda
# ------------------------------------------------------------
isimler = ["Ali", "Veli", "Ayşe"]
for i in range(len(isimler)):
    print(i, isimler[i])  # Normal yol (kötü)

for i, isim in enumerate(isimler):
    print(i, isim)  # 0 Ali, 1 Veli, 2 Ayşe

# start ile 1'den başlat
for i, isim in enumerate(isimler, start=1):
    print(f"{i}. {isim}")  # 1. Ali, 2. Veli, 3. Ayşe


# ------------------------------------------------------------
# 2. ZIP - birden fazla listeyi eş zamanlı gez
# ------------------------------------------------------------
isimler = ["Ali", "Veli", "Ayşe"]
yaslar  = [20, 25, 30]
sehirler = ["İstanbul", "Ankara", "İzmir"]

for isim, yas in zip(isimler, yaslar):
    print(f"{isim} - {yas} yaşında")

for isim, yas, sehir in zip(isimler, yaslar, sehirler):
    print(f"{isim} - {yas} - {sehir}")

# İki listeyi birleştirip dict yap
sozluk = dict(zip(isimler, yaslar))
print(sozluk)  # {'Ali': 20, 'Veli': 25, 'Ayşe': 30}

# Kısa liste bitince durur - zip_longest ile çöz
from itertools import zip_longest
a = [1, 2, 3]
b = [10, 20]
print(list(zip_longest(a, b, fillvalue=0)))  # [(1,10),(2,20),(3,0)]


# ------------------------------------------------------------
# 3. LIST COMPREHENSION
# ------------------------------------------------------------
# Normal yol
kareler = []
for x in range(10):
    kareler.append(x**2)

# Comprehension: [işlem for eleman in iterable if koşul]
kareler = [x**2 for x in range(10)]
ciftler = [x for x in range(20) if x % 2 == 0]

# İf-else ile
etiket = ["çift" if x % 2 == 0 else "tek" for x in range(5)]

# İç içe (nested)
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
duzlestir = [sayi for satir in matris for sayi in satir]


# ------------------------------------------------------------
# 4. DICT COMPREHENSION
# ------------------------------------------------------------
kareler = {x: x**2 for x in range(5)}
filtreli = {x: x**2 for x in range(10) if x**2 > 20}

# İki listeyi dict yap
urunler  = ["elma", "armut", "kiraz"]
fiyatlar = [5, 8, 15]
urun_dict = {urun: fiyat for urun, fiyat in zip(urunler, fiyatlar)}

# Dict'i tersine çevir (keyvalue)
ters = {v: k for k, v in urun_dict.items()}


# ------------------------------------------------------------
# 5. TERNARY - tek satır if-else
# ------------------------------------------------------------
yas = 20
durum = "yetişkin" if yas >= 18 else "çocuk"

# İç içe ternary
seviye = "uzman" if yas > 40 else ("orta" if yas > 20 else "yeni")

# Liste içinde
puanlar = [45, 60, 30, 80]
sonuclar = ["geçti" if p >= 50 else "kaldı" for p in puanlar]


# ------------------------------------------------------------
# 6. WALRUS OPERATÖRÜ := (Python 3.8+)
# Değer atama ve kullanma aynı anda
# ------------------------------------------------------------
data = [1, 2, 3, 4, 5]

# Normal yol: 2 satır
n = len(data)
if n > 3:
    print(f"Liste çok uzun: {n} eleman")

# Walrus: 1 satır
if (n := len(data)) > 3:
    print(f"Liste çok uzun: {n} eleman")

# While içinde kullanım
# while (satir := f.readline()):
#     process(satir)


# ------------------------------------------------------------
# 7. F-STRING - güçlü string formatlama
# ------------------------------------------------------------
isim = "Ali"
yas = 25
para = 1234567.89

print(f"Merhaba {isim}")
print(f"10 yıl sonra: {yas + 10}")          # İfade yazılabilir
print(f"Büyük harf: {isim.upper()}")         # Metod çağrılabilir
print(f"{para:.2f}")                          # 1234567.89  (2 ondalık)
print(f"{para:,.2f}")                         # 1,234,567.89 (binlik ayraç)
print(f"{0.1234:.2%}")                        # 12.34%
print(f"{yas:05d}")                           # 00025 (sıfır dolgu)
print(f"{255:08b}")                           # 11111111 (binary)
print(f"{255:#x}")                            # 0xff (hex)
print(f"{'sol':<20}|")                        # Sol hizala
print(f"{'sag':>20}|")                        # Sağ hizala
print(f"{'orta':^20}|")                       # Ortala
print(f"{'dolu':*^20}|")                      # * ile doldur
print(f"{yas=}")                              # yas=25 (debug modu, 3.8+)


# ------------------------------------------------------------
# 8. JOIN - listeyi stringe çevir
# ------------------------------------------------------------
kelimeler = ["Python", "cok", "guzel"]
print(" ".join(kelimeler))    # Python cok guzel
print("-".join(kelimeler))    # Python-cok-guzel
print(", ".join(kelimeler))   # Python, cok, guzel
print("".join(kelimeler))     # Pythoncokguzel

# Sayı listesi için önce str() gerekir
sayilar = [1, 2, 3, 4, 5]
print(", ".join(str(s) for s in sayilar))  # 1, 2, 3, 4, 5

# Çoklu boşlukları düzelt
bozuk = "  Python   cok    guzel  "
duzgun = " ".join(bozuk.split())  # "Python cok guzel"


# ------------------------------------------------------------
# 9. DICT METODLARI
# ------------------------------------------------------------
urun = {"isim": "Samsung", "fiyat": 5000}

# .get() - KeyError almadan
print(urun.get("renk", "Bilinmiyor"))  # Bilinmiyor
print(urun.get("fiyat", 0))            # 5000

# .setdefault() - yoksa ekle, varsa dokunma
urun.setdefault("stok", 100)   # stok yoktu, ekledi
urun.setdefault("fiyat", 0)    # fiyat vardı, değiştirmedi

# .update() - güncelle veya ekle
urun.update({"renk": "Mavi", "fiyat": 4500})

# .pop() - sil ve döndür
fiyat = urun.pop("fiyat", 0)

# .items(), .keys(), .values()
for k, v in urun.items():  print(f"{k}: {v}")

# Dict birleştirme (Python 3.9+)
a = {"x": 1}
b = {"y": 2}
c = a | b      # {'x': 1, 'y': 2}


# ------------------------------------------------------------
# 10. UNPACKING - esnek değer atama
# ------------------------------------------------------------
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4, 5]        # first=1, rest=[2,3,4,5]
*baslangic, son = [1, 2, 3, 4, 5]     # baslangic=[1,2,3,4], son=5
ilk, *orta, son = [1, 2, 3, 4, 5]    # ilk=1, orta=[2,3,4], son=5

# Fonksiyon parametrelerinde unpack
def topla(a, b, c): return a + b + c
args = [1, 2, 3]
print(topla(*args))                     # [1,2,3]  pozisyonel

kwargs = {"a": 1, "b": 2, "c": 3}
print(topla(**kwargs))                  # dict  keyword

# Listeleri birleştir
liste1, liste2 = [1, 2, 3], [4, 5, 6]
birlesik = [*liste1, *liste2]           # [1, 2, 3, 4, 5, 6]

# Dict'leri birleştir
d1, d2 = {"a": 1}, {"b": 2}
birlesik_dict = {**d1, **d2}            # {'a': 1, 'b': 2}


# ------------------------------------------------------------
# 11. LAMBDA - isimsiz mini fonksiyon
# ------------------------------------------------------------
kare    = lambda x: x**2
topla   = lambda x, y: x + y
kosullu = lambda x: "cift" if x % 2 == 0 else "tek"

print(kare(5))      # 25
print(topla(3, 4))  # 7

# sorted() + lambda
urunler = [{"isim": "B", "fiyat": 30}, {"isim": "A", "fiyat": 10}]
sirali = sorted(urunler, key=lambda x: x["fiyat"])
# Çoklu kritere göre
sirali2 = sorted(urunler, key=lambda x: (x["fiyat"], x["isim"]))


# ------------------------------------------------------------
# 12. MAP, FILTER, REDUCE
# ------------------------------------------------------------
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: Her elemana fonksiyon uygula
kareler = list(map(lambda x: x**2, sayilar))       # [1,4,9,16...]

# Birden fazla listeyle map
a, b = [1, 2, 3], [10, 20, 30]
toplam = list(map(lambda x, y: x + y, a, b))       # [11, 22, 33]

# filter: Koşulu sağlayanları al
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))  # [2,4,6,8,10]

# reduce: Tek değere indir
from functools import reduce
carpim = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])  # 120
toplam = reduce(lambda x, y: x + y, sayilar)            # 55

# NOT: map/filter yerine comprehension daha Pythonic
kareler2 = [x**2 for x in sayilar]
ciftler2  = [x for x in sayilar if x % 2 == 0]


# ------------------------------------------------------------
# 13. ANY ve ALL - toplu koşul
# ------------------------------------------------------------
sayilar = [2, 4, 6, 7, 8]
print(any(x % 2 != 0 for x in sayilar))  # True  (en az biri tek)
print(any(x > 100 for x in sayilar))     # False (hiçbiri >100)
print(all(x % 2 == 0 for x in sayilar))  # False (7 tek)
print(all(x > 0 for x in sayilar))       # True  (hepsi pozitif)

# Pratik: şifre doğrulama
def sifre_gecerli(s):
    return all([
        len(s) >= 8,
        any(c.isupper() for c in s),
        any(c.isdigit() for c in s),
    ])


# ------------------------------------------------------------
# 14. SORTED, MIN, MAX - gelişmiş
# ------------------------------------------------------------
urunler = [
    {"isim": "Samsung", "fiyat": 5000, "stok": 10},
    {"isim": "Apple",   "fiyat": 8000, "stok": 3},
    {"isim": "Xiaomi",  "fiyat": 3000, "stok": 25},
]
sirali    = sorted(urunler, key=lambda x: x["fiyat"])
tersten   = sorted(urunler, key=lambda x: x["fiyat"], reverse=True)
en_pahali = max(urunler, key=lambda x: x["fiyat"])   # {'isim': 'Apple'...}
en_ucuz   = min(urunler, key=lambda x: x["fiyat"])
coklu     = sorted(urunler, key=lambda x: (x["fiyat"], x["stok"]))


# ------------------------------------------------------------
# 15. SET - kume islemleri
# ------------------------------------------------------------
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a & b)   # Kesisim: {3, 4, 5}
print(a | b)   # Birlesim: {1,2,3,4,5,6,7}
print(a - b)   # Fark: {1, 2}
print(a ^ b)   # Simetrik fark: {1, 2, 6, 7}
print({1, 2} <= a)  # Alt kume mi? True
print(a >= {1, 2})  # Üst kume mi? True

# Tekrarsız liste
liste = [1, 2, 2, 3, 3, 3, 4]
tekrarsiz = list(set(liste))

# Ortak elemanlar
ortak = list(set(liste) & set([2, 3, 5]))


# ------------------------------------------------------------
# 16. COLLECTIONS MODÜLLERİ
# ------------------------------------------------------------
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter - eleman sayma
kelimeler = ["elma", "armut", "elma", "kiraz", "elma", "armut"]
sayac = Counter(kelimeler)
print(sayac.most_common(2))        # [('elma', 3), ('armut', 2)]
print(sayac["elma"])               # 3

# defaultdict - eksik key'e varsayılan deger ver
dd_int  = defaultdict(int)         # Varsayılan: 0
dd_list = defaultdict(list)        # Varsayılan: []
dd_int["a"] += 1                   # KeyError vermez
dd_list["okul"].append("Ali")      # Otomatik [] olusturur

# deque - cift uclu kuyruk
d = deque([1, 2, 3])
d.appendleft(0)   # [0, 1, 2, 3]
d.append(4)       # [0, 1, 2, 3, 4]
d.popleft()       # 0 döner, [1, 2, 3, 4] kalır
d.rotate(1)       # [4, 1, 2, 3] - döndür

# namedtuple - isimli tuple
Nokta = namedtuple("Nokta", ["x", "y"])
p = Nokta(3, 4)
print(p.x, p.y)   # 3 4
print(p[0], p[1]) # 3 4 (index ile de erişilir)


# ------------------------------------------------------------
# 17. ITERTOOLS - guclu iteratör araclari
# ------------------------------------------------------------
import itertools

# chain: birden fazla iterable'ı birlestir
for i in itertools.chain([1, 2], [3, 4], [5]):
    print(i)  # 1 2 3 4 5

# combinations: kombinasyonlar (sira önemli değil)
liste = ["A", "B", "C"]
print(list(itertools.combinations(liste, 2)))
# [('A','B'), ('A','C'), ('B','C')]

# permutations: permütasyonlar (sira önemli)
print(list(itertools.permutations(liste, 2)))
# [('A','B'), ('A','C'), ('B','A')...]

# product: kartezyen carpım
print(list(itertools.product([0, 1], repeat=3)))
# [(0,0,0),(0,0,1)...(1,1,1)] - 8 sonuç

# islice: büyük iterable'dan dilim
gen = (x**2 for x in range(1_000_000))
ilk_5 = list(itertools.islice(gen, 5))  # [0, 1, 4, 9, 16]

# groupby: gruplama (önce sort!)
data = [("Ali", "İst"), ("Veli", "İst"), ("Ayşe", "Ank")]
data.sort(key=lambda x: x[1])
for sehir, grup in itertools.groupby(data, key=lambda x: x[1]):
    print(sehir, list(grup))


# ------------------------------------------------------------
# 18. GENERATOR - bellek verimli üretici
# ------------------------------------------------------------
# Normal fonksiyon: tüm listeyi RAM'e yükler
def kareler_liste(n): return [x**2 for x in range(n)]

# Generator fonksiyon: sadece istendiğinde üretir (yield)
def kareler_gen(n):
    for x in range(n):
        yield x**2

# Generator expression
gen = (x**2 for x in range(1_000_000))  # Hemen RAM kullanmaz

for kare in kareler_gen(5):
    print(kare)  # 0 1 4 9 16

# next() ile manuel ilerleme
g = kareler_gen(3)
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 4
# print(next(g))  # StopIteration!


# ------------------------------------------------------------
# 19. DECORATOR - fonksiyona ek güç kat
# ------------------------------------------------------------
import time, functools

# Temel decorator
def sure_olc(func):
    @functools.wraps(func)  # Orijinal isim/docstring korunur
    def wrapper(*args, **kwargs):
        t = time.time()
        sonuc = func(*args, **kwargs)
        print(f"{func.__name__}  {time.time()-t:.4f} sn")
        return sonuc
    return wrapper

@sure_olc
def agir_islem(n): return sum(range(n))
agir_islem(1_000_000)

# Parametre alan decorator
def tekrarla(kez):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(kez):
                sonuc = func(*args, **kwargs)
            return sonuc
        return wrapper
    return decorator

@tekrarla(kez=3)
def merhaba(): print("Merhaba!")
merhaba()  # 3 kez yazdırır

# lru_cache - önbellekleme
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(50))  # Çok hızlı (önbellekli)


# ------------------------------------------------------------
# 20. CONTEXT MANAGER (with)
# ------------------------------------------------------------
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Merhaba\nDünya\n")

with open("test.txt", "r", encoding="utf-8") as f:
    for satir in f:
        print(satir.strip())

# Kendi context manager
from contextlib import contextmanager

@contextmanager
def zamanlayici(isim):
    print(f"{isim} başladı...")
    t = time.time()
    yield
    print(f"{isim} bitti: {time.time()-t:.4f} sn")

with zamanlayici("Hesaplama"):
    sum(range(1_000_000))


# ------------------------------------------------------------
# 21. DATACLASS - modern sınıf tanımı
# ------------------------------------------------------------
from dataclasses import dataclass, field

@dataclass
class Urun:
    isim: str
    fiyat: float
    stok: int = 0
    etiketler: list = field(default_factory=list)  # Mutable varsayılan

u1 = Urun("Samsung", 5000, 10)
u2 = Urun("Apple", 8000)
print(u1)         # Urun(isim='Samsung', fiyat=5000, ...)
print(u1 == u2)   # False (otomatik == karşılaştırması)

# frozen=True: değiştirilemez
@dataclass(frozen=True)
class Nokta:
    x: float
    y: float

p = Nokta(3.0, 4.0)
# p.x = 5  # HATA!


# ------------------------------------------------------------
# 22. TYPE HINTS - tip ipuçları
# ------------------------------------------------------------
from typing import List, Dict, Optional, Union

def topla(a: int, b: int) -> int: return a + b

def bul(id: int) -> Optional[str]:      # None olabilir
    return {1: "Ali"}.get(id)

def isle(v: Union[int, str]) -> str:     # int veya str
    return str(v)

def ort(sayilar: List[float]) -> float:
    return sum(sayilar) / len(sayilar)

# Python 3.10+: int | str  (Union yerine)
def yeni(v: int | str) -> str: return str(v)


# ------------------------------------------------------------
# 23. EXCEPTION HANDLING - gelismis hata yönetimi
# ------------------------------------------------------------
# Kendi hata sınıfı
class YasHatasi(Exception):
    def __init__(self, yas, mesaj="Geçersiz yaş"):
        self.yas = yas
        super().__init__(f"{mesaj}: {yas}")

def yas_kontrol(yas):
    if yas < 0:   raise YasHatasi(yas, "Negatif olamaz")
    if yas > 150: raise YasHatasi(yas, "Çok büyük")
    return yas

try:
    yas_kontrol(-5)
except YasHatasi as e:
    print(f"Hata: {e}, yaş: {e.yas}")
except (ValueError, TypeError) as e:
    print(f"Tip hatası: {e}")
else:
    print("Başarılı!")   # try hatasız geçerse çalışır
finally:
    print("Her zaman!")  # her durumda çalışır

# Exception chaining
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Dönüşüm başarısız") from e


# ------------------------------------------------------------
# 24. STRING - gelismis metodlar
# ------------------------------------------------------------
metin = "  Merhaba Dünya Python  "

# Temizleme
metin.strip()              # Bas/son boşluk sil
metin.lstrip()             # Sol boşluk sil
metin.rstrip()             # Sag boşluk sil

# Bölme
metin.split()              # ['Merhaba', 'Dünya', 'Python']
metin.split("a")           # 'a' karakterine göre böl
metin.rsplit(" ", 1)       # Sagdan 1 kez böl
"a\nb\nc".splitlines()     # Satırlara böl

# Kontrol
metin.startswith("  M")    # True
metin.strip().endswith("n")# True
"Python" in metin          # True
"12345".isdigit()          # True
"merhaba".isalpha()        # True
"  \n".isspace()           # True

# Arama
s = "Python Python"
s.find("Python")    # 0    (ilk indeks, bulamazsa -1)
s.rfind("Python")   # 7    (sondan ara)
s.count("Python")   # 2
# s.index("Java")   # ValueError!

# Büyük/küçük
"MERHABA".lower()           # merhaba
"merhaba".upper()           # MERHABA
"merhaba dünya".title()     # Merhaba Dünya
"Merhaba".swapcase()        # mERHABA

# Doldurma
"42".zfill(5)               # 00042
"test".ljust(10, "-")       # test------
"test".rjust(10, "-")       # ------test
"test".center(10, "-")      # ---test---


# ------------------------------------------------------------
# 25. LIST SLICE - dilim alma
# ------------------------------------------------------------
liste = [10, 20, 30, 40, 50]
# liste[başlangıç:bitiş:adım]
print(liste[1:3])    # [20, 30]
print(liste[:3])     # [10, 20, 30]
print(liste[2:])     # [30, 40, 50]
print(liste[::2])    # [10, 30, 50]  (her 2 adım)
print(liste[::-1])   # [50, 40, 30, 20, 10]  (ters)
print(liste[-3:])    # [30, 40, 50]  (sondan 3)

# Liste metodları
l = [3, 1, 4, 1, 5, 9]
l.append(7)          # Sona ekle: [3,1,4,1,5,9,7]
l.extend([8, 9])     # Birden fazla ekle
l.insert(0, 0)       # Index 0'a ekle
l.remove(1)          # İlk 1'i sil
l.pop()              # Son elemanı sil ve döndür
l.pop(2)             # İndexteki elemanı sil
l.sort()             # Sirala (yerinde)
l.sort(reverse=True) # Büyükten küçüğe
l.reverse()          # Tersine çevir
l.count(5)           # Kaç tane 5 var?
l.index(9)           # 9 hangi indexte?
l.clear()            # Temizle


# ------------------------------------------------------------
# 26. COPY - sig ve derin kopyalama
# ------------------------------------------------------------
import copy

orijinal = [1, [2, 3], {"a": 4}]

# Sığ kopya: iç içe nesneler PAYLAŞILIR
sig = orijinal.copy()     # veya orijinal[:]
sig[0] = 99               # Orijinali etkilemez
sig[1].append(999)        # Orijinal [2,3,999] olur!

# Derin kopya: tamamen bagımsız
derin = copy.deepcopy(orijinal)
derin[1].append(888)      # Orijinali etkilemez


# ------------------------------------------------------------
# 27. GLOBAL ve NONLOCAL
# ------------------------------------------------------------
sayac = 0

def artir():
    global sayac    # Global değişkeni değiştir
    sayac += 1

def dis():
    x = 10
    def ic():
        nonlocal x  # Dıştaki x'i değiştir
        x += 5
    ic()
    return x   # 15


# ------------------------------------------------------------
# 28. *ARGS ve **KWARGS
# ------------------------------------------------------------
def topla(*args):
    return sum(args)                    # (1,2,3,4,5) = 15

def profil(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")              # isim: Ali, yas: 25

def her_sey(zorunlu, *args, **kwargs):
    print(zorunlu, args, kwargs)

her_sey("x", 1, 2, 3, a=4, b=5)
# x (1, 2, 3) {'a': 4, 'b': 5}


# ------------------------------------------------------------
# 29. CLASS - nesne yönelimli programlama
# ------------------------------------------------------------
class BankaHesabi:
    faiz_orani = 0.05   # Class deg. (tüm instance paylaşır)

    def __init__(self, sahip, bakiye=0):
        self.sahip   = sahip
        self._bakiye = bakiye    # _ = private göstergesi

    @property
    def bakiye(self):            # Getter
        return self._bakiye

    @bakiye.setter
    def bakiye(self, deger):     # Setter
        if deger < 0: raise ValueError("Negatif olamaz!")
        self._bakiye = deger

    def para_yatir(self, miktar):
        self._bakiye += miktar
        return self              # Method chaining için

    def para_cek(self, miktar):
        if miktar > self._bakiye: raise ValueError("Yetersiz!")
        self._bakiye -= miktar
        return self

    def __str__(self):    return f"{self.sahip}: {self._bakiye} TL"
    def __repr__(self):   return f"BankaHesabi('{self.sahip}', {self._bakiye})"
    def __eq__(self, o):  return self._bakiye == o._bakiye
    def __lt__(self, o):  return self._bakiye < o._bakiye

    @classmethod
    def faiz_guncelle(cls, oran): cls.faiz_orani = oran

    @staticmethod
    def gecerli_mi(miktar): return miktar > 0

# Method chaining
h = BankaHesabi("Ali", 1000)
h.para_yatir(500).para_yatir(200).para_cek(100)
print(h)  # Ali: 1600 TL


# ------------------------------------------------------------
# 30. ABC - soyut sinif (arayüz)
# ------------------------------------------------------------
from abc import ABC, abstractmethod

class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self) -> str: pass

    @abstractmethod
    def hareket_et(self) -> str: pass

    def tanitim(self):            # Normal metod
        return f"{self.ses_cikar()} - {self.hareket_et()}"

class Kopek(Hayvan):
    def ses_cikar(self):  return "Hav"
    def hareket_et(self): return "koşuyor"

# h = Hayvan()  # HATA! Soyut sınıf örneklenemez
k = Kopek()
print(k.tanitim())  # Hav - koşuyor


# ------------------------------------------------------------
# 31. PATHLIB - modern dosya yolu işlemleri
# ------------------------------------------------------------
from pathlib import Path

p = Path("C:/Users/User/Desktop/python")
p = Path.home() / "Desktop" / "python"  # / operatörü ile birlestir

print(p.name)        # python          (son kisim)
print(p.stem)        # python          (uzantısız)
print(p.suffix)      # .py             (uzantı)
print(p.parent)      # Desktop         (üst dizin)
print(p.exists())    # True/False
print(p.is_file())   # Dosya mı?
print(p.is_dir())    # Klasör mü?

# Dosya işlemleri
dosya = Path("test.txt")
dosya.write_text("Merhaba", encoding="utf-8")
icerik = dosya.read_text(encoding="utf-8")
dosya.unlink()       # Dosyayı sil

# Klasör listeleme
# for f in p.iterdir(): print(f.name)
# for f in p.glob("**/*.py"): print(f)       # Tüm .py


# ------------------------------------------------------------
# 32. JSON İŞLEMLERİ
# ------------------------------------------------------------
import json

data = {"isim": "Ali", "yas": 25, "hobiler": ["okuma", "spor"]}

# Python  JSON string
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON string  Python
geri = json.loads(json_str)
print(geri["isim"])  # Ali

# Dosyaya yaz
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Dosyadan oku
with open("data.json", "r", encoding="utf-8") as f:
    okunan = json.load(f)


# ------------------------------------------------------------
# 33. SAYI - matematiksel islemler
# ------------------------------------------------------------
import math

print(7 // 2)              # 3     (tam bölme)
print(7 %  2)              # 1     (kalan)
print(2 ** 10)             # 1024  (üs)
print(abs(-5))             # 5     (mutlak değer)
print(divmod(17, 5))       # (3,2) (hem bölüm hem kalan)
print(round(3.14159, 2))   # 3.14
print(math.floor(3.9))     # 3     (asagı yuvarla)
print(math.ceil(3.1))      # 4     (yukarı yuvarla)
print(math.sqrt(144))      # 12.0
print(math.pi)             # 3.14159...
print(math.inf)            # sonsuz
print(1_000_000)           # Büyük sayı okunabilirlik için _


# ------------------------------------------------------------
# 34. ENUMERATE + ZIP BIRLIKTE
# ------------------------------------------------------------
isimler = ["Ali", "Veli", "Ayse"]
puanlar = [85, 92, 78]

for i, (isim, puan) in enumerate(zip(isimler, puanlar), start=1):
    print(f"{i}. {isim}: {puan}")
# 1. Ali: 85
# 2. Veli: 92
# 3. Ayse: 78


# ------------------------------------------------------------
# 35. SORTED + KEY FONKSIYONU
# ------------------------------------------------------------
# min(), max(), sorted() hepsinde key parametresi var
kelimeler = ["merhaba", "dünya", "python", "ai"]

# Uzunluğa göre sırala
print(sorted(kelimeler, key=len))       # ['ai', 'dünya', ...]

# Büyük harfe göre sırala (Türkçe uyumlu)
print(sorted(kelimeler, key=str.lower))

# En uzun kelime
print(max(kelimeler, key=len))          # merhaba
