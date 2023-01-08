
#while loop:
'''
#1-10

i=1
while i<=10:
    print(i)
    i=i+1
 
#10-1

i=10
while i>=1:
    print(i)
    i=i-1

#user input 1-n

a=int(input("Enter the number : "))
i=1
while (i<=a):
    print(i)
    i=i+1


#user input n to 1

a=int(input("Enter the number : "))

while a>=1:
    print(a)
    a=a-1

#table

a=int(input("Enter the numnber : "))
i=1
while i<=10:
    table=a*i
    print(table)
    i=i+1

#factorial

fact=1
n=5
while n>=1:
    fact=fact*n
    n=n-1
print(fact)


#take letter input in each itteration and print name at the end
a=int(input("Enter the number : "))
i=1
s=""
while i<=a:
    b=input("Enter the number : ")
    i=i+1
    s=s+b
print(s)


# take user input and print numbers below entered number also mannage negative part.

a=int(input("Enter the number : "))
if a>0 and a<=50:
    while a>=1:
        print(a)
        a=a-1
else:
    print("Enter the valid positive number below 50")



#
a=int(input("Enter the number : "))
i=1
while i<=a:
    if i%2==0:
        print(i,"is an even number.")
    else:
        print(i,"is an odd number.")
    i=i+1

'''

#take user input and display number from 1 till user input

a=int(input("Enter the number : "))
if a<=50 and a>0:
    i=1
    while i<=a:
        print(i)
        i+=1
elif a<0 and a>=-100:
    while a<=-1:
        print(a)
        a+=1
else:
    print("Entered number is out of range.")































