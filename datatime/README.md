# datatime — `datetime` ile tarih/saat işlemleri

Bu klasörün amacı: tarih-saat bilgisini string olarak değil, üzerinde hesap yapılabilen bir veri tipi olarak kullanmayı öğrenmek.

## Nasıl çalıştırılır?

```bash
python datatime/date.py
```

## `date.py` ne anlatıyor?

Dosyada `datetime` sınıfı üzerinden şu adımlar görülür:

### 1) `datetime.now()` ile “şu an”

- `now = datetime.now()`; yıl/ay/gün/saat bilgisi olan bir nesne döner.
- `datetime.ctime(now)` ile insan okunur tarih formatı alınır.

### 2) `strftime` ile formatlama

`datetime.strftime(now, "%y")` gibi format kodları ile tarih-saat string'e çevrilir.

Örnek format kodları:

- `%Y` : 2026 gibi 4 haneli yıl
- `%y` : 26 gibi 2 haneli yıl
- `%X` : saat:dakika:saniye
- `%a` : günün kısa adı (lokale bağlı)

### 3) `strptime` ile string -> datetime

`datetime.strptime(t, "%d %B %Y hour %H:%M:%S")`

- Bu, log/CSV gibi metinlerden tarih parse etmenin temelidir.
- Format şablonu ile metin birebir uyuşmalı.

### 4) Timestamp dönüşümü

- `datetime.timestamp(birthday)` -> 1970-01-01'den itibaren saniye sayısı
- `datetime.fromtimestamp(ts)` -> tekrar datetime nesnesi

### 5) `timedelta` ile tarih aritmetiği

`simdi - timedelta(days=7)` gibi işlemlerle “7 gün önce” hesaplanır.

## Sık karşılaşılan hatalar

- `strptime` formatı ile metin uyuşmazsa `ValueError` alırsın.
- Tarihleri karşılaştırırken string değil `datetime` nesnesi karşılaştır.

## Alıştırmalar

- Kullanıcıdan iki tarih alıp (`input`), aradaki gün farkını hesapla.
- “Bugüne kaç gün kaldı?” tarzı bir sayaç yap (örn. sınav tarihi).
- `strftime` ile dosya adı üret: `backup_2026-04-30.txt`
