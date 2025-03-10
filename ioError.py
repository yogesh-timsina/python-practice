try:
    with open('file.txt','r') as f:
        f.write("this file is just a example not created")
except IOError as e:
    print("Error:",e)