import pyfiglet
count = 0

def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print() 

def check_p1():
    F =print ("Player 1  is  Winner")

    if( game_board[0][0]==" X " and game_board[0][1]==" X " and game_board[0][2]==" X "):
        print (p1)

    elif(game_board[1][0]==" X " and game_board[1][1]==" X " and game_board[1][2]==" X "):
        print (p1)

    elif(game_board[2][0]==" X " and game_board[2][1]==" X " and game_board[2][2]==" X "):
        print (p1)

    elif(game_board[2][0]==" X " and game_board[1][1]==" X " and game_board[0][2]==" X "):
        print (p1)

    elif(game_board[0][0]==" X " and game_board[1][1]==" X " and game_board[2][2]==" X "):
        print (p1)

    elif(game_board[0][0]==" X " and game_board[1][0]==" X " and game_board[2][0]==" X "):
        print (p1)

    elif(game_board[0][1]==" X " and game_board[1][1]==" X " and game_board[2][1]==" X "):
        print (p1)

    elif(game_board[0][2]==" X " and game_board[1][2]==" X " and game_board[2][2]==" X "):
        print (p1)



def check_p2():
    p2 =print ("Player 2  is  Winner")

    if( game_board[0][0]==" O " and game_board[0][1]==" O " and game_board[0][2]==" O "):
        print (p2)

    elif(game_board[1][0]==" O " and game_board[1][1]==" O " and game_board[1][2]==" O "):
        print (p2)

    elif(game_board[2][0]==" O " and game_board[2][1]==" O " and game_board[2][2]==" O "):
        print (p2)

    elif(game_board[2][0]==" O " and game_board[1][1]==" O " and game_board[0][2]==" O "):
        print (p2)

    elif(game_board[0][0]==" O " and game_board[1][1]==" O " and game_board[2][2]==" O "):
        print (p2)

    elif(game_board[0][0]==" O " and game_board[1][0]==" O " and game_board[2][0]==" O "):
        print (p2)

    elif(game_board[0][1]==" O " and game_board[1][1]==" O " and game_board[2][1]==" O "):
        print (p2)

    elif(game_board[0][2]==" O " and game_board[1][2]==" O " and game_board[2][2]==" O "):
        print (p2)
      

game = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print (game)

game_board = [[" - ", " - ", " - "],
               [" - ", " - ", " - "],
               [" - ", " - ", " - "]] 

show()

while True :

    print("player 1")
    while True:
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        if 0 <= row <=2 and 0 <= col <= 2 :
        
            if game_board[row][col] == " - ":
                game_board[row][col] =" X "
                count = count +1
                show()
                break
            else:
                print("Select other Cell...")
        else:
            print("Enter row and coloumn between 0 and 2")

        check_p1()
   


    print ("player2")
    while True:
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        if 0 <= row <=2 and 0 <= col <= 2 :        
            if game_board[row][col] == " - ":
                game_board[row][col] =" O "
                count = count +1
                show()
                break
            else:
                print("Select  other Cell...") 
        else:
            print("Enter row and coloumn between 0 and 2")

        check_p2()
    