#dosya ve dizin işlemleri için kullanılan bir modül olan os modülünün içindeki fonksiyonları listeleyelim.
import os 

#os modülünün içindeki fonksiyonları listeleyelim.
# result = dir (os)
# print (result)

#en çok kullanılan os modüllerinden bazıları:
#os.name : işletim sisteminin adını döndürür.
result = os.name
print(result)  # işletim sisteminin adını döndürür.

#os.getcwd() : geçerli çalışma dizinini döndürür.
result1 = os.getcwd()
print(result1)  # geçerli çalışma dizinini döndürür.

# #os.listdir() : belirtilen dizindeki dosya ve klasörlerin listesini döndür
# result2 = os.listdir()
# print(result2)  # belirtilen dizindeki dosya ve klasörlerin listesini döndürür.
# result3 = os.listdir("C:\\")  # belirtilen dizindeki dosya ve klasörlerin listesini döndürür.
# print(result3)  # belirtilen dizindeki dosya ve klasörlerin listesini döndürür.

#os.listdir() : belirtilen dizindeki dosya ve klasörlerin listesini döndürür.
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)  # belirtilen dizindeki dosya ve klasörlerin listesini döndürür.
    

# #os.chdir() : belirtilen dizine geçiş yapar.
# c=os.chdir("C:\\Users\\User\\Desktop")  # belirtilen dizine geçiş yapar.
# print(os.getcwd())  # belirtilen dizine geçiş yapar.
# #.. ile bir üst dizine geçiş yapabiliriz.
# c1=os.chdir("..")  # belirtilen dizine geçiş yapar.
# print(os.getcwd())  # belirtilen dizine geçiş yapar.
# #../.. ile iki üst dizine geçiş yapabiliriz.
# c2=os.chdir("../..")  # belirtilen dizine geçiş yapar.
# print(os.getcwd())  # belirtilen dizine geçiş yapar.

# #os.system() : belirtilen komutu işletim sisteminde çalıştırır.
# result2 = os.system("dir")  # belirtilen komutu işletim sisteminde çalıştırır.
# print(result2)  # belirtilen komutu işletim sisteminde çalıştırır.

#os.makedirs() : belirtilen dizinleri oluşturur.
# a=os.makedirs("yeni_dizin/yeni_alt_dizin")  # belirtilen dizinleri oluşturur.

# #os.mkdir() : belirtilen isimde bir klasör oluşturur.
# result3 = os.mkdir("yeni_klasor.txt")  # belirtilen isimde bir klasör oluşturur.
# print(result3)  # belirtilen isimde bir klasör oluşturur.

# #os.rmdir() : belirtilen isimde bir klasör siler.
# result4 = os.rmdir("yeni_dizin")  # belirtilen isimde bir klasör siler.
# print(result4)  # belirtilen isimde bir klasör siler.

# #os.removedirs() : belirtilen dizinleri siler.
# result5 = os.removedirs("yeni_dizin/yeni_alt_dizin")  # belirtilen dizinleri siler.
# print(result5)  # belirtilen dizinleri siler.

# #os.remove() : belirtilen isimde bir dosya siler.
# result5 = os.remove("yeni_dosya.txt")
# print(result5)  # belirtilen isimde bir dosya siler.

#os.path.exists() : belirtilen dosya veya klasörün var olup olmadığını kontrol eder.
result6 = os.path.exists("yeni_dosya.txt")
print(result6)  # belirtilen dosya veya klasörün var olup olmadığını kontrol eder.
#os.path.abspath() : belirtilen dosya veya klasörün tam yolunu döndürür.
result7 = os.path.abspath("yeni_dosya.txt")
print(result7)  # belirtilen dosya veya klasörün tam yolunu döndürür.
#os.path.dirname() : belirtilen dosya veya klasörün dizin adını döndürür.
result8 = os.path.dirname("C:\\Users\\User\\Desktop\\python\\yeni_dosya.txt")
print(result8)  # belirtilen dosya veya klasörün dizin adını döndürür.
#os.path.dirname(os.path.abspath("yeni_dosya.txt")) : belirtilen dosya veya klasörün dizin adını döndürür.
result9 = os.path.dirname(os.path.abspath("yeni_dosya.txt"))
print(result9)  # belirtilen dosya veya klasörün dizin adını döndürür.
#os.path.exists() : belirtilen dosya veya klasörün var olup olmadığını kontrol eder.
result10 = os.path.exists("C:/users/user/desktop/pythone")
print(result10)  # belirtilen dosya veya klasörün var olup olmadığını kontrol eder.
#os.path.isdir() : belirtilen yolun bir dizin olup olmadığını kontrol eder.
result11 = os.path.isdir("C:/users/user/desktop/python")
print(result11)  # belirtilen yolun bir dizin olup olmadığını kontrol eder.
#os.path.join() : belirtilen dizinleri birleştirir.
result12 = os.path.join("C:/users/user/desktop/", "python")
print(result12)  # belirtilen dizinleri birleştirir.
#os.path.split() : belirtilen yolun dizin ve dosya adını döndürür.
result13 = os.path.split("C:/users/user/desktop/python/yeni_dosya.txt")
print(result13)  # belirtilen yolun dizin ve dosya adını döndür
#os.path.splitext() : belirtilen dosya adının uzantısını döndürür.
result14 = os.path.splitext("yeni_dosya.txt")
print(result14)  # belirtilen dosya adının uzantısını döndürür.

# #os.rename() : belirtilen isimde bir dosya veya klasörün adını değiştirir.
# result7 = os.rename("yeni_klasor", "eski_klasor")
# print(result7)  # belirtilen isimde bir dosya veya klasörün adını değiştirir.


