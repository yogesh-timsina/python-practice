class Methodoverloading:
    def sum(self,a,b):
        res=a+b
        print("The sum of two number is:",res)
    def sum(self,a,b,c=0):
        res=a+b+c
        print("The sum of Three number is:",res)
obj=Methodoverloading()
obj.sum(10,2,40)
obj.sum(10,20)