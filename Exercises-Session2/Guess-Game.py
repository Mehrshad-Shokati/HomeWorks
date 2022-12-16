import random
T=1
S=1
pc_number = random.randint(0,20)
for i in range(5):
    user = int(input("please enter a number: "))

    if pc_number == user:
        print("you WON :))) ")
        sum=S-T
        if   i==0 and sum==0:
            print("You are a Master:)")
        elif i==1 and sum==0:
            print("You are a Genius")    
        elif i==2 and sum==0:
            print("You are  Smart")
        elif i==3 and sum==0:
            print("Good")
        elif i==4 and sum==0:
            print("Not Bad")
       
        break
    elif pc_number > user:
        print("Go upper:/")
        sum = S+T
    elif pc_number < user:
        print("Go Downer:/")
        sum = S+T
print("the Correct number : ", pc_number)
print("Your number of attempts: ",i+1)
if i==4 and sum==2:
    print("It's okay, try again :(")
