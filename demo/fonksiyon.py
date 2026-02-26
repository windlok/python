#1.örnek
def deger(a="",b=0):
    for x in range(b):
        print(f'deger: {a} donme sayisi: {x+1} ')

deger('mustafa',3); 

#2.örnek
def list(*params):
    liste=[]
    for x in params:
        liste.append(x)
    return liste
   
print(list(12,'mustafa',100,True))

#3.örnek
a=int(input('bir sayi giriniz: '))
b=int(input('bir sayi giriniz: ')) 
 
def asal(a=1,b=2):
    if a<b:
        for x in range(a,b):
            if x<2:
                print(f'sayi: {x} , asal sayi degildir')
                continue

            asalsayi=True
            for y in range(2,x):
                if x%y==0:
                    asalsayi=False
                    break
            if asalsayi:
                    print(f'sayi: {x} , asal sayidir')

            else:
                    print(f'sayi: {x} , asal sayi degildir')    
    else:
         print('birinci sayi ikinci sayidan buyuk olmalidir')
print(asal(a,b))

#4.örnek
a = int(input("bir sayi giriniz: "))
def tambolen(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(f'girilen sayi: {b} tam bölen: {i}')
tambolen(a) 

#5.örnek
def tambolenleribul(sayi):
    tambo=[]

    for i in range(2,sayi):
        if(sayi%i==0):
            tambo.append(i)
    return tambo        
tambolenleribul(20)