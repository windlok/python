print("--- iterator örneği ---")
list =[1,2,3,4,5]

#list bir iterable'dır, yani üzerinde dolaşılabilir bir yapıdır. Bu nedenle, list üzerinde bir for döngüsü kullanarak her bir elemanı tek tek yazdırabiliriz.
for i in list:
    print(i)

print("\n--- Iterator Kullanımı ---")

iterator = iter(list)  # list üzerinde bir iterator oluşturuyoruz
print(next(iterator))  # iterator'ın ilk elemanını yazdırır (1)
print(next(iterator))  # iterator'ın ikinci elemanını yazdırır (2)
print(next(iterator))  # iterator'ın üçüncü elemanını yazdırır (3)
print(next(iterator))  # iterator'ın dördüncü elemanını yazdırır (4)
print(next(iterator))  # iterator'ın beşinci elemanını yazdırır (5)
# print(next(iterator))  # iterator'ın altıncı elemanını yazdırmaya çalışır, ancak StopIteration hatası verir çünkü artık eleman kalmamıştır.

print("\n--- Iterator ile Döngü ---")

iterator2 = iter(list)  # list üzerinde yeni bir iterator oluşturuyoruz
while True:
    try:
        print(next(iterator2))  # iterator'ın bir sonraki elemanını yazdırır
    except StopIteration:  # iterator'ın elemanları bittiğinde StopIteration hatası yakalanır
        break  # döngüyü sonlandırır

print("\n--- Kendi Iterator Sınıfımız ---")
class myNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            num = self.start
            self.start += 1
            return num
        else:
            raise StopIteration
        
myNumbersIterator = myNumbers(1, 6)  # 1'den başlayarak 5'e kadar sayıları üreten bir iterator oluşturuyoruz
for num in myNumbersIterator:  # myNumbersIterator üzerinde bir for döngüsü kullanarak her bir sayıyı yazdırır
    print(num)    

print("\n--- Kendi Iterator Sınıfımız ile Döngü ---")
myNumbersIterator = myNumbers(1, 6)  # 1'den başlayarak 5'e kadar sayıları üreten yeni bir iterator oluşturuyoruz

while True:
    try:
        print(next(myNumbersIterator))  # myNumbersIterator'ın bir sonraki sayısını yazdırır
    except StopIteration:  # myNumbersIterator'ın sayıları bittiğinde StopIteration hatası yakalanır
        break  # döngüyü sonlandırır    