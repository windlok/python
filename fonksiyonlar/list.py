#her yaptıgımız işlemi tek satırda yapabiliriz.
#buradaki amac kısa ve uzun kod yazmak değil, daha okunabilir ve anlaşılır kod yazmaktır.
"""numbers =[]
for x in range(10):
    numbers.append(x)

print(numbers)


numbers =[x for x in range(10)]
print(numbers)

for x in range(10):
    print(x**2)


number =[x**2 for x in range(10)]
print(number)    

#burada naptık range(10) ile 0-9 arasındaki sayıları aldık ve x*x ile her bir sayının karesini aldık ve number listesine ekledik.
numbers =[x*x for x in range(10) if x%2==0] #sadece çift sayıların karesini alır.
print(numbers)
"""
"""
#aşağıdaki kodların ikiside aynı işlemi yapar ama ikinci kod daha kısa ve okunabilir.
myString = 'Hello, World!'
myList=[]
for letter in myString:
    myList.append(letter)
print(myList)

print('-------------------------------------------------------------------')

myList = [letter for letter in myString]
print(myList)"""

years = [1990, 1995, 2000, 2005, 2010]
ages=[2026-year for year in years]
print("yaslar")
print(ages)

result = [x if(x%2==0) else 'tek' for x in range(10)]
print(result)

#range kullanımı range(start, stop, step) şeklindedir. start: başlangıç değeri, stop: bitiş değeri, step: adım değeri.
#örneğin range(0, 10, 2) ifadesi 0, 2, 4, 6, 8 sayılarını üretir. range(1, 10, 2) ifadesi ise 1, 3, 5, 7, 9 sayılarını üretir. range(0, 10) ifadesi ise 0'dan başlayarak 9'a kadar olan sayıları üretir. range(10) ifadesi ise 0'dan başlayarak 9'a kadar olan sayıları üretir.
#range(10) ifadesi 0'dan başlayarak 9'a kadar olan sayıları üretir. range(0, 10) ifadesi ise 0'dan başlayarak 9'a kadar olan sayıları üretir. range(0, 10, 2) ifadesi ise 0, 2, 4, 6, 8 sayılarını üretir. range(1, 10, 2) ifadesi ise 1, 3, 5, 7, 9 sayılarını üretir.

#aşağıdaki kodların ikiside aynı işlemi yapar ama ikinci kod daha kısa ve okunabilir.
results =[]
for x in range(3):
    for y in range(3):
        results.append((x,y))
print(results)

numbers = [x*y for x in range(3) for y in range(3)]
print(numbers)