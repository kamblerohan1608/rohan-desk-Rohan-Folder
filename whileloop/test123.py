# practice patterns :

#for :
'''
n=5
for i in range(0,n):
    for j in range(i+1):
        print("*",end=" ")
    print()



n=5
for row in range(n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*",end=" ")
    for col2 in range(row):
        print("*",end=" ")
    print()

for row1 in range(row):
    for col3 in range(row1+1):
        print(" ",end=" ")
    for col4 in range(row-row1):
        print("*",end=" ")
    for col5 in range (row-row1-1):
        print("*",end=" ")
    print()
        
'''
'''
n=1
while n!=0:
    
    n=int(input("Enter the number : "))
    for row in range(n,0,-1):
        for col in range(row-1):
            print(" ",end=" ")
        for col1 in range(n-row+1):
            print("*",end=" ")
        for col2 in range(n-row):
            print("*",end=" ")
        print()
        
    for row1 in range(n-1,0,-1):
        for col3 in range(n-1-row1+1):
            print(" ",end=" ")
        for col4 in range(row1):
            print("*",end=" ")
        for col5 in range(row1-1):
            print("*",end=" ")
        print()
else:
    print()
    print("****************Thank you******************")
    print("   *********     ")
    print("  *         *    ")
    print("  * *** *** *    ")
    print("  *  0   0  *    ")
    print("  *    *    *    ")
    print("  *   ( )   *    ")
    print("  *   ***   *    ")
    print("   *********     ")

print()
print()
print("********* Visit again ***********")



# prime numbers between two user inputs.

a=int(input("Enter the first number : "))
b=int(input("Enter the secound number : "))

if a>b:                              
    a,b=b,a                          # to correct the sequence from smaller to grater number if entered oppositely
    
i=0                                  # to show number of prime numbers present in the mentioned squence 
x=a                                  # storing value of a in x to be used in last result to show the start point of the sequence
k=""
while a<=b:
    if a==0 or a==1 :                # 0 and 1 are not prime numbers setting s=0 to neglect this numbers
        s=0
    else:
        z=a                          # storing a in z as z will be used to verify multiples of a by decreasing its values and checking its reminder when its dividing a in each itteration
        s=0
        while z>=1:
            if a%z==0:
                s=s+1                # s will stores and update its value by 1 each time a multiple of a is observed 
            z-=1
    if s==2:                         # if s==2 it indicates that there are 2 multiple of this number (i.e. a),which is the requirement as prime number are only divisible fully by either by 1 or by itself
        i=i+1
        k=k + str(a)+"  "           # k stores all the prime number calculated in a string to display later,
    a+=1

print("There are ",i," prime numbers between ",x," and ",b," which are : "+k)

'''
'''

# addition of even and odd numbers falling between two user inputs :

a=int(input("Enter the first number : "))
b=int(input("Enter the secound number : "))
c=a
d=b
i=""
j=""
k=0
l=0
if a>b:
    a,b=b,a
    c,d=d,c
while a<=b:
    if a%2==0:
        i=i+str(a)+" "
        k=k+a
        
    else:
        j=j+str(a)+" "
        l=l+a
    a+=1
    
print()
print("The even numbers between",c,"to",d,"are",i)
print("The addition of even numbers is : ",k)
print()
print("The odd numbers between",c,"to",d,"are",j)
print("The addition of odd numers is : ",l)        
        

a=int(input("Enter the number : "))
for i in range(1,11):
    print(a," * ",i ,"=", a*i)

'''




























