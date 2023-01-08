'''
* * * * * * * * 
*             * 
*   # # # #   * 
*   #     #   * 
*   #     #   * 
*   # # # #   * 
*             * 
* * * * * * * * 


n=int(input("Enter the number : "))
row=1
while row<=n:
    col=1
    while col<=n:
        if row==1 or row==n or col==1 or col==n:
            print("*",end=" ")
        elif (row==3 and col>=3 and col<=n-2) or (row==n-2 and col>=3 and col<=n-2):
            print("#",end=" ")
        elif (col==3 and row>=3 and row<=n-2) or (col==n-2 and row>=3 and row<=n-2):
            print("#",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()


a=int(input("Enter the number : "))
s=0
while a:
    b=a%10
    s=s+b
    a=a//10
print("The sum is",s)
'''
'''
a=1
while a!=0:
    s=0
    a=int(input("Enter the number : "))
    if a < 3:
        s=s+2
    else:
        for i in range(a,0,-1):
            if a%i==0:
                s=s+1
    if s==2:
        print(a,"is a prime number.",)
    else:
        print(a,"not a prime number.",)
'''
'''
i=0
while i<3:
    print(i)
    i+=1
else:
    print(7)


i=2
for x in range(i):
    x+=4
    print(id(x))
    print(x)
print(x)
print(id(x))

'''
'''
a=1
i=0
s=0
while a!=0:
    a=int(input("Enter the number : "))
    if a==0:
        pass
    else:
        
        s=s+a
        i=i+1
print("The average is "+ str(s/i))



#pallendrom no.

a=1
while a!=0:
    
    s=''
    a=int(input("Enter the number : "))
    c=int(a)
    if a>0 and a<10:
        print("**************invalid number***************")
        print()
        print("***********Enter a valid number*************")
    elif a==0:
        print()
        print("***************Thank you********************")

    else:
        a=str(a)
        for i in a:
    
            j=c%10
            s=s+str(j)
            c=c//10

        if a==s:
            print(a +" is a pallendrom number.", a,"==",s)
        else:
            print(a +" is not pallendrom number.", a ,"!=",s)

'''
'''
# Perfect number single input

while True:

    num=int(input("Enter the number : "))

    if num == 0:
        print("************ Thank You ****************")
        break
    i_p=num
    a=num-1
    s=0
    p=""
    while a>=1:
        if num%a==0:
            p = p + str(a) + " "
            s=s+a
        a-=1    
    if s==i_p:
        print(i_p, "Number is a perfect number as multiples",p,"have addition of",s)
    else:
        print(i_p, "it is not a perfect number as multiples",p,"have addition of",s,)

# Perfect number over a range ( Two inputs )

while True:
    num_1=int(input("Enter the number : "))
    num_2=int(input("Enter the number : "))
    if num_1 > num_2:
        num_1,num_2=num_2,num_1
    i_p1 = num_1
    i_p2 = num_2
    k=0
    while i_p1 <= i_p2:
        x = i_p1 - 1
        s=0
        p=""
        while x >= 1:
            if i_p1 % x == 0:

                s = s + x
                p = p + str(x) + " "

            x -= 1 

        if s == i_p1:
            print(i_p1, "Number is a PERFECT NUMBER as multiples",p,"have addition of",s)
            k=k + 1
        i_p1 += 1
    if k==0:
        print("No perfect number in given sequences.")

'''
'''
# Q. sequence  :   1 + x/1! + x^2/2! + x^3/3!.......x^n/n!
# To ckeck output:
    x=1, n=1  o/p : 2
    x=1, n=2  o/p : 2.5
    x=1, n=3  o/p : 2.6

    x=2, n=1  o/p : 3
    x=2, n=2  o/p : 5
    x=2, n=3  o/p : 6.33

'''    
'''
def fact(k):
    fac=1
    while k>=1:
        fac=fac*k
        k-=1
    return fac
while True:
    x=int(input("Enter the value of x : "))
    n=int(input("Enter the value of n : "))
    i=1
    z=1
    while i<=n:
        z=z + (x**i) /fact(i)   
        i+=1
    print(z)
'''
'''
# Q. sequence a + ar + ar^2 + ar^3 + .......ar^n
# To check output : 
#a=2 r=2 n=2  o/p : 14
#a=3 r=2 n=2  o/p : 21


a=int(input("Enter the value of a : "))
r=int(input("Enter the value of r : "))
n=int(input("Enter the value of n : "))
i=0
z=0
while i<=n:
    z=z + a*(r**i)
    i+=1
print(z)
'''

















