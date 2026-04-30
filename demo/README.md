# demo — Mini uygulamalar & alıştırmalar

Bu klasördeki dosyalar “küçük ama çalıştırılabilir” örneklerden oluşur.
Ortak özellik: çoğu `input()` kullanır ve terminal etkileşimi üzerinden öğrenmeyi hedefler.

## Nasıl çalıştırılır?

Proje kökünden örnekler:
```bash
python demo/asal.py
python demo/quiz.py
python demo/not_uygulaması.py
```

> Not: `not_uygulaması.py` dosyası `demo/kullaniciler.txt` yolunu kullanır. Bu yüzden komutu proje kökünden çalıştırmak önemli.

## Dosya dosya

### `asal.py` — Asal sayı kontrolü

- Kullanıcıdan bir sayı alır.
- `2..n-1` arası bölen arayıp asal olup olmadığını belirler.

Öğrendirdikleri:

- `input()` + `int()`
- `for` döngüsü ve `break`
- boolean bayrak (`asalmi`)

Alıştırma:

- Negatif sayılar ve 0 için davranışı belirle.
- Daha hızlı kontrol: `range(2, int(sqrt(n))+1)`.

### `bankamatik.py` — Çok basit ATM/hesap

- Hesap bilgisi sözlük (`dict`) olarak tutulur.
- `paracek(hesap, miktar)` fonksiyonu bakiye kontrolü yapar.

Öğrendirdikleri:

- Sözlük erişimi: `hesap["bakiye"]`
- Fonksiyonla “iş” tanımlama

Alıştırma:

- Para yatırma fonksiyonu ekle.
- İşlem geçmişini liste olarak tut.

### `error_demo.py` — Hata yakalama + `raise`

Dosyada birkaç farklı deneme var (bazıları yorum satırında).
Aktif kısım:

- `faktoriyel(x)` fonksiyonu `x` negatifse `ValueError` üretir.
- Örnek giriş listesinde (`[5,10,20,-3,'asd']`) hatalı değerler try/except ile yakalanır.

Öğrendirdikleri:

- “Kendi kuralını” `raise` ile zorlamak
- Birden fazla veri üzerinde dönerken hatalı olanı atlayıp devam etmek

Alıştırma:

- `TypeError` yakalayıp `"asd"` gibi girdileri ayrı mesajla yönet.

### `fonksiyon.py` — Fonksiyon pratikleri

Dosya birkaç mini görev içerir:

1) `deger(a, b)` ile `b` kez yazdırma
2) `list(*params)` ile değişken sayıda parametreyi listeye çevirme
3) `asal(a, b)` ile iki sayı arasındaki asalları yazdırma
4) `tambolen(b)` ile tam bölenleri yazdırma
5) `tambolenleribul(sayi)` ile tam bölen listesini döndürme

Öğrendirdikleri:

- Parametre, dönüş değeri, `*args`
- Döngü içinde iç içe döngü

Alıştırma:

- `tambolen` fonksiyonunu “liste döndürecek” hale getir.

### `quiz.py` — Sınıf tabanlı quiz

İki sınıf var:

**`Question`**

- Soru metni, şıklar, doğru cevap
- `checkAnswer()` ile kontrol

**`Quiz`**

- Sorular listesi
- `score` ve `questionsindex` ile ilerleme
- `displayQueation()` -> kullanıcıdan cevap alır
- `guess()` -> kontrol eder, bir sonraki soruya geçer
- `showScore()` -> quiz bitince sonucu gösterir

Öğrendirdikleri:

- Sınıf ile “durum” (state) yönetmek
- Metotlar arası akış

Alıştırma:

- 10 soru ekle, skoru yüzde olarak yazdır.
- Yanlış cevapta doğru cevabı göster.

### `sayi_tahmini.py` — Sayı tahmin oyunu

- 0-99 arasında rastgele sayı seçer.
- Kullanıcı tahmin eder; yukarı/aşağı yönlendirme yapar.
- İlk bölümde puan 100'den başlayıp her yanlışta 20 azalır.

Not:

- Dosyada ikinci bir tahmin döngüsü daha var; “hak” soruluyor ama aktif olarak kullanılmıyor. Bunu geliştirmek iyi bir alıştırmadır.

Alıştırma:

- Hak sayısını gerçekten kullan (örn. 5 hak).
- Puanı hakla ilişkilendir (her hak puanı düşürsün).

### `not_uygulaması.py` + `kullaniciler.txt` — Dosyaya kayıtlı mini not sistemi

Bu örnek, sınıf + dosya yazma + menü akışını bir araya getirir.

Parçalar:

- `kullanici`: ad/soyad/vize/final/but bilgisini tutar.
- `dosya_kayit`: kullanıcıları `demo/kullaniciler.txt` dosyasına ekler ve gösterir.
- `secim()`: terminal menüsü (yeni kayıt, not düzenleme, kaydetme, listeleme).

Öğrendirdikleri:

- Dosyaya satır satır yazma (`open(..., "a")`)
- Menü döngüsü ile uygulama akışı kurma

Alıştırma:

- Kullanıcı listesini dosyadan okuyup başlangıçta yükle.
- Not düzenlemede vize/final seçimini menüye bağla.
