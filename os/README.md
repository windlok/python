# os — İşletim sistemiyle çalışmak (path, dizin, dosya)

Bu klasör, `os` ve `os.path` ile en sık yapılan işlemleri gösterir:

- Çalışma dizinini öğrenme
- Klasör listeleme
- Yol birleştirme ve parçalama
- Dosya/dizin var mı kontrolü

## Nasıl çalıştırılır?

```bash
python os/_os.py
```

## `_os.py` ne yapıyor?

Dosyada hem çalışan örnekler hem de yorum satırında bırakılmış “deney” parçaları var.

Aktif olarak:

- `os.name` ile işletim sistemi adını basar.
- `os.getcwd()` ile geçerli dizini yazar.
- `os.listdir()` ile dizindeki `.py` uzantılı dosyaları listeler.
- `os.path.exists(...)` ile bir dosya var mı kontrol eder.
- `os.path.abspath(...)`, `dirname(...)`, `join(...)`, `split(...)`, `splitext(...)` gibi path yardımcılarını gösterir.

Yorum satırlarında ayrıca:

- `chdir`, `system`, `makedirs`, `mkdir`, `rmdir`, `remove`, `rename` gibi komutlar var.

## Sık yapılan hatalar

- Windows yolunda `\` kaçış karakteridir; Python string içinde `"C:\\Users\\..."` yazmak gerekir (dosyada örnek var).
- `os.system` platforma bağımlıdır; taşınabilirlik için dikkat.

## Alıştırmalar

- Mevcut dizindeki tüm `.txt` dosyalarını listele.
- “Bugünün tarihine göre” bir klasör adı üretip oluştur (örn. `logs/2026-04-30`).
- `os.path.join` kullanarak platform bağımsız yol üret.
