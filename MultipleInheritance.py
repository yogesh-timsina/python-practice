class ParentClass1:
    def display(self):
        print("This is the method of ParentClass1")
class ParentClass2:
    def Show(self):
        print("This is the method of ParentClass2")
class ChildClass(ParentClass1,ParentClass2):
    def displayMethod(self):
        print("This is the method of ChildClass")
        print("From this class we are going to access the property of parent classes")
Obj=ChildClass()
Obj.display()
Obj.Show()
Obj.displayMethod()