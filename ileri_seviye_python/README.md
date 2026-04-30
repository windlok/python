# ileri_seviye_python — Bölüm bölüm ileri Python

Bu klasör, ileri konuları “bölüm” mantığıyla toplar.
Her bölüm, bir kavrama odaklanan küçük scriptlerden oluşur.

## Nasıl çalıştırılır?

Her dosya tek başına çalışır. Örnek:
```bash
python "ileri_seviye_python/bölüm_2/list_comp.py"
python "ileri_seviye_python/bölüm_3/map.py"
python "ileri_seviye_python/bölüm_14/async.py"
```

> Bölüm adlarında Türkçe karakter var; Windows terminalinde tırnak kullanmak daha az sorun çıkarır.

## Bölümler (ne öğretiyor?)

- [bölüm_2/README.md](bölüm_2/README.md)
	- List comprehension'a giriş, koşullu üretimler

- [bölüm_2_örnek/README.md](bölüm_2_örnek/README.md)
	- Bölüm 2 pratikleri (metin/dict/list üzerinde comprehension)

- [bölüm_3/README.md](bölüm_3/README.md)
	- Fonksiyonel araçlar: `map`, `filter`, `lambda`, `any`, `all`, `sorted`, `min/max`, `sum/round`

- [bölüm_4/README.md](bölüm_4/README.md)
	- OOP'nin ileri tarafı: `@classmethod`, `@property`, metaclass

- [bölüm_4_örnek/README.md](bölüm_4_örnek/README.md)
	- “Shopping cart” ile sınıf pratiği

- [bölüm_13/README.md](bölüm_13/README.md)
	- Socket ile temel istemci-sunucu

- [bölüm_13_örnek/README.md](bölüm_13_örnek/README.md)
	- Aynı chat fikrinin iki uygulaması (kişisel vs referans)

- [bölüm_14/README.md](bölüm_14/README.md)
	- Eş zamanlılık: `asyncio`, `threading`, `multiprocessing`

## Çalışma önerisi

1) Önce `bölüm_2` ve `bölüm_3` ile “Pythonic” yazıma alış.
2) Sonra `bölüm_4` ile sınıf konusunu ileri seviyeye taşı.
3) Ardından `bölüm_13` (socket) ve `bölüm_14` (async/thread/process) ile gerçek dünyaya yaklaş.

## Alıştırma fikri

- Her dosyada 1 değişiklik yapıp çıktıyı etkileyerek öğren:
	- Filtre limitini değiştir
	- `reverse=True` yap
	- Yeni bir kullanıcı/soru ekle
