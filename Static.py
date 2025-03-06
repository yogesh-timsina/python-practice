class StaticMethod:
    @staticmethod
    def display(name,age):
        n=name
        a=age
        print("Name:",n,"Age:",a)
obj=StaticMethod()
StaticMethod.display("yogesh",20)