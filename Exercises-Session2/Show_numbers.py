a=[]
x=1
while x==1:
    s=int(input("please enter a number: "))
    a.append(s)
    
    i=input("if you wanna exit enter E otherwise enter C : ")
    if i=="E":
        break
    elif i=="C":
        x=1
sum1=sum(a)
print("sum of your inputs is",sum1)