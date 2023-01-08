'''
#hollow square :

* * * * *
*       *
*       *
*       *
* * * * *



row=1
while row<=5:
    col=1
    while col<=5:
        if (col==5) or (col==1) or (row==1) or (row==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()



#hollow triangle pattern :


          *           
        *   *         
      *       *       
    *           *     
  *               *   
* * * * * * * * * * * 

row=1
while row<=6:
    col=1
    while col<=11:
        if (row+col==7) or (col-row==5) or (row==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()


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


row=1
while row<=11:
    col=1
    while col<=11:
        if (row+col==7) or (col-row==5) or (row-col==5) or (row+col==17):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()


* * * * * * * 
*           * 
*     *     * 
*   * * *   * 
*     *     * 
*           * 
* * * * * * * 


row=1
while row<=7:
    col=1
    while col<=7:
        if row==1 or col==1 or row==7 or col==7:
            print("*",end=" ")
        elif row==4 and col>=3 and col<=5:
            print("*",end=" ")
        elif col==4 and row>2 and row<6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    print()
    row+=1



#  number patterns:
n=15
i=1
while i<=5:
    j=1
    while j<=i:
        print(n,end="\t")
        n=n-1
        j+=1
    print()
    i+=1

'''
#printing name with star pattern :

row=0
while row<=14:
    col=0
    while col<=12:
        if (row==0) and (col<5):
            print("*",end=" ")
        elif (col==1):
            print("*",end=" ")
        elif ((row==1) and (col==5))or((row==2) and (col==6)):
            print("*",end=" ")
        elif (col==6) and (row>1) and (row<6):
            print("*",end=" ")
        elif row==6 and col==5:
            print("*",end=" ")
        elif (row==7) and (col>1) and (col<5):
            print("*",end=" ")
        elif (row>7) and (row-col==6) or (row==14) and (col<3):
            print("*",end=" ")
        elif (row==14 and col>6 and col<10):
            print("*",end=" ")

        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

print("\n")
print("\n")

row=1
while row<=14:
    col=1
    while col<=10:
        if ((row==1) and (col>2) and (col<8)) or (row==14 and col>2 and col<8):
            print("*",end=" ")
        elif (col==1 and row>2 and row<13) or (col==9 and row>2 and row<13):
            print("*",end=" ")
        elif ((row==1) and (col==3))or((row==2) and (col==2)) or (row==3 and col==1):
            print("*",end=" ")
        elif ((row==1) and (col==7))or((row==2) and (col==8)) or (row==3 and col==9):
            print("*",end=" ")
        elif ((row==12) and (col==1))or((row==13) and (col==2)) or (row==14 and col==3):
            print("*",end=" ")
        elif ((row==12) and (col==9))or((row==13) and (col==8)) or (row==14 and col==7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
print("\n")
print("\n")


row=1
while row<=15:
    col=1
    while col<=10:
        if col==2 or col==9:
            print("*",end=" ")
        elif (row==8 and col>2 and col<9) or (row==15) and (col<4) or (row==15) and (col>7):
            print("*",end=" ")
        elif ((row==1) and (col<4)) or ((row==1) and (col>7)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
print("\n")
print("\n")


row=1
while row<=15:
    col=1
    while col<=10:
        if (row==1 and col>4 and col<6):
            print("*",end=" ")
        elif col==2 and row>3 or col==9 and row >3:
            print("*",end=" ")
        elif ((row==1) and (col==5))or((row==2) and (col==4)) or (row==3 and col==3):
            print("*",end=" ")
        elif ((row==1) and (col==6))or((row==2) and (col==7)) or (row==3 and col==8):
            print("*",end=" ")
        elif row==8 and col>1 and col<9:
            print("*",end=" ")
        elif (row==15) and (col<4) or (row==15) and (col>7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
print("\n")
print("\n")


row=1
while row<=15:
    col=1
    while col<=12:
        if (col==2 and row<11) or (col==11 and row<11):
            print("*",end=" ")
        elif col-row==1 and col<12:
            print("*",end=" ")
        elif (row==10) and (col<4) or (row==1) and (col>9):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    















