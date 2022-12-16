print("Please enter The length of the three sides of the triangle")
a=float(input("First side: "))
b=float(input("Second side: "))
c=float(input("Third side: "))

if c>=(a+b):
    print("invalid")
elif a>=(b+c):
    print("invalid")
elif b>=(a+c):
    print("invalid")
else:
    print("Correct")