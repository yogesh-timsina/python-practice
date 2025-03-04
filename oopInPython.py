class Animal:
    def eat(self):
        print("animal eat grass")

class Cow(Animal):
    def moo(self):
        print("cow moo")
class Buffalo (Animal):
    def bellow(self):
        print("buffalo bellow")
        
obj1=Cow()
obj1.eat()
obj1.moo()
obj2=Buffalo()
obj2.eat()
obj2.bellow()
