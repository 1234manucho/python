# IF-ELIF-ELSE STATEMENT

Number=0

if Number>0: #condition 1
    print("positive number")
elif Number==0: #condition2
    print("Zero")
else:
    print("negative number") #last option

marks=float(input("enter your marks"))

if marks<30:
    print("BELOW AVERAGE")
elif marks>=30 and marks<40:
    print("AVERAGE")
elif marks>=40 and marks<70:
    print("ABOVE AVERAGE")
else:
    print("EXCELLENT")
    if marks==100:
        print("valedictorian")
    elif marks==0:
        print("repeat test")
    else:
        print("invalid input")
        



    




   

    
