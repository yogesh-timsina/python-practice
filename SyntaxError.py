try:
    exec("x===10")
except SyntaxError as e:
    print("Error:",e)