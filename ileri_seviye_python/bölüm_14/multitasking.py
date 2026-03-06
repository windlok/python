#multitasking nedir?
#multitasking, bir bilgisayarın aynı anda birden fazla görevi yerine getirebilme yeteneğidir. 
#Bu, birden fazla programın veya işlemin aynı anda çalışmasına izin verir. 
#Multitasking, işletim sistemleri tarafından yönetilir ve genellikle iki tür multitasking vardır: preemptive multitasking ve cooperative multitasking.

import time
import threading

def calculate_square(num):
    print("sayının karesini hesaplıyorum...")

    for i in num:
        time.sleep(0.3)  # Her sayının karesini hesaplamadan önce 1 saniye bekleyelim
        print(f"{i} sayısının karesi: {i**2}")

def calculate_cube(num):

    print("sayının küpünü hesaplıyorum...")

    for i in num:
        time.sleep(0.3)  # Her sayının küpünü hesaplamadan önce 1 saniye bekleyelim
        print(f"{i} sayısının küpü: {i**3}")


sayilar = [1, 2, 3, 4, 5]

#senkron çalıştırma için bu şekilde yapabiliriz
t = time.time()

#asenkron çalıştırma için threading kullanarak yapabiliriz
t1 = threading.Thread(target=calculate_square, args=(sayilar,))
t2 = threading.Thread(target=calculate_cube, args=(sayilar,))

#thread'leri başlatmak için start() metodunu kullanırız
t1.start()
t2.start()

#thread'lerin bitmesini beklemek için join() metodunu kullanırız
t1.join()
t2.join()


print(f"geçen süre: {time.time() - t} saniye")

# calculate_cube(sayilar)

# print(f"geçen süre: {time.time() - t} saniye")


