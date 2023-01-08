
#calculator

print()
print()
print("*******************calculator**********************")
print()
print("Choose the option")
print()
print("1 - Addition")
print("2 - Substraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Percentage")
print("6 - Factorial")
print("7 - Exit")
print()

while True:
    print()
    ch=int(input("Enter your choice : "))
    

    if ch==1:
        a=int(input("Enter the first number for Addition : "))
        b=int(input("Enter the secound number for Addition : "))
        print("Addition is : " + str(a+b))
        
    elif ch==2:
        a=int(input("Enter the first number for Substraction : "))
        b=int(input("Enter the secound number for Substraction : "))
        print("Substraction is : " + str(a-b))
        
    elif ch==3:
        a=int(input("Enter the first number for Multiplication : "))
        b=int(input("Enter the secound number for Multiplication : "))
        print("Multiplication is : " + str(a*b))
        
    elif ch==4:
        a=int(input("Enter the first number for Division : "))
        b=int(input("Enter the secound number for Division : "))
        print("Division is : " + str(a/b))
        
    elif ch==5:
        total=int(input("Enter total marks : "))
        obt=int(input("Enter the otained marks : "))
        if obt>total:
            total,obt=obt,total
        print("The percentages are " + str((obt*100)/total))
        
    elif ch==6:
        fact=1
        a=int(input("Enter the number for factorial : "))
        for i in range(a,0,-1):
            fact=fact*i
        print("factorial of " + str(a) + " is " + str(fact))
    elif ch==7:
        print("**************************Thank you***********************************")
        break
    else:
        print("************************Invalid option********************************")
        print()
        print("************************Kindly try again******************************")


