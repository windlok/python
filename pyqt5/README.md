# pyqt5 — PyQt5 ile masaüstü GUI örnekleri

Bu klasör, PyQt5 ile pencere açmayı, widget yerleştirmeyi ve kullanıcı etkileşimini (sinyal-slot) öğretir.
PyQt5'te temel akış:

1) `QApplication` oluştur
2) Pencereyi (QWidget/QMainWindow) oluştur
3) Widget'ları yerleştir
4) Sinyalleri (`clicked`, `textChanged`...) slotlara (fonksiyon) bağla
5) `app.exec_()` ile event-loop başlat

## Kurulum

```bash
pip install PyQt5
```

## Nasıl çalıştırılır?

Proje kökünden:
```bash
python pyqt5/creating.app.py
python pyqt5/class.py
python pyqt5/desing/calculator.py
```

## Dosya dosya

### `creating.app.py` — En temel pencere

- `QApplication` ve `QMainWindow` oluşturur.
- Başlık, boyut/konum (`setGeometry`), ikon (`icon.png`), tooltip ayarlar.
- `app.exec_()` ile uygulamayı başlatır.

Ne öğrenirsin:

- Event-loop mantığı
- Pencere temel ayarları

### `class.py` — Basit form: ad/soyad al, butonla yazdır

- `QLabel` ve `QLineEdit` ile iki alan oluşturur.
- “kaydet” butonuna tıklanınca girilen metinleri konsola yazar.

Ne öğrenirsin:

- Widget oluşturma ve konumlandırma (`move`)
- Buton `clicked` sinyalini fonksiyona bağlama

### `calculator2.py` — UI sınıfı ile hesap makinesi (Qt Designer çıktısı)

- 2 sayı alan iki `QLineEdit` ve 4 işlem butonu.
- Buton tıklanınca ilgili matematik işlemini yapıp sonucu label'a yazar.

Önemli not (import yolu):

- Dosya `from MainWindow import Ui_MainWindow` diye import eder.
- Repo'da `MainWindow.py` dosyası `pyqt5/desing/MainWindow.py` altında duruyor.
- Eğer `ModuleNotFoundError: No module named 'MainWindow'` görürsen:
	- `MainWindow.py` dosyasını `pyqt5/` içine al, veya
	- `calculator2.py` içindeki import'u bulunduğu konuma göre düzenle.

### `desing/` alt klasörü

Qt Designer ile hazırlanan `.ui` dosyaları ve onların Python çıktıları burada.
Ayrıntı için: [pyqt5/desing/README.md](desing/README.md)
