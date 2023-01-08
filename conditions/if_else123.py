#if_else

'''
#Example 1 : addition of two numbers

a=int(input("Enter the first number : "))
b=int(input("Enter the secound number : "))
add=a+b
if (add>0):
    print("The addition is positive : ",add)
else:
    print("The addition is negative : ",add)
print("Program Finished.")


#Example 2 : finding name in the list


ls_name=["Rohan","Roy","Sam","Shlok","Seema"]
name=input("Enter the name : ")
if name in ls_name :
    print("Hey",name,"Congratulation!!! Your name is in the list.")
else :
    print("Sorry!!! Your name is not in thr list.")
print("Program Finished.")


#Example 3 : finding even odd number


a1=int(input("Enter the number : "))
if(a1%2==0):
    print("The entered number is even.")
else:
    print("The enteres number is odd.")
print("Program Finished.")


#Example 3 to find out whther the last digit of entered number is divisible by 5.


a2=int(input("Enter the number : "))
l_d = a2 % 10
if (l_d % 3 == 0):
    print("The last digit of the entered number is divisible by 3.")
else:
    print("The last digit of entered number is NOT divisible by 3")
print("Program Finished")
'''

a3=int(input("Enter the percentages : "))
if (a3 >= 90):
    print("Your grade is A.")
elif (a3 < 90 and a3 >= 80):
    print("Your grade is B.")
elif (a3 < 80 and a3 >= 60):
    print("Your grade is C.")
else :
    print("Your grade is D.")
print("Program Finished")






















