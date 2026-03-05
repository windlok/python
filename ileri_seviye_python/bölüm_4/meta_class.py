class Meta(type):
    def __init__(self, class_name, bases, attrs):
        print(attrs)

        return type(class_name,bases,attrs)
    

class Person(metaclass=Meta):
    name = "Ali"
    surname = "Veli"
    age = 30

    def hello(self):
        print("Hello")



p = Person()        