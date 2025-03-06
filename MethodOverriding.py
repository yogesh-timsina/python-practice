class sum:
    def display(self,a,b):
        print("sum:",a+b)
class sub(sum):
    def display(self,a,b):
        print("sub:",a-b)
obj=sub()
obj.display(10,5)