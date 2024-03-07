fruits=['apple','banana','orange']
print(fruits)
print(type(fruits))
print(fruits[1])
# addition of grape to the list/insert
fruits.insert(3,'grapes')
print(fruits)

# tuples
colors=('red','green','blue')
print(colors[1])

# dictionaries
Ages={
    "Alice":"25" ,
    "Bob" : "30",
    'Charlie':"35"    

}
print(Ages)
Ages['David']=40
print(Ages)


# 5
tuple1=("orange",[10,20,30],(5,15,25))
print(tuple1)
print(tuple1[1][1])

# reverse the tuple
tuple1=(10,20,30,40,50)
print(tuple1[::-1])

# copy
tuple1=(11,22,33,44,55,66)
print(tuple1[3:5])

# nested tuple
tuple3=(11,[222,33],44,55)
print(tuple3)


# no 8
list1=[10,20,[300,400,[5000,6000],500],30,40]
list1[2][2].append(7000)
print(list1)
