#inheritance(kalıtım): Miras alma 

#Person => name ,lastname ,age , eat() ,run() , drink()
#Student(Person),Teacher(Person)

#Animals => Dogs(Animals), Cat(Animals)

class Animals():
    def __init__(self,name,type):
        self.name=name
        self.type=type
        print("animals")

    def angre(self):
        print("the animals")

class Dogs(Animals):
    def __init__(self,name,type):
        Animals.__init__(self, name, type)
        print("hav hav")

a1=Animals('kedi','4 ayakli')
d2=Dogs("dog","2 bacakli")

a1.angre()
d2.angre()



