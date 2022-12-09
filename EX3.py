Name = input("Please enter your name: ")
Lname = input("Please enter your lastname: ")
Math = float(input("please enter your math Score: "))
Geography = float(input("please enter your geography Score: "))
Science = float(input("please enter your Science Score: "))
sum= Math+Geography+Science
ave=sum/3
print("\nYour name is:",Name)
print("\nYour lastname is:",Lname)
print("\nYour average is:",ave)

if ave >= 17:
    print("\nGreat")

if 12 <= ave < 17:
    print("\nNormal")

if ave < 12:
    print("\nFail")