class GrandParent:
    a=10
    b=5
    def sum(self):
        c=self.a+self.b
        print("This is GrandParent Class")
        print("sum:",c)
class Parent(GrandParent):
    def sub(self):
        c=self.a-self.b
        print("This is the  Parent class Method")
        print("Sub is:",c)
class Child(Parent):
    def prod(self):
        c=self.a*self.b
        print("This is the child class method")
        print("prod :",c)
obj=Child()
obj.sum()
obj.sub()
obj.prod()