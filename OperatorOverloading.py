class OperatorOverloading:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a+b.a
class OperatorOverloadingA:
    def __init__(self,a):
        self.a=a
obj=OperatorOverloading(10)
obj1=OperatorOverloadingA(20)
print(obj+obj1)