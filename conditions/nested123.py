
#Nested if

'''
#example 1

# Finding a number is positive negative or zero

a = int(input("Enter the number : "))
if (a > 0):
    print("Entered number is positive.")
elif (a < 0):
    print("Entered number is negative.")
else:
    print("Entered number is zero")


#Example 1 (using nested if)

a1=int(input("Enter the number : "))
if (a1>=0):
    if (a1>0):
        print(a1,"is a positive number.")
    else :
        print(a1,"is zero")
else:
    print(a1,"is negative number")
print("Program Finished.")


#Example 2 find greatest of 3 number entered by user.

a1=int(input("Enter first number : "))
a2=int(input("Enter secound number : "))
a3=int(input("Enter third number : "))
if (a1>a2) and (a1>a3):
    print(a1,"is greagter.")
elif (a2>a1) and (a2>a3):
    print(a2,"is greatrer.")
else:
    print(a3,"is greater.")
print("Program Finished.")


#Example 2 (using nested if)


a1=int(input("Enter first number : "))
a2=int(input("Enter secound number : "))
a3=int(input("Enter third number : "))
if (a1>a2):
    if(a1>a3):
        print(a1,"is greater.")
    else:
        print(a3,"is grester.")
else:
    if(a2>a1) and (a2>a3):
        print(a2,"is greater.")
    else:
        print(a3,"is greater.")
'''
# self

#Example 2.

a1=int(input("Enter first number : "))
a2=int(input("Enter secound number : "))
a3=int(input("Enter third number : "))
if(a1>a3) and (a2>a3):
    if (a1>a2):
        print(a1,"is greater")
    else :
        print(a2,"is greater")
elif (a2>a1) and (a3>a1):
    if (a2>a3):
        print(a2,"is greater.")
    else:
        print(a3,"is greater.")
elif (a1>a2) and (a3>a2):
    if (a1 > a3):
        print(a1,"is greater.")
    else :
        print(a3,"is greater.")






















