class Product:
    def __init__(self,name,price):
        self.name =name
        self.price = price  # setter'ı çağırır ve kontrol yapar
    
    @property
    def price(self):
        return self._price
    
    #deger atamak için kullanıyoruz 
    @price.setter
    def price(self,value):
        if value >= 0:
            self._price =value
        else:
            raise ValueError("ürün fiyatı için negatif deger ataması yapılamaz")

p = Product("iphone16",80000)

print(p.price)

p.price = 30000

print(p.price)

