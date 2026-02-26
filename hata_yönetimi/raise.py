"""x = 10
if x> 5:
    raise Exception('x 5 ten buyuk olamaz')"""

#bir hata olusturmak icin kullanilir
import re


def check_password(psw):
    if len(psw)<8:
        raise Exception('parola en az 8 karakter olmalidir')
    elif len(psw)>16:
        raise Exception('parola en fazla 16 karakter olmalidir')
    elif not re.search('[a-z]',psw):
        raise Exception('parola kucuk harf icermelidir')
    else:
        print('parola basariyla kaydedildi')

password = input('parola: ')
try:
    check_password(password)
except Exception as hata:
    print(f'hata mesaji: {hata}')