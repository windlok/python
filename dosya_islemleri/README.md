# dosya_islemleri — Dosya okuma/yazma/güncelleme

Bu klasör; `open()`, dosya modları, okuma yöntemleri, `seek()` ile imleç yönetimi ve `with` context manager kullanımını öğretir.

## Nasıl çalıştırılır?

```bash
python dosya_islemleri/files.py
python dosya_islemleri/with.py
python dosya_islemleri/updating.py
```

> Bu dosyalar `dosya_islemleri/deneme.txt` üzerinde çalışır. Örneklerde göreceli yol kullanıldığı için proje kökünden çalıştırmak en güvenlisidir.

## Temel kavramlar (kısa özet)

- Modlar:
	- `"r"`: oku (dosya yoksa hata)
	- `"w"`: yaz (varsa siler, yoksa oluşturur)
	- `"a"`: sona ekle
	- `"x"`: yalnızca yoksa oluştur
	- `"r+"`: oku + yaz (imleç yönetimi önemli)

- Okuma metotları:
	- `read()` / `read(n)`
	- `readline()`
	- `readlines()`

- İmleç:
	- `file.seek(pos)` imleci taşır.
	- `read()` tekrar çalışınca “kaldığı yerden” devam eder.

- Encoding:
	- Türkçe karakter için `encoding="utf-8"` kullanmak iyi alışkanlıktır.

## Dosya dosya

### `files.py` — `open()` ve okuma yöntemleri

- Dosya modlarını yorum satırlarında tek tek özetler.
- `read()`, `read(n)`, `readline()`, `readlines()` örnekleri bulunur (bazıları yorum satırında).
- Aktif kısım: `readlines()` ile tüm satırları liste olarak alır.

Deneme:

- `readlines()` yerine `for line in file:` ile satır satır oku ve `strip()` uygula.

### `with.py` — Context manager

- `with open(...) as file:` kullanımı.
- `read(10)` ile ilk 10 karakteri okur, sonra `seek(0)` ile başa döner.

Öğrendirdikleri:

- `with` bloğu bitince dosya otomatik kapanır (elle `close()` unutma derdi yok).

### `updating.py` — Dosya içeriğini güncelleme

Bu dosyada birkaç farklı güncelleme yaklaşımı gösterilir (çoğu yorum satırında):

- `seek()` ile ortadan yazma
- `"a"` ile sona ekleme
- `"r+"` ile başa ekleme (içeriği okuyup başa yeni metin ekleyip tekrar yazma)
- `readlines()` + `insert()` + `writelines()` ile satır bazlı ekleme

Aktif kısım: dosyayı okuyup ekrana basar.

## Sık yapılan hatalar

- `r+` modunda `seek()` yapmadan yazarsan, dosyanın başını ezebilirsin.
- Dosyayı açıp kapatmayı unutmak: `with` kullan.

## Alıştırmalar

- `deneme.txt` içine bir “log” formatında tarihli satırlar ekle.
- Dosyadan “en son 5 satırı” oku (liste dilimleme).
- Satır bazlı arama yap: `windlok` geçen satırları bul.
