#close yapmanın kolay yolu kod bolugu bitince clsoe oluyor 
with open("dosya_islemleri/deneme.txt","r") as file:
    r=file.read(10)
    print(r)
    file.seek(0)
    r1=file.read(10)
    print(r1)

