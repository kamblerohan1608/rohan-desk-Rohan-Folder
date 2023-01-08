
#program 1:
'''
#take a list and display how many times a is present in a perticular name.

ans:-

ls=["rohan","samarth","simran","kishor","seema","roy","moksh","ramesh","raja","pratiksha"]
for i in ls:
    s=0
    for j in i:
        if "a"==j:
            s=s+1
    print("a is present "+str(s)+" times in"+i)



#program 2

#print tabular structure

1	2	3	4	5	6	7	8	9	10	
2	4	6	8	10	12	14	16	18	20	
3	6	9	12	15	18	21	24	27	30	
4	8	12	16	20	24	28	32	36	40	
5	10	15	20	25	30	35	40	45	50	
6	12	18	24	30	36	42	48	54	60	
7	14	21	28	35	42	49	56	63	70	
8	16	24	32	40	48	56	64	72	80	
9	18	27	36	45	54	63	72	81	90	
10	20	30	40	50	60	70	80	90	100

#also convert it into dynamic

ans:-

#static

for row in range(1,11):
    for col in range(1,11):
        print(row*col,end="\t")
    print( )

#dynamic

a=int(input("Enter the number for box pattern : "))

for row in range(1,a+1):
    for col in range(1,a+1):
        print(row*col,end="\t")
    print( )


#problem 3:

#static square pattern


* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

#also make is dynamic.

ans:- 

#static

for row in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print( )

#dynamic


a=int(input("Enter the number : "))
for row in range(1,a+1):
    for col in range(1,a+1):
        print("*",end=" ")
    print( )


#problem 4

#right angle triangle pattern

*
* *
* * *
* * * *
* * * * *

#also make it dynamic.


#static

for row in range(6):
    for col in range(row+1):
        print("*",end=" ")
    print( )

#dynamic


a=int(input("Enter the number : "))
for row in range(a):
    for col in range(row+1):
        print("*",end=" ")
    print( )


#problem 5

#print below pattern

* * * * * 
* * * *
* * *
* *
*

#also make is dynamic

ans :-

#static

for row in range(5,0,-1):
    for col in range(row,0,-1):
        print("*",end=" ")
    print( )

#dynamic

a=int(input("Enter the number : "))
for row in range(a,0,-1):
    for col in range(row,0,-1):
        print("*",end=" ")
    print( )
    



#problem 6

#print mirror right angle triangle


     *
    **
   ***
  ****
 *****

#also make it dynamic

ans :-

#static

for i in range(1,6):
    s=0
    for j in range(6-i,0,-1):
        print(" ",end=" ")
        s=s+1
    for k in range(1,6-s+1):
        print("*",end=" ")
    print( )


#dynamic

a=int(input("Enter the number : "))
for i in range(1,a+1):
    s=0
    for j in range(a-i,0,-1):
        print(" ",end=" ")
        s=s+1
    for k in range(1,a-s+1):
        print("*",end=" ")
    print( )


#problem 7

#print below pattern

* * * * *
  * * * *
    * * *
      * *
        *
#also make it dynamic

ans :-

#static

for i in range(1,6):
    for j in range(2,i+1):
        print(" ",end=" ")
    for k in range(6-i,0,-1):
        print("*",end=" ")
    print( )

#dynamic

a=int(input("Enter the number : "))
for i in range(1,a+1):
    for j in range(2,i+1):
        print(" ",end=" ")
    for k in range(a+1-i,0,-1):
        print("*",end=" ")
    print( )


a=int(input("Enter the number : "))
for row in range(a,0,-1):
    for col in range(row,0,-1):
        print("*",end=" ")
    print( )

'''


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print( )







        

    
















