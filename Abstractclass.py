from abc import ABC , abstractmethod
class ParentClass:
    @abstractmethod
    def display(self):
        print("This is the parent class method.Which need the abstract method declaration as well as concrete class.")
    def show(self):
        print("This is the concrete method without defining the abstract method")
class ChildClass(ParentClass):
    def display(self):
        print("This is the child class method display")
    def show(self):
        print("This is the Child class method show")
obj=ChildClass()
obj.display()
obj.show()