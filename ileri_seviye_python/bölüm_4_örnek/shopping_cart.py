class ShoppingCart():
    def __init__(self):
        self.item=[]

    def add_item(self,veri):
        self.item.append(veri) 


    def display_items(self):
        [print(f'gelen veriler : {i}') for i in self.item]

    def calculator_totals(self):
        print(f'toplam uzunluk: {len(self.item)}')   

veri = ["merhaba dünya","naber la"]
veri1 = ["dasdasdasdads"]
veri2=[" "]
shop = ShoppingCart()
shop.add_item(veri)
shop.add_item(veri1)

shop.calculator_totals()

shop.display_items()



class ShoppingCart1():
    def __init__(self,file):
        self.file = file.copy()

    def add_items(self,item):
        self.file.append(item)

    def display_items(self):
        for i in self.file:
            print(f'gelen veriler : {i}')

    def total_veri(self):
        print(f'toplam veri girişi: {len(self.file)}')

sc = ShoppingCart1([veri,veri1])  
sc.add_items(veri2)

sc.display_items()
sc.total_veri()