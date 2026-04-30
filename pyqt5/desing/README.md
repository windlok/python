# pyqt5/desing — Qt Designer (.ui) + PyQt5 örnekleri

Bu klasörde iki tip dosya görürsün:

- `.ui` dosyaları: Qt Designer ile çizilmiş arayüz tasarımı
- `*ui.py` veya `MainWindow.py` gibi dosyalar: `.ui` dosyasının `pyuic5` ile Python'a çevrilmiş hali
- “asıl uygulama” dosyaları: butonlara tıklanınca ne olacak, veriyi nereye yazacağız vs. (ör. `combobox.py`, `checkedBox.py`...)

## Çalıştırma

Bu klasördeki örneklerin çoğu doğrudan çalışır:
```bash
python pyqt5/desing/combobox.py
python pyqt5/desing/checkedBox.py
python pyqt5/desing/list.py
python pyqt5/desing/msgbox.py
python pyqt5/desing/radiobutton.py
python pyqt5/desing/table_view.py
python pyqt5/desing/time_edit.py
python pyqt5/desing/layouts.py
python pyqt5/desing/calculator.py
python pyqt5/desing/wim-items.py
```

## UI dosyasını Python'a çevirme (pyuic5)

Genel komut:
```bash
pyuic5 <tasarim.ui> -o <cikti.py>
```

Örnek:

- `desing.ui` -> `MainWindow.py`
	```bash
	pyuic5 pyqt5/desing/desing.ui -o pyqt5/desing/MainWindow.py
	```

> Not: `*ui.py` dosyaları genellikle “elle düzenlenmez”. Mantık kodu ayrı `.py` dosyasında tutulur.

## Örnekler (dosya dosya)

### `calculator.py` — Elle widget yerleşimi + `sender()`

- `QLabel`, `QLineEdit`, `QPushButton` ile arayüzü tamamen kodla kurar.
- Tek bir `hesapla()` fonksiyonu, tıklanan butonu `self.sender()` ile anlayıp işlemi seçer.

Öğrenilecekler:

- OOP ile pencere sınıfı yazma (`QMainWindow`)
- Sinyal-slot: `btn.clicked.connect(self.hesapla)`
- `sender()` ile “hangi buton?” çözmek

### `MainWindow.py` + `desing.ui` — Designer'dan gelen hesap makinesi UI'si

- `desing.ui` tasarımından üretilmiş UI sınıfı.
- Bu dosya tek başına uygulama çalıştırmaz; sadece arayüzü kurar.
- Bu UI'yı kullanan bir “mantık” dosyası ile birleştirilir (ör. `pyqt5/calculator2.py` gibi).

### `checkedBox.py` (+ `checkedBoxui.py`, `checkedBox.ui`)

- Birden çok checkbox seçimi.
- `stateChanged` ile anlık “seçildi/seçilmedi” bilgisi.
- `findChildren(QCheckBox)` ile groupBox içindeki tüm checkbox'ları dolaşıp seçili olanları toplar.

Öğrenilecekler:

- Widget ağacında arama (`findChildren`)
- GroupBox içindeki elemanları toplu yönetme

### `combobox.py` (+ `comboboxui.py`, `combobox.ui`)

- `QComboBox` içine item yükleme: `addItems`
- Seçili elemanı alma: `currentText`, `currentIndex`, `count`
- Seçim değişince tetiklenen sinyaller:
	- `currentIndexChanged(int)`
	- `currentIndexChanged(str)`

### `layouts.py` — Layout yöneticileri

- `QGridLayout`, `QVBoxLayout`, `QHBoxLayout` kullanımını gösterir.
- Renkli kutucuklar için `Color(QWidget)` sınıfı ve `QPalette` kullanır.
- `setContentsMargins` ile layout boşlukları ayarlanır.

### `list.py` (+ `listui.py`, `listui.ui`) — QListWidget CRUD

- Listeye öğrenci ekleme/düzenleme/silme
- Yukarı/aşağı taşıma
- Sıralama (`sortItems`)
- `QInputDialog` ile kullanıcıdan metin alma

### `msgbox.py` (+ `msgboxui.py`, `msgboxui.ui`) — QMessageBox

- “Çıkmak istiyor musun?” tarzı onay penceresi.
- `QMessageBox.question(...)` ile tek satırda Ok/Cancel döndürme.

### `radiobutton.py` (+ `radioboxui.py`, `radiobox.ui`) — RadioButton grupları

- Ülke / eğitim / yaş gibi seçenekleri radio button ile seçtirme.
- `toggled` ile anlık seçim takibi.
- `findChildren(QRadioButton)` ile seçili olanı bulma.

### `table_view.py` (+ `table_viewui.py`, `table_viewui.ui`) — QTableWidget ile tablo

- Başlangıçta ürün listesini tabloya yükler.
- Kolon başlıkları, genişlik ayarları.
- `saveProducts()` fonksiyonu yeni ürün ekleme mantığını içerir (UI'da bir butona bağlayarak aktif edebilirsin).

### `time_edit.py` (+ `time_editui.py`, `time_editui.ui`) — QDate ile tarih farkı

- Başlangıç/bitiş tarihlerini alır.
- `daysInMonth`, `daysInYear`, `daysTo` gibi metodlarla fark hesaplar.
- Sonuçları konsola basar.

### `wim-items.py` — OOP ile basit form

- `MyWindow(QMainWindow)` sınıfı içinde widget'ları kurar.
- Butona basınca label'a sonuç yazar.

## Sık yapılan hatalar

- `.ui` dosyasını her güncellediğinde `pyuic5` ile tekrar üretmen gerekir.
- UI dosyası ile mantık dosyasını karıştırırsan bakım zorlaşır. “UI = görünüm, .py = davranış” ayrımı yap.
