try:
    lst=[1,2,3,4]
    print(lst[5])
except IndexError as e:
    print("The error occur:",e)