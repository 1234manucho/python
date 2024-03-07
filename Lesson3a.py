# Relational apparators
# >-greater than,<-less thsn,!=-not equal to, ==-equal to, >=-greater than or equal to, <=-less than or equal to.


print(20>30)
print(60==30)
print(50!=70)
print(60>=40)

# Logical operators are used to combine multiple conditions together and express them as a single boolean operations they include: And, or and not
# AND: Any true value multiplied by a false value gives of a false value.
# OR: True or salse=true, true or true=true, false or false=false, 
# NOT : it gives the inverse of the correct output

Numb1=50
Numb2=70
logic=(Numb1<Numb2) and (Numb2>=Numb1)
print(logic)
logic2=(Numb1==Numb2) or (Numb1>Numb2)
print(logic2)
print(not Numb1>Numb2)

# control flow: IF, IF_ELSE, ELIF
# IF-works only on one true condition,IF_ELSE-Works  on one condition when True or False.,ELIF-Works mainly for multiple conditions(if-condition,elif-condition,elifcondition2....,)
# If condition: #body of if statement.

# if statement
number=20

if number<50:
    print("number is greater than 50")

if number!=0:
    print("20 is greater than zero")

if number>=70:
    print("number is viable")
if number>15:
    output=(number-10)
    print(output)
if number==20:
    summation=(number+50)
    print(summation)
if number<=50:
    print("viable to multiply by 70")
    out=(number*70)
    print(out)

# IF_ELSE Condition , IF conditon: #body statement ELSE : #body condition