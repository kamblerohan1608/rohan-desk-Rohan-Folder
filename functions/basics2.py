import functools


import functools

#lamda function

#obj=lamda list of parameters: Expression

'''
#example 1 without parameters:

add=lambda:20+30
sub=lambda:30-20
a=add()
b=sub()
print(a)
print(b)
print(a+b)


# example 2 with parameters :

mul=lambda a,b : a*b
div=lambda a,b : a/b

a=int(input("Enter the number : "))
b=input("Enter the number : ")
b=int(b)
c=mul(a,b)
d=div(a,b)
print(c)
print(d)

#example 3

per=lambda obt,total : (obt*100)/total
k=per(20,100)
print(k)
print(per(30,100))


# pattern using lambda :

ptr=lambda a,b : a*b
a="*"
for i in range(1,6):
    print(ptr(a,i))
for j in range(5,0,-1):
    print(ptr(a,j))



#
n=5
for i in range(5):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()



#
balance=0
print(balance)
def deposit():
    global balance
    for i in range(500):
        balance +=2
    return balance
print(balance)
print(deposit())
print(deposit())
print(deposit())



a=1
table=lambda a,b:a*b
while a!=0:
    a=int(input("Enter the number : "))
    if a==0:
        print()
        print()
        print("*******Thank you*********")
        print()
        print()
    else :
        for i in range(1,11):
            print(table(a,i))


# lambda with conditions :

a=int(input("Enter the number : "))
age=lambda a:"even" if a%2==0 else "odd"
print(age(a))



#
a=int(input("Enter the number : "))
sign=lambda a:("Number is zero" if a==0 else "positive")if a>=0 else "negative"
print(sign(a))

#
a=1
b=1
c=1

while a!=0 and b!=0 and c!=0:
    a=int(input("Enter the number : "))
    b=int(input("Enter the number : "))
    c=int(input("Enter the number : "))
    grt=lambda a,b,c:("a ia greater" if (a>b and a>c) else "b is greatest") if c<a or c<b else "c is greatest"
    print(grt(a,b,c))


#Recursive function :

def test():
    print("Hello this is python lecture.")
    print("welcome")
    test()
test()

#

n=0
def demo():
    global n
    n+=1
    print(n)
    demo()
demo()
'''
#
# import sys
# print(sys.getrecursionlimit())
# sys.getrecursionlimit()


# Generator function

# used to return multiple of values at a time

# returns a unstructured gnerator object which is itterable and whoes values vanishes after used once.

#

# from functools import reduce
# from re import L


# def add():
#     a  = [1,2,3,4,5,6,7,8,9]
#     for i in a:
#         yield i

# x=add()
# print(x)
# # x=list(x)
# print(x)
# for i in x:
#     print(i)

# for i in x:
#     print(list(x))

# # Map

# def func(n):
#     return n**3 
# l=[1,2,3,4,5,6]
# x = map(lambda n:n**3,l)
# print(x)
# x = list(x)
# print(x)


# reduce

# def two(a,b):
#     return a+b
# l = [1,2,3,4,5]
# x = functools.reduce(two,l)
# print(x)

