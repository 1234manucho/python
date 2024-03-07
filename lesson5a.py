#functions
def greet():
    print('hello world')

greet()
greet()
greet()

def add():
    num1=40
    num2=30
    total=num1+num2
    print(total)

add()

def minus():#user defined
    num4=45
    num3=60
    total2=num3-num4
    print(total2)

minus()
def mult():
    num5=45
    num6=45
    ttl=num5*num6
    print(ttl)

mult()

def div():
    num7=90
    num8=3
    y=num7/num8
    print(y)
div()
def modu():
    total3=20 % 3
    return total3
print(modu())

def exp():
   
    return 4**4
print(exp())
def modulus():
    total3=50 % 4
    return total3
print(modulus())
def exp2():
   
    return 5**5
print(exp2())

def addition(x,y):#x and y are parameters
    sum=x+y
    return sum
addition(30,50)#50 and 30 are arguements , 50 +30 is x and y
print(addition(30,50))



def multiply(one,two):
    return one*two
print(multiply(60,33))

def multiply(w,x,y):
    return w*x*y
print(multiply(60,33,90))

def chills(w,x,y):
    return w+x+y
print(chills(60,33,90))

def m(e,r,t):
    return e*r*t
print(m(70,337,970))

def greeting(name):
    print(f"hello {name},how are you?")#the f string is used to add variables or expressions inside a string
greeting("chills")
greeting("tim")
greeting("sarah")

def check(number):
    if number<=10:
        print("number is less than or equal to ten")
    else:
        print("number is more than ten")
check(1)
check(12)
#nested function
def outer_functiom():
    x=58
    def inner_function():
        print(x)   
    inner_function()
outer_functiom()
# MODULES
import math
def area(radius):
    return math.pi*radius**2
print(area(14))

print(math.sqrt(9))
print(math.sqrt(81))
print(math.log10(10))
print(math.factorial(9))

from math import log10
print(log10(20))
