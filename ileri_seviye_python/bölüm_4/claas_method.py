class CartItem():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #decorator kullanarak sınıf yöntemi tanımlama yapılmıştır.
    @classmethod
    def from_string(cls, string):
        name, price = string.split(",")
        return cls(name, float(price))
    

item1 = CartItem("Laptop", 1500)
print(item1.name)  # Output: Laptop

#Bu sınıf yöntemi, bir dize alır ve onu CartItem nesnesine dönüştürür. 
# Dize, ürün adını ve fiyatını virgülle ayrılmış olarak içermelidir. 
# from_string yöntemi, dizeyi parçalayarak adı ve fiyatı çıkarır ve ardından CartItem sınıfının bir örneğini oluşturur.
item2 = CartItem.from_string("Phone,800")
print(item2.name)  # Output: Phone