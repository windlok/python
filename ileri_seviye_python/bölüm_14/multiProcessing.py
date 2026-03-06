import time 
import multiprocessing


def calculate_square(number, liste):
    print("sayının karesini hesaplıyorum...")

    for iindex,value in enumerate(number):
        time.sleep(0.3)  # Her sayının karesini hesaplamadan önce 1 saniye bekleyelim
        print(f"{value} sayısının karesi: {value**2}")
        liste[iindex] = value**2

def calculate_cube(number, liste):
    print("sayının küpünü hesaplıyorum...")

    for index,value in enumerate(number):
        time.sleep(0.3)  # Her sayının küpünü hesaplamadan önce 1 saniye bekleyelim
        print(f"{value} sayısının küpü: {value**3}")
        liste[index] = value**3

# multiprocessing, bir bilgisayarın aynı anda birden fazla işlem yapabilmesini sağlayan bir modüldür.
if __name__ == "__main__":
    sayilar = [1, 2, 3, 4, 5, 123,1222]

    t = time.time()

    liste_square = multiprocessing.Array('i', len(sayilar))  # 'i' tipi integer, len(sayilar) kadar eleman içeren bir dizi oluşturuyoruz
    liste_cube = multiprocessing.Array('i', len(sayilar))  # 'i' tipi integer, len(sayilar) kadar eleman içeren bir dizi oluşturuyoruz  

    #asenkron çalıştırma için multiprocessing kullanarak yapabiliriz
    p1 = multiprocessing.Process(target=calculate_square, args=(sayilar, liste_square))
    p2 = multiprocessing.Process(target=calculate_cube, args=(sayilar, liste_cube))

    #process'leri başlatmak için start() metodunu kullanırız
    p1.start()
    p2.start()


    #process'lerin bitmesini beklemek için join() metodunu kullanırız
    p1.join()
    p2.join()

    print(f"geçen süre: {time.time() - t} saniye")
    print(f"Kareler: {list(liste_square)}")
    print(f"Küpler: {list(liste_cube)}")

    print(f"geçen süre: {time.time() - t} saniye")

    print(list(liste_square[:]))
    print(list(liste_cube[:]))