a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

checkLargest=f"{a} is greater than {b} and {c}"if(a>b) and (a>c) else f"{b} is greater than {a} and {c}"if b>c else f"{c} is greater than {a} and {b}"
print(checkLargest)