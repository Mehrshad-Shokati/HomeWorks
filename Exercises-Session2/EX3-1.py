a=int(input("enter the length of List: ")) 
p=[]
for i in range(a):
    s=int(input("Fill the List: "))
    p.append(s)
print("The orginal List is: ",p)

p=list(dict.fromkeys(p))
print(p)