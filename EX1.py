#Mehrshad Shokati's Calculator:
import math

a= float(input("Please enter a number: "))

print("Please choose your operation:\n if your operation doesn't exist please enter 7 for more operations:\n1 for Cos\n2 for Sin\n3 for Factorial\n4 for Tan\n5 for Cot\n6 for Radical")

op= int(input("Operation type= "))

b= math.radians(a) 

if op == 1:
   
    result = math.cos(b)

if op == 2:
    result = math.sin(b)

if op == 3:
    result = math.gamma(a+1)

if op == 4:
    result = math.tan(b)

if op == 5:
    result = 1/(math.tan(b))

if op == 6:
    result = math.sqrt(a)

if op == 7:
    c = float(input("Please enter your second number: "))
    print ("(+) for sum\n(-) for subtraction\n(*) for multiplication\n(/) for division")
    op2=input("Please enter your operation:")
    if op2 == "+":
        result = a+c
    if op2 == "-":
        result = a-c
    if op2 == "*":
        result = a*c
    if op2 == "/":
        result = a/c
    

print (result)
