# Dictionary

Jane_doe={
    'Name' :'Sarah',
    'Age'  :'25',
    'Gender':'Female',
    'Address':'60050',
    'Favourite color':["Blue","Red"]

} 
print(Jane_doe)
print(Jane_doe['Gender'])
print(Jane_doe['Favourite color']) 
# adding national id field / append
Jane_doe["National id"]=101
print(Jane_doe)
Jane_doe["Marritial status"]="Single"
Jane_doe["Highschool"]="Chewoyet "
print(Jane_doe)
# changing the address/insert
Jane_doe['Address']=70060
print(Jane_doe)