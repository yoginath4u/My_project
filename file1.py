
f=open("loop.py","r")
f1=open("mydata.txt","w")
print(f.readlines)

for data in f:
    f1.writelines(data)

