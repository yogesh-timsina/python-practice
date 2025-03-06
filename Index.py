try:
    lst=[1,5,6,3]
    print(lst[5])
except IndexError as e:
    print("There occur ",e)