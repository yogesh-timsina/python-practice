try:
    a=[1]*(10**10)
except MemoryError as e:
    print("Error :",e)