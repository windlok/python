x="global x"

def fonksiyon():
    x="local x"
    print(x)

fonksiyon()
print(x)
print("***********************")

#def içinde x değişkeni tanımlanmazsa fonksiyon global x değişkenini kullanır.
x="global x"
def fonksiyon():
    #x="local x"
    print(x)

fonksiyon()
print(x)

print("***********************")
x="global x"
#global anahtar kelimesi ile global değişkeni fonksiyon içerisinde değiştirebiliriz.
def fonksiyon():
    global x
    x="local x"
    print(x)

fonksiyon()
print(x)