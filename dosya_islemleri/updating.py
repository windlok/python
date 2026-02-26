#direkt belirtec nerede ise oradan devam eder.
# with open("dosya_islemleri/deneme.txt","r+",encoding='utf-8') as file:
#     file.seek(5)
#     file.write("deneme")

# with open("dosya_islemleri/deneme.txt","r+",encoding='utf-8') as file:
#     print(file.read())

#------sayfa sonunda güncelleme---------------
#with open("dosya_islemleri/deneme.txt","a",encoding='utf-8') as file:
#    file.write("\nmustafa taştay")

#------sayfa basında güncelleme---------------
# with open("dosya_islemleri/deneme.txt","r+",encoding='utf-8') as file:
#     content = file.read()
#     content ="\nwindlok" + content 
#     file.seek(0)
#     file.write(content)


#------sayfa basında güncelleme---------------

# with open("dosya_islemleri/deneme.txt","r+",encoding='utf-8') as file:
#     liste = file.readlines()
#     liste.insert(1,"ali korkmaz\n")
#     file.seek(0)
#     #bunu böylede yapabiliriz ama daha kolay yolu var 
#     # for i in liste:
#     #     file.write(i)
#     #for kullanmak yerine bunu kullanabiliriz 
#     file.writelines(liste)


with open("dosya_islemleri/deneme.txt","r",encoding='utf-8') as file:
    print(file.read())