# Boolean:-it is a datya type that has two values:True or False.
# Python List:Python uses small  square brackets([]) to indicate a list.We use a comma(,) to separate two items. Mutability refers to data types that can be accessed and changed after they have been created and stored in memory.
# Append()-used to add value at the end of the list
# insert()-used to insert values in certain index
# pop()-to remove value in a cecrtain value
# remove()- to remove  

# boolean
is_name=True
is_admin=False

print(type(is_name))
print(type(is_admin))

# python lists
tai=['Natalie','Nelson','Levy','Sylvester','Paul']
print("This are tai students:",tai)
print(type(tai))
print(tai[0])
print(tai[1:4])
print(tai[3:5])
# in a list, values are arranged in index that is from index 0 to the number of values in the given list

# append
tai.append('Alphonce')
print('Alphonce  has been updated',tai )

tai.append('Rayan')
print('Rayan has also been added',tai)

# insert
tai.insert(3,'Caleb')
print(tai)

tai.insert(5,'Simon')
print(tai)

# nested list
tai_age=['Natalie','Nelsonm',[25,26],'Levy',[15],'Caleb',[19]]
print(tai_age)

# reversed
print(tai[::-1])
print(tai[:-1])
name=['chills','brio','babz','shiru','bro','doc']
print(name)
# Tuple: it is the opposite of a list, it can not change it used paranthesis() unlike list which uses square brackets[]
