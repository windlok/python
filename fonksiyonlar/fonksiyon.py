def toplam(a,b):
    return a+b

print(toplam(3,5))

# fonksiyonlarda variable sayida parametre gonderebiliriz
#*args: fonksiyona gonderilen parametreleri tuple olarak alir gönderlen parametre sayisi bilinmiyorsa kullanilir
def kisiler(*kisiler):
    
    """DOCSTRING: kisiler fonksiyonu verilen isimleri ekrana yazdirir
    Args:
        *kisiler: fonksiyona gonderilen isimler
    OUTPUT:
        verilen isimler ekrana yazdirilir
    """

    for kisi in kisiler:
        print(kisi)

kisiler('Ali','Veli','Ayse')

# fonksiyonlarda default degerler verebiliriz
def name(name="user"):
    print(name)

name()
name("Ahmet")
print(help(kisiler))

def change(n):
    n[0]='istanbul'

n = ['ankara','izmir','bursa']

change(n[:]) # n[:] ile n'nin kopyasini gonderiyoruz
print(n) # n listesinin degismis halini goruyoruz
change(n) # n'nin kendisini gonderiyoruz
print(n)# n listesinin degismis halini goruyoruz

#** artarsa dictionary gonderilir
def kisiler(**kisiler):
    for key,value in kisiler.items():
        print(f'{key}: {value}')
kisiler(name='Ali',age=30,city='Istanbul')
kisiler(name='Veli',age=25,city='Izmir')     


def myFunc(a,b,*c,**d):
    print(a)
    print(b)
    print(c)
    print(d)

myFunc(1,2,3,4,5,name='Ali',age=30)    