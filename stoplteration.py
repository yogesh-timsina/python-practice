try:
    my_iter=iter([1,2,3])
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
except StopIteration as e:
    print("error:",e)
    