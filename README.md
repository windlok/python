# Python Öğrenme Notları (Script Arşivi)

Bu repo; Python'u “konu konu” öğrenmek için hazırlanmış küçük, bağımsız örneklerden oluşur.
Buradaki dosyaların çoğu bir kütüphane/paket gibi import edilmek için değil, doğrudan çalıştırılıp çıktı görülerek öğrenmek için yazılmıştır.

## Hızlı Başlangıç

- Python 3.x kurulu olmalı.
- En pratik çalışma şekli: proje kök dizininden çalıştırmak.

Örnek:
```bash
python demo/asal.py
```

Bazı dosyalar `input()` ile kullanıcıdan veri ister. Bu tip dosyalarda VS Code “Run Python File” yerine terminalden çalıştırmak daha sorunsuz olur.

### PyQt5 (arayüz örnekleri için)

Arayüz örnekleri için PyQt5 gerekir:
```bash
pip install PyQt5
```

## Windows'ta çalıştırma ipuçları

- Türkçe karakter veya boşluk içeren dosya adlarını tırnakla çalıştır:
	```bash
	python "ornek_proje/SkyLog_Otonom_Drone_Filo_Yönetimi.py"
	python "qt_ornekleri/Siparis_SkyLog_Yer_Kontrol_İstasyonu.py"
	```
- Dosya okuyan örnekler göreceli yol kullanır (örn. `demo/kullaniciler.txt`). Bu yüzden komutları proje kökünden çalıştırmak güvenlidir.

## Repo Haritası (Ne nerede?)

Aşağıdaki linkler klasör içindeki README dosyalarına gider:

- Hızlı “hap bilgiler” dosyası: `hap_bilgiler.py` (tek dosyada kısa kısa Python pratikleri)
- OOP (sınıf/kalıtım/özel metotlar): [class/README.md](class/README.md)
- Tarih-saat: [datatime/README.md](datatime/README.md)
- Mini alıştırmalar (input'lu örnekler): [demo/README.md](demo/README.md)
- Dosya okuma-yazma: [dosya_islemleri/README.md](dosya_islemleri/README.md)
- Fonksiyonlar, `*args/**kwargs`, scope, lambda: [fonksiyonlar/README.md](fonksiyonlar/README.md)
- Hata yönetimi (`try/except`, `raise`): [hata_yönetimi/README.md](hata_yönetimi/README.md)
- İleri fonksiyon teknikleri (decorator/closure): [Ileri_Seviye/README.md](Ileri_Seviye/README.md)
- Iterator & generator: [itarasyonvegeneratos/README.md](itarasyonvegeneratos/README.md)
- Standart kütüphane modülleri (`math`, `random`): [moduller/README.md](moduller/README.md)
- OS/dosya yolu yardımcıları: [os/README.md](os/README.md)
- PyQt5 GUI örnekleri: [pyqt5/README.md](pyqt5/README.md) ve [pyqt5/desing/README.md](pyqt5/desing/README.md)
- Qt ile daha bütünlüklü örnek: [qt_ornekleri/README.md](qt_ornekleri/README.md)
- Bölüm bölüm ileri seviye dersler: [ileri_seviye_python/README.md](ileri_seviye_python/README.md)
- Mini “proje” senaryoları: [ornek_proje/README.md](ornek_proje/README.md)
- JSON örnekleri: `json/deserialize-json.py`, `json/serialize_json.py` (klasörde README yok; kod üzerinden ilerleyebilirsin)

## Önerilen öğrenme sırası (pratik rota)

1) `demo/` + `fonksiyonlar/`
- Temel akış: `if/for/while`, `input()`, fonksiyon ve küçük problemler

2) `class/` + `hata_yönetimi/` + `dosya_islemleri/`
- Daha “proje gibi” yazmaya başlarsın: OOP, kontrollü hata yönetimi, kalıcı veri (dosya)

3) `Ileri_Seviye/` + `itarasyonvegeneratos/` + `ileri_seviye_python/`
- Daha güçlü teknikler: decorator/closure, iterator/generator, fonksiyonel araçlar, socket, async/thread/process

4) `pyqt5/` + `qt_ornekleri/`
- Arayüzde sinyal-slot mantığı, event-loop, UI dosyaları

5) `ornek_proje/`
- Küçük ama daha bütünlüklü senaryolar (envanter, sensör filtresi, drone filo)

## “Ben anladım mı?” kontrol listesi

- Bir dosyayı çalıştırıp, aynı çıktıyı üretecek şekilde 1-2 satırını değiştir (ör. limit, mesaj, liste içeriği).
- `print` yerine fonksiyonlardan `return` döndürüp sonucu başka yerde kullanmayı dene.
- Her klasördeki “Alıştırmalar” bölümünden en az 1 görev seç ve uygula.
