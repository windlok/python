kilo = 5.0
menzil = 20.0
hiz = 60

mesafe = float(input("Teslimat mesafesi kaç km?"))
kargokilo = float(input("Kargo agirliği kaç kg?"))

def ucus_onayi(m,k):
    global yol
    if (k <= kilo):
        print("ucmaya uygun kilo")
        if(m*2<=menzil):
            print("mesafa uygundur")
            yol=(m/hiz)*60
            print(f'gidilen yol: {yol}')   
        else:
            print("Uçuş Reddedildi: Hedef çok uzak, batarya yetersiz!")    
    else :
        print("drone icin uygun degildir")

    
ucus_onayi(mesafe,kargokilo)