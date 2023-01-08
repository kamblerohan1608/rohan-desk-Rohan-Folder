
#
'''
n=0
for i in range(10):
    a=int(input("Enter the number : "))
    n=n+a
print("The average is ", n)

#prime number between two numbers defined by user:

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
n=a
for i in range(a,b+1):
    k=0
    for j in range(2,b+1):
        if i%j==0:
            k=k+1
        if ((j==b) and (k==1)):
            print(i,"is a prime number.")
        #else:
         #   print(j,"is not a prime number.")


n=5
for row in range(n):
    for col in range(row+1):
        print("*",end=" ")
    for col1 in range(n-row-1):
        print(" ",end=" ")
    for col2 in range(n-row-2):
        print(" ",end=" ")
    for col3 in range(row+1):
        if col3<4:
            print("*",end=" ")
        
    print()
for row1 in range(row):
    for col4 in range(row-row1):
        print("*",end=" ")
    for col5 in range(row1+1):
        print(" ",end=" ")
    for col6 in range(row1):
        print(" ",end=" ")
    for col7 in range(row-row1):
        print("*",end=" ")
    print()
'''



