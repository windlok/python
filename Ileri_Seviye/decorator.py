#decorator nedir?
##Decorator, bir fonksiyonun davranışını değiştirmek veya genişletmek için kullanılan bir yapıdır.
##Decorator'lar, bir fonksiyonun öncesinde veya sonrasında ek işlemler yapmak için kullanılır. Bu, kodun daha temiz ve modüler olmasını sağlar.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    print("Hello!")