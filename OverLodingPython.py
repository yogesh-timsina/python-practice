class Addition:
    def add(self,*args):
        return sum(args)
obj=Addition()
res1=obj.add(5,3)
res2=obj.add(3,5,8)
print("sum:",res1)
print("sum:",res2)