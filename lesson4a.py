#For loop
for index in range(7):
    print(index)
for index2 in range(11):
    print(index2)
for index3 in range(2,11):
    print(index3)
for index4 in range(20,31):
    print(index4)

for even in range(2,11,2):
    print(even)
for odd in range(1,9,2):
    print(odd)

my_name='python'
for x in  my_name:
    print(x)
my_name='@poor millionaire'
for n in my_name:
    print(n)
cars=['mitsubishi','toyota','bmw','ferrari','footsubishi','fielder']
for y in cars:
    print(y)
names=('jane','manucho','tim','bro','nathe')
for t in names:
    print(t)
countries=['kenya','canada','usa','UG','TZ']
for e in countries:
    print(e)

fruits=['mango','apple','berries','banana']
for o in fruits:
    if o=="berries":
        break
    print(o)
for k in fruits:
    if k=='berries':
        continue
    print(k)
counties=('tl','ld','bg','kak','kisii')
for w in counties:
    if w=='kak':
        break
    print(w)
counties=('tl','ld','bg','kak','kisii')
for y in counties:
     if y=='kak':
          continue
     print(y)