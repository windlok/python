class Person:
    address = "no information"
#class attributes
#constructor(yapıcı method)
    def __init__(self,name,year):
        #object attributes
        self.name =name
        self.year=year
        print("init calisti")
    #instance methods 
    def intro(self):
        print(f"Hello I am {self.name}")

    def calculateAge(self,currentYear):
        return currentYear - self.year
p1 = Person("ali",1990)
p2=Person("mustafa",2002)

"""print(f'name: {p1.name} years: {p1.year} adress: {p1.address}')
print(f'name: {p2.name} years: {p2.year}')"""

p1.intro()
p2.intro()
print(f"{p1.name} is {p1.calculateAge(2026)} years old")
print(f"{p2.name} is {p2.calculateAge(2026)} years old")

class Circle:
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    #method
    def cevre_hesap(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesaplama(self):
        return self.pi * (self.yaricap**2)
    

c1=Circle()
c2=Circle(5)

print(c1.alan_hesaplama())
print(c2.cevre_hesap())
        