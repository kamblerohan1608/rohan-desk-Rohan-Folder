'''

#practice find wether entered letter is vowel or not.

a="aeiousAEIOUS"
b=input("Enter the letter : ")
if (b in a):
    print("the enteres letter is a vowel")
else :
    print("The entered letter is NOT a vowel.")



# practice

#calculate percentage of class attended and if less then 75 show he can't sit in exam.

a=int(input("Enter total number of working days : "))
b=int(input("Enter total number of days absent : "))

per= (a-b)/a*100
if per >= 75 :
    print("You are eligibal for exam.")
else:

   print("You are not eligible for exam as your attendance is low.")



#practice

#bonus calculation

a=int(input("Enter the salary : "))
b=int(input("Enter the total no. of working years : "))
if (b > 10):
    print("Your salary is ",a + (a * 10/100))
elif (b >= 6) and (b <= 10):
    print("Your salary is",a + (a * 8/100))
else :
    print("Your salary is", a + (a *5/100))



#Practice

# calulate the type of triangle :

a=int(input("Enter the length of first side : "))
b=int(input("Enter the length of second side : "))
c=int(input("Enter the length of third side : "))
if (a==b==c):
    print("This is a eqitlateral triangle.")
elif (a != b!= c):
    print("This is a scalene triangle.")
else :
    print("This is a isoscales triangle.")



# Practice

#accept age, sex and no. of days of work and display weges accordingly (weges : payment on daily basis) i.e age >=18 and age < 30    Male     700 wege per day
#                                                                                                                                    Female   750
#                                                                                                           age >=30 and age <= 40  Male     800
#                                                                                                                                    Female   850   

age=int(input("Enter the age : "))
gender=input("Enter the gender : ")
days=int(input("Enter the total working days : "))
if (age >=18 and age < 30):
    if (gender=="male"):
        print("The salary is : ",days*700)
    elif (gender=="female"):
        print("The salary is : ",days*750)
    else :
        print("Enter the correct gender.")
elif (age >=30 and age <= 40):
    if (gender=="male"):
        print("The salary is : ",days*800)
    elif (gender=="female"):
        print("The salary is : ",days*850)
    else :
        print("Enter the correct gender.")
else:
    print("Enter correct age.")

'''

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))
d=int(input("Enter the number : "))

if (a>b):
    if (a>c):
        if (a>d):
            print(a,"is greater.")
        else:
            print(d,"is greater.")
elif (b>c):
    if (b>a):
        if (b>d):
            print(b,"is greater.")
        else:
            print(d,"is greater.")
elif (c>d):
    if (c>a):
        if (c>b):
            print(c,"is greater.")
        else:
            print(b,"is greater.")
else :
    print(d,"is greater.")
