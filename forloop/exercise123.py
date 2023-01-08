
#for loop exercies

#print numbers till user input
'''
a=int(input("Enter the number : "))
for i in range(1,a+1):
    print(i)
'''
#for loop using list as a range
'''

ls=[1,2,3,4,5,6,7,8,9]
for i in ls:
    print(i)

ls=["Rohan","Sam","Sakshi","Javed"]
for i in ls:
    print(i)
'''

# calculate a table
'''
a=int(input("Enter the number : "))
for i in range(1,11):
    total=(a*i)
    print(total)
'''
#itterate using string
'''
a="abcdefghijklmnopqrstuvwxyz"
for i in a:
    print(i)
'''
#print sum of the listed elements
'''
a=[1,2,35,45,78,90,10]
total=0
for i in a:
    total=total+i
    print(total)
'''

#factorial
'''
a=int(input("Enter the number : "))
fact=1
for i in range(a,0,-1):
    fact=fact*i
    print(fact)

a=int(input("Enter the number : "))

for i in range(1,11):
    table=a*i
    print(table, end="+")
'''
#table in reverse order

a=int(input("Enter a number : "))

for i in range(10,0,-1):
    rtable=a*i
    print(rtable)






























