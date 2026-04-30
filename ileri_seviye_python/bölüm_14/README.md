# bölüm_14 — Eşzamanlılık: asyncio / threading / multiprocessing

Bu bölüm, “aynı anda birden fazla iş” fikrini 3 farklı araçla gösterir:

- `asyncio`: I/O ağırlıklı işler için tek thread içinde asenkron akış
- `threading`: aynı proses içinde birden fazla thread
- `multiprocessing`: birden fazla proses (çok çekirdek kullanabilir)

## Çalıştırma

```bash
python "ileri_seviye_python/bölüm_14/async.py"
python "ileri_seviye_python/bölüm_14/multitasking.py"
python "ileri_seviye_python/bölüm_14/multiProcessing.py"
```

## Dosya dosya

### `async.py` — asyncio ile asenkron görevler

- `fetch_data(id, delay)` async fonksiyonu:
	- başlar, `await asyncio.sleep(delay)` ile bekler, biter ve dict döndürür.
- `main(msg)`:
	1) `create_task` ile 1 görev başlatıp `await` eder (tek görev örneği).
	2) Sonra iki görevi aynı anda başlatır ve `asyncio.gather` ile birlikte bekler.

Çıktıda “Elapsed time” ve “Total elapsed time” değerleri, paralel/seri çalışmayı anlamana yardım eder.

Not:

- Dosya `asyncio.run(main(...))` çağrısını iki kez yapıyor; her seferinde event-loop yeniden kurulur.

Alıştırma:

- `fetch_data` sayısını 5'e çıkar, `gather` ile hepsini topla.
- `await asyncio.sleep(2)` satırını kaldırıp süre farkını gözle.

### `multitasking.py` — threading ile aynı anda iki iş

- `calculate_square` ve `calculate_cube` fonksiyonları `time.sleep` ile gecikme simüle eder.
- Thread'ler başlatıldığında çıktıların iç içe geçtiğini görürsün.

Önemli fikir:

- Python'da GIL sebebiyle CPU-bound işlerde threading hız kazandırmayabilir.
- Ama `sleep`, ağ, dosya gibi I/O bekleyen işlerde “boş zamanı” değerlendirmek için işe yarar.

Alıştırma:

- Thread başlamadan önce `t = time.time()`'ı yeniden ayarla ve süreyi daha doğru ölç.
- Sonuçları bir listeye yazmak için `queue.Queue` kullan.

### `multiProcessing.py` — multiprocessing ile iki ayrı proses

- Kare ve küp hesapları iki ayrı proses olarak başlatılır (`Process`).
- Sonuçları paylaşmak için `multiprocessing.Array` kullanılır.
- Windows'ta kritik: `if __name__ == "__main__":` bloğu var (olmazsa child process tekrar aynı dosyayı import eder).

Alıştırma:

- `Array` yerine `multiprocessing.Queue` ile sonuç taşı.
- Sayı listesini büyüt, süre farkını ölç.
