import re
"""
liste = ["1","2","5a","10b","abc","10","50"]
"""
#liste elemanları içindeki sayısal degerleri bulunur 

"""for sayi in liste:
    try:
        result=int(sayi)
    except TypeError:
        print(f'lsitedeki {sayi} sayi degildir')
        continue
    except ValueError:
        print(f'lsitedeki {sayi} sayi degildir') 
        continue
    else:
        print(f'listedeki {sayi} sayidir')    
"""

#kullanıcıdan q degerini girmedigi surece aldıgımız her input sayısı oldugundan emin olunuz aksi halde hata ver 
"""while True:
    sayi =str(input("bir deger giriniz: "))
    if sayi=="q":
        break

    try:
        result=float(sayi)
        print(f'girilen sayi {result}')

    except ValueError:
        print(f'girilen deger {sayi} gecersiz')
"""
#girilen sayi türkçe karakter içermemelidir hata verdirme uygulaması yapmak iştiyorum
"""def checpassword(parola):
    turkce_karakter='şğçüıİ'

    for i in parola:
        if i in turkce_karakter:
            raise TypeError('parola turkce karakter icereemz')
       
    print(f'parola gecerli')
        
parola=input('parola:')
try:
    checpassword(parola)
except TypeError as err:
    print(err)"""

#faktoriyel fonksiyonu olustur gelen degerere göre hata mesajı getir göster

def faktoriyel(x):
    x=int(x)

    if x < 0:
        raise ValueError("negatif deger")
    result =1

    for i in range(1,x+1):
        result *= i

    return result

for x in [5,10,20,-3,'asd']:
    try:
        y =faktoriyel(x)

    except ValueError as err:
        print(err)   
        continue
    print(y)    