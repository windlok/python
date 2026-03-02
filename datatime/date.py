from datetime import datetime, time, timedelta

result = dir(datetime)
print(result)

simdi = datetime.now()
print(simdi)

now = datetime.now()

print(now)

result0 =datetime.ctime(now)
print(result0)
result1 = datetime.strftime(now,'%y')
result2 = datetime.strftime(now,'%X')
result3 = datetime.strftime(now,'%a')
print(result1)
print(result2)
print(result3)


t='21 nisan 2020'

#t.split() ile t stringini boşluklardan bölerek bir liste oluştururuz. Oluşan listenin elemanlarını sırasıyla gun,ay,yil değişkenlerine atarız.
gun,ay,yil = t.split()
print(gun)
print(ay)
print(yil)

t ='15 april 2013 hour 12:45:30'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)

birthday = datetime(1990, 5, 17)
result = datetime.timestamp(birthday) #datetime nesnesini timestamp'e çevirir. Timestamp, 1 Ocak 1970'ten itibaren geçen saniye sayısını temsil eder.
result = datetime.fromtimestamp(result) #timestamp'i datetime nesnesine çevirir. Timestamp, 1 Ocak 1970'ten itibaren geçen saniye sayısını temsil eder.



result0 = simdi - timedelta(days=7) #simdi değişkeninden 7 gün çıkararak yeni bir datetime nesnesi oluşturur. timedelta(days=7) ifadesi, 7 günlük bir zaman farkını temsil eder. Bu işlem sonucunda, simdi değişkeninin 7 gün öncesine ait bir datetime nesnesi elde edilir.
print(result0)