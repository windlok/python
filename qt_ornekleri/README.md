# qt_ornekleri — SkyLog drone arayüz örneği (PyQt5 + QTimer)

Bu klasör, tek tek widget örneklerinden biraz daha “senaryo” içeren bir GUI denemesidir.
Temel fikir: Bir drone'u UI üzerinden başlat/durdur, pil ve irtifa gibi değerleri ekranda güncelle.

## Çalıştırma

Dosya adında Türkçe karakter var; tırnakla çalıştır:
```bash
python "qt_ornekleri/Siparis_SkyLog_Yer_Kontrol_İstasyonu.py"
```

## Dosyalar ve roller

### `Gorsel_Arayuz.ui` -> `skylogui.py`

- `Gorsel_Arayuz.ui`: Qt Designer tasarımı (pencere, butonlar, progress bar, text area…)
- `skylogui.py`: bu tasarımın `pyuic5` ile üretilmiş Python karşılığı

`skylogui.py` genelde elle düzenlenmez; UI elemanlarını (`self.pro_batarya`, `self.lbl_irtifa`...) oluşturur.

### `Siparis_SkyLog_Yer_Kontrol_İstasyonu.py` — Uygulama başlangıcı

- `App(QMainWindow, Ui_MainWindow)` sınıfı UI'ı kurar (`setupUi`).
- Ardından `dron` sınıfından bir nesne oluşturur ve UI referansını verir.
- “Sistemi Başlat / Durdur” butonlarını drone metodlarına bağlar:
	- `clicked.connect(self.d.ucus_basla)`
	- `clicked.connect(self.d.ucus_durdur)`

Öğrenilecekler:

- UI ile “iş mantığı” sınıfını birbirine bağlama
- Signal-slot

### `dron.py` — Drone simülasyonu (`QTimer` ile)

Bu sınıf, UI'yı güncellemek için iki timer kullanır:

- `sarj_timer`: pili 100'e doğru arttırır, progress bar'ı günceller
- `ucus_timer`: uçuş sırasında irtifa üretir, pil düşürür, text area'ya yazar

Akış:

1) `ucus_basla()` çağrılır.
2) Pil yeterli değilse şarj başlatılır (`sarj_timer.start(...)`).
3) Şarj bitince otomatik uçuş başlar (`ucus_timer.start(...)`).
4) `ucus_guncelle()` her tick'te irtifa basar ve pil azaltır.
5) Şartlar bitince timer durur ve UI'da durum güncellenir.

## Sık notlar / geliştirme fikirleri

- Uçuş şartı kontrolünde `dron_pil` karşılaştırması ters olabilir (kendi kontrolün olarak değerlendir).
- UI güncellemelerinde `self.ui` referansı kritik: drone sınıfı, UI elemanlarına dokunuyor.
- Daha “gerçek” telemetri için ayrı bir thread veya async yaklaşımı gerekebilir.

## Alıştırmalar

- Hız (`lcd_hiz`) değerini de timer ile güncelle.
- Uçuş bitince irtifa alanını temizle veya log dosyasına yaz.
- Pil azaldığında otomatik “iniş” senaryosu ekle.
