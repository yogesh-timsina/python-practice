class superclass:
    def display(self):
        print("This is the super class method")
class subclass(superclass):
    def show(self):
        print("This is the sub class Method")
Obj=subclass()
Obj.display()
Obj.show()