#-"w": (write) ekleme modu. Dosya yoksa oluşturur, varsa içeriği siler ve yeni içerik ekler.
#-"r": (read) okuma modu. Dosya yoksa hata verir, varsa içeriği okur.
#-"a": (append) ekleme modu. Dosya yoksa oluşturur, varsa iç
#-"x": (exclusive creation) oluşturma modu. Dosya yoksa oluşturur, varsa hata verir.
#-"r+": (read and write) okuma ve yazma modu. Dosya yoksa hata verir, varsa içeriği okur ve üzerine yazabilir.
#-Dosya açarken encoding parametresi ile karakter kodlamasını belirtebilirsiniz. Örneğin, Türkçe karakterler için "utf-8" kullanabilirsiniz.
#-r+ da seak yapmazsanız dosya başından okumaya başlarsınız ve yazarken de baştan yazarsınız. Bu da mevcut içeriği siler. 
#O yüzden r+ modunda seak yaparak imleci dosyanın sonuna getirirseniz, ekleme yapabilirsiniz.

"""
file =open("dosya_islemleri/deneme.py","w")
file.close"""

"""file =open("dosya_islemleri/deneme.py","r")
file.read
file.close"""

"""file =open("dosya_islemleri/deneme.txt","a",encoding='utf-8')
file.write("\nmerhabalar la gardeş")
file.close

"""

file =open("dosya_islemleri/deneme.txt","r",encoding='utf-8')

"""relaud=file.read()
print("1.okuma")
print(relaud)
#close edilmediği için okumam yani imleç sonda oldugu için okunacak dosya bulamıyor 
relaud1=file.read
print("2.okuma")
print(relaud1)

file.close


"""
"""
cikti =file.read(2)
cikti2 =file.read(4)
cikti3 =file.read(5)
print(cikti)
print(cikti2)
print(cikti3)
file.close"""

"""
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
"""
print(file.readlines())