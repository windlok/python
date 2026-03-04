#lambda arguments: expressinon
#def kullanımı
def kareAl(a):
    return a ** 2

sonuc = kareAl(5)  
print(sonuc)

#lambda ile kullanımı
sonuc1=(lambda a: a ** 2)(5)
print(sonuc1)

kareAl = lambda a: a ** 2
sonuc2 = kareAl(5)
print(sonuc2)

toplama = lambda a, b, c : a + b + c
print(toplama(1, 2, 3))

def myFunc(n):
    return lambda a : a * n

myDoubler = myFunc(2)
print(myDoubler(11))

carpma2 = myFunc(2)
sonuc4 =carpma2(33)
print(sonuc4)
