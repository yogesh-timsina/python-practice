class Method:
    a=10
    b=20
    def sum(self):
        res=self.a+self.b
        print("sum of the nos:",res)
    def sub(self,a,b):
        print("sub:",a-b)
obj=Method()
obj.sum()
obj.sub(20,10)