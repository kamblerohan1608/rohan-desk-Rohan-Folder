
#if_elif_else
'''
#Example 1  Add two numbers if they are positive and if not find which one is negative.


a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
if (a<0)and(b<0):
    print("Both entered numbers are negative.")
elif (a<0):
    print("The first number is negative.")
elif (b<0):
    print("The secound number is negative.")
else :
    print("The addition is : ",a+b)
print("Program Finished.")


#Example 2 determine whether entered number is positive,negative or zero.


a1 = int(input("Enter the number : "))
if (a1>0):
    print("The entered number is positive.")
elif (a1<0):
    print("The entered number is negative.")
else :
    print("The entered number is zero.")
print("Program Finished.")
'''

#Example 3 write program to calculate electricity bill (accept no. of units from user) according to the following criteria:
#pricing
#first  100 no fees
#next 100 rs.5 per unit
#above 200 rs.10


units=int(input("Enter the number of units used : "))
if (units > 100 and units <= 200):
    print("The bill amount to be paid : ", (units-100) * 5,"INR.")
elif (units > 200):
    l_u1 = units - 200
    print("The bill to be paid : ",500 + (l_u1 * 10),"INR.")
else :
    print("No due payment for you.")

























