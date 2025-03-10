try:
    lst=[1,3,6,6]
    lst.append(4)
    lst.push(5)
except AttributeError as e:
    print("There Occur Error:",e)