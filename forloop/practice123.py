'''
#for loop practice

a=int(input("Enter the number : "))
for i in range(1,a + 1):
    print(i)


# Pattern :

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


a=int(input("Enter the size of pattern : "))
#a=5
for i in range(a+1):
    for j in range(i):
        print("*",end=' ')
    print('')




# Pattern :

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5



a=int(input("Enter the number : "))
for i in range(a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print('')
''' 
n=5
for row in range(0,n):
    for col3 in range(0,row+1):
        if col3<4:
            print("*",end=" ")
    print()




















