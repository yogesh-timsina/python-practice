from functools import reduce
lst=[1,2,5,6,7,8]
sum=reduce(lambda a,b:a+b,lst)
print(sum)