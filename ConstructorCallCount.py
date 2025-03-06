class Demo:
    count=0
    def __init__(self):
        Demo.count=Demo.count+1
obj1=Demo()
obj2=Demo()
obj3=Demo()
obj4=Demo()
print("The number of Demo Constructor are:",Demo.count)