ahmethesap={
    'adi': 'Ahmet',
    'soyadi': 'Yilmaz',
    'hesap_no': '123456789',
    'bakiye': 1000
}
mahmuthesap={
    'adi': 'Mahmut',
    'soyadi': 'Yilmaz',
    'hesap_no': '987654321',
    'bakiye': 2000
}

def paracek(hesap,miktar):
    print(f"merhaba {hesap['adi']}")

    if(hesap['bakiye']>=miktar):
        hesap['bakiye'] -=miktar
        print(f"para cekme işlemi basarili kalan para: {hesap['bakiye']}")
    else:
        print("hesabinda o kadar para yok")    

paracek(ahmethesap,1000)
paracek(mahmuthesap,3000)


cars=["araba"]
