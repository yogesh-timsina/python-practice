try:
    f=open("c:\\Mytext\\create.txt","r")
except FileNotFoundError as e:
    print("Error:",e)