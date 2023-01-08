
'''
# 1. write a program taking 3 inputs from user and find out smallest.

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
if (a < b):
    if (a < c):
        print(a,"is the smallest.")
    else:
        print(c,"is smallest.")
else :
    if (b < c):
        print(b,"is smallest.")
    else:
        print(c,"is smallest.")
print("Program Finished.")


# 2. Write a program taking 4 inputs from user and find the greatet of them.

# Method 1

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
d=int(input("Enter the number : "))

if(a > b):
    if(a > c):
        if(a > d):
            print(a,"is greatest.")
        else:
            print(d,"is greatest.")
elif(b > c):
    if(b > a):
        if(b > d):
            print(b,"is greatest.")
        else:
            print(d,"is greatest.")
elif(c > d):
    if(c > a):
         if(c > b):
             print(c,"is greatest.")
         else:
            print(b,"is greatest.")
else:
    print(d,"is greatest.")
print("Program finished.")



# Method 2 :

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
d=int(input("Enter the number : "))

if (a > b) and (a > c):
    if (a > d):
        print(a,"is greater.")
    else:
        print(d,"is greater.")
elif (b>a) and (b>c):
    if (b>d):
        print(b,"is greater.")
    else:
        print(d,"is greater.")
elif (c>a) and (c>b):
    if (c>d):
        print(c,"is greater.")
    else:
        print(d,"is greater.")
else:
    print(d,"is greatest.")
print("Program Finished.")


'''

# Method 3

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
d=int(input("Enter the number : "))

if (a>b and a>c) and (a>d):
    print(a,"is greater.")
elif (b>a and b>c) and (b>d):
    print(b,"is greater.")
elif (c>a and c>b) and (c>d):
    print(c,"is greater.")
else:
    print(d,"is greatest.")
print("Program Finished.")

