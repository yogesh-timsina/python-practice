try:
    import math
    result=math.exp(1000)
except OverflowError as e:
    print("Error:",e)