
#Example 1

#calculator (choose 1 for addition, choose 2 for substract)

print("Choose option from below :")
print("Press 1 - Addition")
print("Press 2 - Substraction")
print("Press 3 - Multiplication")
print("Press 4 - Division")
print("Press 5 - Percentage")

ch = int(input("Enter your choice : "))

if (ch == 1):
    a = int(input("Enter the first number for addition : "))
    b = int(input("Enter the secound number for addition : "))
    print("The addition is : ",a+b)
elif (ch == 2):
    a = int(input("Enter the first number for substraction: "))
    b = int(input("Enter the secound number for substraction: "))
    print("The substraction is : ",a-b)
elif (ch == 3):
    a = int(input("Enter the first number for multiplication : "))
    b = int(input("Enter the secound number for multiplication : "))
    print("The multiplication is : ",a*b)
elif (ch == 4):
    a = int(input("Enter the first number division : "))
    b = int(input("Enter the secound number division : "))
    print("The division is : ",a/b)
elif (ch == 5):
    a = int(input("Enter the marks obtained : "))
    b = int(input("Enter the total marks : "))
    print("The percentages are : ",a/b*100)
else:
    print("Invalid choice.\n Enter the appropriate choice.")
print("Program Finished.")

'''
#Example 2

#calculator (choose 1 or add for addition, choose 2 or sub for substract)

print("Choose option from below :")
print("Press 1 or add - Addition")
print("Press 2 or sub- Substraction")
print("Press 3 or mul- Multiplication")
print("Press 4 or div- Division")
print("Press 5 or per- Percentage")

ch = input("Enter your choice : ")

if (ch == "1" or ch =="add"):
    a = int(input("Enter the first number for addition : "))
    b = int(input("Enter the secound number for addition : "))
    print("The addition is : ",a+b)
elif (ch == "2" or ch == "sub"):
    a = int(input("Enter the first number for substraction: "))
    b = int(input("Enter the secound number for substraction: "))
    print("The substraction is : ",a-b)
elif (ch == "3" or ch == "mul"):
    a = int(input("Enter the first number for multiplication : "))
    b = int(input("Enter the secound number for multiplication : "))
    print("The multiplication is : ",a*b)
elif (ch == "4" or ch == "div"):
    a = int(input("Enter the first number division : "))
    b = int(input("Enter the secound number division : "))
    print("The division is : ",a/b)
elif (ch == "5" or ch == "per"):
    a = int(input("Enter the marks obtained : "))
    b = int(input("Enter the total marks : "))
    print("The percentages are : ",a/b*100)
else:
    print("Invalid choice.\n Enter the appropriate choice.")
print("Program Finished.")

'''

#Example 3

#calculator (choose any reference word for addition or substraction or ......)

print("Choose option from below :")
print("Press 1 - Addition")
print("Press 2 - Substraction")
print("Press 3 - Multiplication")
print("Press 4 - Division")
print("Press 5 - Percentage")

ch = input("Enter your choice : ")

add=["1","add","Add","ADD","addition","Addition","ADDITION","+"]
sub=["2","sub","Sub","SUB","substraction","Substraction","SUBSTRACTION","-"]
mul=["3","mul","Mul","MUL","multiplication","Multiplication","MULTIPLICATION","*"]
div=["4","div","Div","DIV","division","Division","DIVISION","/"]
per=["5","per","Per","PER","percentage","Percentage","PERCENTAGE","%"]

if (ch in add):
    a = int(input("Enter the first number for addition : "))
    b = int(input("Enter the secound number for addition : "))
    print("The addition is : ",a+b)
elif (ch in sub):
    a = int(input("Enter the first number for substraction: "))
    b = int(input("Enter the secound number for substraction: "))
    print("The substraction is : ",a-b)
elif (ch in mul):
    a = int(input("Enter the first number for multiplication : "))
    b = int(input("Enter the secound number for multiplication : "))
    print("The multiplication is : ",a*b)
elif (ch in div):
    a = int(input("Enter the first number division : "))
    b = int(input("Enter the secound number division : "))
    print("The division is : ",a/b)
elif (ch in per):
    a = int(input("Enter the marks obtained : "))
    b = int(input("Enter the total marks : "))
    c = a/b*100
    print("The percentages are : ",round(c,2))
else:
    print("Invalid choice.\nEnter the appropriate choice.")
print("Program Finished.")

