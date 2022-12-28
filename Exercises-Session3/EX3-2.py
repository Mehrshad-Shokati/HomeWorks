import numpy as np

m =int(input("Enter the row: "))
n =int(input("Enter the colomn: "))
 

x = np.full((m,n), "⬜")
 
x[1::2, ::2] = "⬛"
x[::2, 1::2] = "⬛"

for i in range(m):
    for j in range(n):
        print(x[i][j], end='')
    print()
    

 