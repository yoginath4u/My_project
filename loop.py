
num=1
while num<=10:
    print(num)
    num+=1


num=1
while num<=10:
    if num==5:
        print(num)
    num+=1


num=1
while num<=10:
    if num<=5:
        num+=1
        continue
    print(num)
    num+=1

for i in range(1,10,2):
    print(i)

name="yoginath"
for i in name:
    print(i)
print("hello")