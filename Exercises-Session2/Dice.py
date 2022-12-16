import random

ans=1
while ans==1:
    s=input("Do you want to start?(y/n) ")
    if s=="y":
        Dice=random.randint(1,6)
        print(Dice)
    else:
        print("have a good day   Bye... ")
        ans=2
    if Dice == 6:
        print("You won\nYou can Roll again :) ")
    else:
        print("Bye")
        ans=2
   