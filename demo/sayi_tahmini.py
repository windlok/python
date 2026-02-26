import random
puan =100

sayi1=[x for x in range(100)]
#print(f'sayilar: {sayi1}')

rasgele = random.choice(sayi1)
print(f'gelen rasgele sayi: {rasgele}')

#burada kullanıcıdan hak bilgisini almadık
while(True):
    sayi = input("sayi giriniz: ")
    sayi = int(sayi)
    if(rasgele==sayi):
        print("dogru cevap")
        print(f'puanin: {puan}')
        break
    elif(sayi > rasgele):
        print("söyledigin sayi üretilen sayinin ustunde asagi bir deger soyleyiniz:")
    elif(sayi<rasgele):
        print("söyledigin sayi üretilen sayinin altinda yukarida bir deger soyleyiniz:")
    elif(puan==0) :
        print("puaniniz bitti")
        break
    puan=puan-20

hak=input("kac hak istersin: ")

while(True):
    sayi = input("sayi giriniz: ")
    sayi = int(sayi)
    if(rasgele==sayi):
        print("dogru cevap")
        print(f'puanin: {puan}')
        break
    elif(sayi > rasgele):
        print("söyledigin sayi üretilen sayinin ustunde asagi bir deger soyleyiniz:")
    elif(sayi<rasgele):
        print("söyledigin sayi üretilen sayinin altinda yukarida bir deger soyleyiniz:")

