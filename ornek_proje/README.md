# ornek_proje — Mini proje senaryoları (sınıf + akış)

Buradaki dosyalar, “tek satır örnek” yerine küçük bir senaryoyu uçtan uca kurmaya çalışır.
Amaç:

- Sınıf tasarlamak
- Veriyi bir yerde tutmak (liste/sözlük)
- Kurallar koymak (validasyon)
- Küçük bir rapor/çıktı üretmek

## Nasıl çalıştırılır?

Dosya adlarında Türkçe karakterler olduğu için tırnak kullanmak güvenli:
```bash
python ornek_proje/Envanter_Sistemi.py
python "ornek_proje/LoadCell_Veri_İsleme_Sınıfı.py"
python "ornek_proje/Otonom_Kargo_Ucus_Kontrol_Sistemi.py"
python ornek_proje/Sensor_Verisi_Filtreleme.py
python "ornek_proje/SkyLog_Otonom_Drone_Filo_Yönetimi.py"
```

## Dosya dosya

### `Envanter_Sistemi.py` — Envanter + kritik stok raporu

Sınıflar:

- `Parca`: isim/kategori/stok ve arızalı adet yönetimi (`ariza_bildir`)
- `Laboratuvar`: envanter listesi, parça kaydetme, kritik stok raporu

Senaryo:

- Parçalar oluşturulur, bazıları arızalıya düşürülür.
- Envantere eklenir.
- Kritik stok eşiği (`<= 3`) raporlanır.

Alıştırma:

- Kritik stok eşiğini parametre yap.
- `Parca` içine “stok ekle” metodu ekle.

### `LoadCell_Veri_İsleme_Sınıfı.py` — Sensör verisi temizleme + kalibrasyon

Sınıf:

- `Sensor`: ham verileri toplar, kalibrasyon çarpanı uygular.

Adımlar:

1) Rastgele ham veri üretme
2) `veri_ekleme` ile listeye alma
3) `veri_temizleme(altlimit, ustlimit)` ile filtreleme
4) Filtrelenen verilerin ortalamasını alıp kalibrasyonla çarpma

Öğrendirdikleri:

- Liste toplama
- Filtreleme
- Ortalama hesaplama (mean)

Alıştırma:

- Filtreleme sonrası `min/max` değerleri de raporla.
- Kalibrasyon çarpanını dosyadan oku.

### `Sensor_Verisi_Filtreleme.py` — Döngü ile filtreleme ve rapor

- 12 adet rastgele sensör değeri üretir.
- 0..200 aralığında olanları “temiz” kabul eder.
- Sonunda rapor basar: elenen sayısı, sıralama, min/max/ortalama.

Alıştırma:

- Aralıkları (0..200) parametre yap.
- “median” (ortanca) hesapla.

### `Otonom_Kargo_Ucus_Kontrol_Sistemi.py` — Uçuş onayı

- Kullanıcıdan mesafe ve kargo kilosu alır.
- Maksimum kilo ve menzil kuralına göre uçuşu onaylar/reddeder.
- Onaylanırsa süre hesabı yapar: `yol = (mesafe/hiz)*60`

Alıştırma:

- Gidiş-dönüş (mesafe*2) için süreyi ayrı yazdır.
- `global` kullanmadan fonksiyon sonucu döndür.

### `SkyLog_Otonom_Drone_Filo_Yönetimi.py` — Drone + filo yönetimi

Sınıflar:

- `Drone`: batarya, durum, kapasite ve uçuş aksiyonu
- `Filo`: birden fazla drone tutar, uygun drone seçer, rapor basar

Görülen iş kuralları:

- Uçuş için batarya ve kapasite şartı
- Filoda “uygun drone bul” mantığı (batarya >= 60, durum beklemede, kapasite yeterli)

Alıştırma:

- Uçuş sonrası drone'u tekrar `beklemede` yapacak bir “iniş” metodu ekle.
- Filoda birden fazla kargo talebini sıraya al (queue).
