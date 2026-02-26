sayi =int(input('sayi: '))
asalmi=True

if sayi == 1:
    print('1 sayisi asal sayi degildir')

for i in range(2,sayi):
    if sayi % i == 0:
        asalmi =False
        break


if asalmi:
    print('sayi asaldir.')
else:
    print('sayi asal degildir.')        