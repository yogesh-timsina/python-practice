f=open('myfile2.txt',)
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()