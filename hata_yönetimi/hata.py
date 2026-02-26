"""try:
    x = int(input('x: '))
    y = int(input('y: '))
except ZeroDivisionError:
    print('sifira bolme hatasi')
except ValueError:
    print('deger hatasi')
print(f'{x} sayisinin {y} sayisina bolumu: {x/y}')
"""
"""try:
    a = int(input('bir sayi giriniz: '))
    b = int(input('bir sayi giriniz: '))
except (ZeroDivisionError,ValueError) as hata:
    print(f'hata mesaji: {hata}')

print(f'{a} sayisinin {b} sayisina bolumu: {a/b}')
"""

"""try:
    a = int(input('bir sayi giriniz: '))
    b = int(input('bir sayi giriniz: '))
except:
    print("bir hata olustu")

print(f'{a} sayisinin {b} sayisina bolumu: {a/b}')
"""

"""try:
    a = int(input('bir sayi giriniz: '))
    b = int(input('bir sayi giriniz: '))
except (ZeroDivisionError,ValueError) as hata:
    print(f'hata mesaji: {hata}')
else:
    print(f'{a} sayisinin {b} sayisina bolumu: {a/b}')
"""
while True:
    try:
        a = int(input('bir sayi giriniz: '))
        b = int(input('bir sayi giriniz: '))
    except Exception as hata:
        print(f'hata mesaji: {hata}')
    else:
        print(f'{a} sayisinin {b} sayisina bolumu: {a/b}')
        break
    
    #burada dosya kapama,veritabani baglantisi kapama gibi islemler yapilabilir
    finally:
        print('islem tamamlandi')