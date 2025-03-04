#what is python?/single comment
'''python is an programming language
it is open source
easy to learn and use language
cross plartform
python is an object oriented programming language(hamro real world entity lai programming term baata implementation)
python is an interpreted language
'''#multi line comment
#what is token?
''' token is an smallest unit of programming language python
* keyword
* identifiers
* constant/literals
* operators
* function

'''
"""hellon suvam
how are you?"""
#variable is the container that holds the data or value
#Arithmetic operator(+,-,*,/,%)
'''a=10
b=20
sum=a+b
print(sum)
print("The sum of a and b is:",sum)

sub=b-a
print(sub)
print("the sub of b and a is:",sub)'''

#Assignment operator(=,+=,-=,*=,/=,%=)
"""a=10
b=20
print(a)
a+=b
print(a)
"""
#comparision operator(==,<=,>=,!=,<,>)
"""a=10
b=30
print("a is equal to b:",a==b)#false
print("a is less than b:",a<b)#true"""
#logical operator(and ,or,not)
"""
a=10
b=30
c= (a<b) and (b>a)
print(c)
c=(a<=b) or (b<a)
print(c)
c=not(a==b)
print(c)"""


#bitwise Operator(&(and),|(or),^(xor),~(not like),>>(bitwise right),<<(bitwise left))
'''
a=7
print("left shift: ",a<<2) '''
#64 32 16 8 4 2 1

#identity operator(is, is not,==,!=)
'''
a=10
b=20
c=a
print("a is c:",a is c)#true
print("a is not c:",a is not c)#false
print("a==b:",a==b)#false
print("a!=b",a!=b)#true'''

#what is constant?
"""constant is a special type of variable whose value cannot be changed
"""
# id(),type(),getsizeof() functions
'''
a=10
print(type(a))
print(id(a))
from sys import*
print(getsizeof(a))
'''
'''
for num in range(1,11):
    if num==5:
        break
    print(num)'''
'''
name={"name":"yogesh","age":19}
print(name)'''

#function
'''function is nothing but group of statements which only executes when we call them'''
#benefits of function
'''1.provide modularity 2. offer reusable code 3.debugging is easy '''
#types of function
"""1.Build in function(predefine function/library function) 2.user define function"""

#syntax def function_name(self)
            #code

'''def Function():
    print("hello shubham")
Function()
def sum():
    a=int(input("enter the number1:"))
    b=int(input("Enter the number2:"))
    c=a+b
    print(f"The sum of {a} and {b} is:",c)
sum()'''
#passing Arguments:
'''
def sum(a,b):
   
    c=a + b
    print("The sum of a and b:",c)
sum(30,40)'''
#passing user argument
'''
def sum(a,b):
    c=a+b
    print(f"the sum of the {a} and {b} is:",c)
num1=int(input("Enter the first digit to check:"))
num2=int(input("Enter the second digit to check:"))
sum(num1,num2)'''
#default parameter
'''
def sum(a,b=10):
   
    c=a + b
    print("The sum of a and b:",c)
sum(10)
sum(30,40)'''
#return values:
'''
def display(a,b):
    return a*b
c=display(2,4)#object
print("the multiplication of 2 digits are : ",c)
'''
#pass function as a parameter
'''def display(sum):
    print("this is function:",sum())
def sum():
    return "shuvam basu"
display(sum)'''
#Nesting of function
'''
def display():
    def display2():
        print("this is inner function of display")
    display2()
    print("this is outer function display")
display()'''
#variable length argument
'''
def display(a,*vartup):
    print(a)
    for i in vartup:
        print(i)
display(10,11,23,12)   
'''
#Control statement
#if  else  elif statement
'''
a=80
if (a<=18):
    print("you are young kid")
elif(a<15):
    print("saanu bachcha")
elif(a>60):
    print("budho manxe")
else:
    print("xito mar")'''
#Nested if else statement
'''
age=int(input("Enter the age of the Your parent:"))
gender=input("Enter the gender of your parent:")
if age>=60:
    print("Ohh Noo ,your parents are too old")
    if gender=="male":
        print("Your parent gender is male")
    else:
        print("your parent is female")
else:
    print("your parent is too young for our survey")'''
#conditional operator(ternary operator)three operand are required 
'''
a=int(input("enter any number to generate:"))
b=int(input("Enter second number to generate:"))
c=int(input("enter third number generate:"))
largest=f"{a} is greater than {b} and {c}"if(a>b) and (a>c) else f"{b} is greater than {a} and {c}"if(b>c) else f"{c} is greater than {a} and {b}"
print(largest)'''
#looping 
#for loop
'''for i in range(1,11):
    print(i)'''
#while loop
'''i=1
while i<=10:
    print(i)
    i=i+1
    '''
#fibonanci series
'''
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the position (n): "))
print(f"Fibonacci number at position {num} is {fibonacci(num)}")
'''
#directory
"""
a={'name':"yogesh",'Address':"panchthar",'age':16}
print(a['name'])"""
#list & list using loop
'''namelist=["yogesh","bim","bhaktapur",19,4.0]
for i in range(1,3):
    print(namelist[i])'''
#list function
'''namelist=["yogesh","bim","bhaktapur",19,4.0]
a=namelist.reverse
print(a)'''
#slicing & indexing
'''
N="Hello yogesh"
l=len(N)
print(l)#12
print(N[1])#e
print(N[0:6])#Hello
print(N[:8])#Hello yo
print(N[0::2])#Hloygs
print(N[-1::-2])#heo le
print(N[-7::3])# gh
print(N[-7:-3])# yog
print(N[::-1])#hsegoy olleH
'''
#list comprihension
'''mark=[40,50,60,70]
print(mark)
newMark=[i+2 for i in mark]
print(newMark)#42,52,62,72
'''
#Build in string function
'''
name='yOgesh tims'
N='Hello Nisha'
print("upper case:",name.upper())
print("lower case:",name.lower())
print("Capitalize:",name.capitalize())
print("title case:",name.title())
print("split case:",name.split())
print("compare:",name==N)'''
