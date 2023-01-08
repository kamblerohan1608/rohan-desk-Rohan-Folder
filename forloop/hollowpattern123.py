#vowels
'''
names=["rohan","sonakshi","hritik","rutuja","shilpa","komal"]
v=["a","e","i","o","u"]
for name in names:
    for vo in v:
        if vo in name:
            print(name," has ",vo,"vowel present.")
            
'''
#numbers
'''
names=["rohan1","sonakshi2","hritik3","4rutuja","shi5lpa","k6omal"]
n=[1,2,3,4,5,6,7,8,9,0]
for name in names:
    for m in n:
        if str(m)in name:
            print(name,"has",m,"number in it.")

'''
#Hollow patterns

#1
'''
* * * * * *
*         *
*         *
*         *
*         *
* * * * * *

n=7
for row in range(1,7):
    for col in range(1,7):
        if (row==1) or (row==n-1) or (col==1) or (col==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )
'''
#2
'''
*
* *
*   *
*     *
*       *
* * * * * *


n=7
for row in range(1,n):
    for col in range(1,n):
            if (row==n-1) or (col==1) or(row==col):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print( )
'''
#3
'''
 
          *
        *   *
      *       *
    *           * 
  *               *
* * * * * * * * * * *


n=6
for row in range(6):
    for col in range(11):
        if (row==n-1) or (row+col==5) or (col-row==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#4
'''
 * * * * * * *
 *           *  
 *     *     *
 *   * * *   *
 *     *     *
 *           *
 * * * * * * *

n=8
for row in range(1,n):
    for col in range(1,n):
        if (row==1) or (row==n-1) or (col==1) or (col==n-1):
            print("*",end=" ")
        elif (row==4) and (col>2) and (col<6):
            print("*",end=" ")
        elif (col==4) and (row>2) and (row<6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )
'''
#5
'''

          *
        *   *
      *       *
    *           * 
  *               *
*                   *
  *               *
    *           *
      *       *
        *   *
          *


n=12
for row in range(1,n):
    for col in range(1,n):
        if (row+col==7) or (col-row==5) or (row-col==5) or (row+col==17):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print( )

'''




for i in range(10):
    print(i,"\n")









