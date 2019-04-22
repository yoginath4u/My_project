
lst1=[1,2,3,4,5,'Six','Seven']

for data in lst1:
    print(data)

fruits1=['mango','banana','apple']
#append and insert method
fruits1.append('kiwi')# add the item at end
fruits1.insert(0,'graps')#add the item at specific position,here zero position
print(f"Fruits:{fruits1}")

names=['yogi','sunil','ravi']
print(f"Names:{names}")

mix=fruits1+names   #concat 2 list using + operator
print(f"Mix:{mix}") 

college=['HNCC','BIGCE']

#extend method
college.extend(names)#extend the college list with names list values.
print(college)

#pop method
names.pop(1)#pass the index to be delete
print(names)

#del operator
del fruits1[1]
print(fruits1)

#remove method
mix.remove('yogi')
print(mix)

#append,insert,extend methos to add the values to thr list
#pop,del and remove to remove the items from list

#create the list using range function
numbers=list(range(1,10))
print(numbers)