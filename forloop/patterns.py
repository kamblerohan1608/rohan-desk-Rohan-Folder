
# Pattern 1
'''
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


for row in range(1,11):
    for col in range(1,11):
        print(row*col,end="\t")
    print( )


'''



#pattern 2

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 


for row in range(0,5):
    for col in range(0,5):
        print("*",end=" ")
    print( )


'''

#pattern 3

'''

*
* *
* * *
* * * *
* * * * *


n=5
for row in range(0,n):
    for col in range(row+1):
        print("*",end=" ")
    print( )

'''

#pattern 4

'''

* * * * * 
* * * *
* * *
* *
*



n=5
for row in range(0,5):
    for col in range(n-row):
        print("*",end=" ")
    print( )
'''


#pattern 5

'''

        *
      * *
    * * *
  * * * *
* * * * *


n=5
for row in range(0,5):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*",end=" ")
    print( )


'''

#pattern 6

'''

* * * * *
  * * * *
    * * *
      * *
        *


n=5
for row in range(0,n):
    for col in range(row):
        print(" ",end=" ")
    for col1 in range(n-row):
        print("*",end=" ")
    print( )

'''


#pattern 7

'''

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *



n=5
for row in range(0,n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*", end=" ")
    for col2 in range(row):
        print("*",end=" ")
    print()
'''


#pattern 8

'''

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *


n=5
for row in range(n,0,-1):
    for col in range(n-row):
        print(" ",end=" ")
    for col1 in range(row):
        print("*",end=" ")
    for col2 in range(row-1):
        print("*",end=" ")
    print()



n=5
for row in range(0,n):
    for col in range(row):
        print(" ",end=" ")
    for col1 in range(n-row):
        print("*",end=" ")
    for col2 in range(n-row-1):
        print("*",end=" ")
    print()
'''

#pattern 9

'''

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


n=5
for row in range(0,n):
    for col1 in range(row+1):
        print("*",end=" ")
    print(" ")


for row1 in range(0,row):
    for col2 in range(row-row1):
        print("*",end=" ")
    print(" ")
'''   
    
#pattern 10

'''

        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *


n=5
for row in range(0,n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*",end=" ")
    print( )
for row1 in range(row):
    for col2 in range(row1+1):
        print(" ",end=" ")
    for col3 in range(n-row1-1):
        print("*",end=" ")
    print( )
'''


#pattern 11

'''

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 


n=5
for row in range(0,n):
    for col in range(row):
        print(" ",end=" ")
    for col1 in range(n-row):
        print("*",end=" ")
    for col2 in range(n-row-1):
        print("*",end=" ")
    print( )
for row1 in range(row):
    for col3 in range(row-row1-1):
        print(" ",end=" ")
    for col4 in range(row1+2):
        print("*",end=" ")
    for col5 in range(row1+1):
        print("*",end=" ")
    print( )
'''

#pattern 12

'''


*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * * 
* * * *   * * * * 
* * *       * * *
* *           * *
*               *


n=5
for row in range(0,5):
    for col in range(row+1):
        print("*",end=" ")
    for col1 in range(n-row-1):
        print(" ",end=" ")
    for col2 in range(n-row-2):
        print(" ",end=" ")
    for col3 in range(row+1):
        if col3<4:
            print("*",end=" ")
    print()
for row1 in range(row):
    for col4 in range(row-row1):
        print("*",end=" ")
    for col5 in range(row1+1):
        print(" ",end=" ")
    for col6 in range(row1):
        print(" ",end=" ")
    for col7 in range(row-row1):
        print("*",end=" ")
    print( )

'''

#pattern 13

'''

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *



n=5
for row in range(n):
    for col in range(n-row-1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*",end=" ")
    for col2 in range(row):
        print("*",end=" ")
    print( )
for row1 in range(row):
    for col3 in range(row1+1):
        print(" ",end=" ")
    for col4 in range(row-row1):
        print("*",end=" ")
    for col5 in range(row-row1-1):
        print("*",end=" ")
    print( )
'''



















