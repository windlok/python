def usalma(number):
    def inner_power(power):
        return number ** power
    return inner_power

iki_kuvvet = usalma(2)
print(iki_kuvvet(3))  # 2^3 = 8
print(iki_kuvvet(4))  # 2^4 = 16

def yetki_sorgula(page):
    def inner(user):
        if user == "admin":
            return "{0} kullanıcısı {1} sayfasına erişebilir.".format(user, page)
        else:
            return "{0} kullanıcısı {1} sayfasına erişemez.".format(user, page)
    return inner
admin_sayfasi = yetki_sorgula("Admin Paneli")
print(admin_sayfasi("admin"))  # admin kullanıcısı Admin Paneli sayfasına erişebilir.