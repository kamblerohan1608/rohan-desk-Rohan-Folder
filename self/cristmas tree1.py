
# #Cristmas tree structure 

n=int(input("Enter the no. of rows : "))
for row in range(0,n):
    for col in range(n-row+1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*", end=" ")
    for col2 in range(row):
        print("*",end=" ")
    print()

for row in range(0,n):
    for col in range(n-row):
        print(" ",end=" ")
    for col1 in range(row+2):
        print("*", end=" ")
    for col2 in range(row+1):
        print("*",end=" ")
    print()

for row in range(0,n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col1 in range(row+3):
        print("*", end=" ")
    for col2 in range(row+2):
        print("*",end=" ")
    print()

for row in range(0,n):
    for col in range(n):
        print(" ",end=" ")
    for col1 in range(3):
        print("*", end=" ")
    print()


n=int(input("Enter the number : "))
for row in range(0,n):
    for col in range(0,n-row+3):
        print(" ",end="")
    for col1 in range(0,row+1):
        print("* ",end="")
    print()
for row1 in range(n):
    for col2 in range(0,n-row1+1):
        print(" ",end="")
    for col3 in range(0,row1+3):
        print("* ",end="")
    print()
for row2 in range(0,n):
    for col4 in range(n-row2-1):
        print(" ",end="")
    for col5 in range(0,row2+5):
        print("* ",end="")
    print()
for row3 in range(n-3):
    for col6 in range(n+1):
        print(" ",end="")
    for col7 in range(3):
        print("* ",end="")
    print()

