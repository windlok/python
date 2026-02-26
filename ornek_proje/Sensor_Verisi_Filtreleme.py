import random
ham_veri = []

for i in range(0, 12):
    ham_veri.append(random.randrange(-500, 999))

def veri_temizle():
    temiz_veri = []
    
    # 1. Aşama: Filtreleme Döngüsü
    for deger in ham_veri:  # Senin [i] mantığını bu şekilde sadeleştirdim
        if (deger <= 200 and deger >= 0):
            temiz_veri.append(deger)
            print(f"Veri düzgün: {deger}")
        else:
            print(f"Veri bozuk: {deger}")
            
    # DÖNGÜ BİTTİ! Şimdi girintiyi geriye alıp raporlamaya geçiyoruz:
    
    print("\n--- SENSÖR ANALİZ RAPORU ---")
    print(f'Elenen bozuk veri sayısı: {len(ham_veri) - len(temiz_veri)}')
    
    if temiz_veri:
        temiz_veri.sort()
        print(f'Sıralı temiz veri: {temiz_veri}')
        print(f'Geçerli okuma sayısı: {len(temiz_veri)}')
        print(f'Maksimum Sıcaklık: {max(temiz_veri)}')
        print(f'Minimum Sıcaklık: {min(temiz_veri)}')
        print(f'Ortalama Sıcaklık: {sum(temiz_veri)/len(temiz_veri):.2f}')
    else:
        print('Geçerli veri yok.')

# Sistemi çalıştırıyoruz
veri_temizle()