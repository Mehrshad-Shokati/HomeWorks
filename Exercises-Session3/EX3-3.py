import math
print("Please Fill the coefficient (a & b & c) like this\n ax^2+bx+c")
def second_degree_equation():
    a=float(input("Enter the first coefficient (a): "))
    b=float(input("Enter the Second coefficient(b): "))
    c=float(input("Enter the constant(c): "))  
    
    d=b**2 - 4*a*c
    
    if d<0:
        print("No answer in real ")
    elif d==0:
        x=(-1*b + math.sqrt(d))/2*a
        print("Rout is ",x)
    else:
        print("delta is \n",d)
        x1=(-1*b + math.sqrt(d))/(2*a)
        x2=(-1*b - math.sqrt(d))/(2*a)
        print("x1 = ", x1 , "\nx2= ",x2)
    


second_degree_equation()




