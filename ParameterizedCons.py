class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print("Id of the student is:",self.id)
        print("Name of the student is:",self.name)
obj=Student(1,"Yogesh")
obj.display()
