'''
#bmi

height=int(input("Enter your height : "))
weight=int(input("Enter your weight : "))
bmi=weight/(height/100)**2
print("Your Body Mass Index is : ",bmi)


marks=float(input("Enter the marks obtaind : "))
total=float(input("Enter the total marks : "))
per=marks/total*100
per1=round(per,3)
print("Your percentages are : ",per,"%") 
print("Which can be represented as : ",per1)


#Advance assignment operators

a=int(input("Enter the number : "))
print(a)

a+=10
print(a)

a-=10
print(a)

a*=10
print(a)

a/=2
print(a)

a**=2
print(a)

a%=1190
print(a)

a/=7
a=round(a,3)
print(a)



#logical opperators

a=10
b=20
c=30
print("10>20 and 20<30",a>b and b<c)
print("10>20 or 20<30",a>b or b<c)
print("20=20 and 20<30",c==b+a and b<c)
'''

t=[1,2,3,4,5,6,7,8,9,10,"rohan","suman","kiran","shyam","raj"]
new=input("Enter the entry to find in list t : ")  #only string data will be searched here if entered int values then it will show false.
print("Is",new,"in the list t : ",new in t)
result=(new in t)
print(result)












