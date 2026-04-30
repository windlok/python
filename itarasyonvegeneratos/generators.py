def cube():
    for i in range(500):
        #yer tutucu olarak kullanılır, fonksiyonun çalışmasını durdurur ve bir değer döndürür
        #bir yerde tutulmazsa, fonksiyonun çalışması devam eder ve sonraki değeri döndürür
        #ramde yer tutar, ancak tüm değerler bellekte tutulmaz, sadece o anki değer tutulur
        #performans açısından avantaj sağlar, çünkü tüm değerler bellekte tutulmaz, sadece o anki değer tutulur
        yield i ** 3

kupler = cube()
# print(next(kupler))  # 0
# print(next(kupler))  # 1
# print(next(kupler))  # 8
# print(next(kupler))  # 27
# print(next(kupler))  # 64
#next() fonksiyonu, generator'ın bir sonraki değerini döndürür. Eğer generator'ın sonuna gelinmişse, StopIteration hatası verir.

#her seferinde generator'ın bir sonraki değerini döndürür, ancak generator'ın sonuna gelinmişse, StopIteration hatası verir.
# iterator = iter(kupler)

# print(next(iterator))  # StopIteration hatası verir, çünkü generator'ın sonuna gelinmişti.

for k in kupler:
    print(k)  # 0, 1, 8, 27, 64, ... 124999000000

#comprehension ile generator oluşturmak
#neden comprehension ile generator oluşturmak daha avantajlıdır?
#comprehension ile generator oluşturmak daha avantajlıdır, çünkü comprehension ile generator oluşturmak daha okunabilir ve daha az kod yazmanızı sağlar. Ayrıca, comprehension ile generator oluşturmak daha performanslıdır, çünkü comprehension ile generator oluşturmak daha az bellek kullanır, çünkü tüm değerler bellekte tutulmaz, sadece o anki değer tutulur.

generator = [i ** 3 for i in range(500)]
print(generator)  # [0, 1, 8, 27, 64, ... 124999000000]

for g in generator:
    print(g)  # 0, 1, 8, 27, 64, ... 124999000000