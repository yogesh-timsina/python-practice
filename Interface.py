from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def show(self):
        pass
class Child(Parent):
    def display(self):
        print("This is display Method")
    def show(self):
        print("This is show Method")
obj=Child()
obj.display()
obj.show()