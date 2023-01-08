
#r pattern

for row in range(14):
    for col in range(10):
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
        elif (row>7) and (row-col==6) or (row==13) and (col<3):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print( )


#number pattern:
'''
n=1
for i in range(1,6):
    for j in range(i):
        print(n,end=" ")
        n=n+1
    print()
'''

# character pattern
'''
for i in range(200):
    print(str(chr(i))+"\t"+str(i))
'''

#
'''
n=65
for i in range(8):
    
    for col in range(i):
        if n<91:
            print(chr(n),end=" ")
            n=n+1
    print()

#
n=97
for i in range(8):
    
    for col in range(i):
        if n<123:
            print(chr(n),end=" ")
            n=n+1
    print()

'''

#
'''
for i in range(6):
    for j in range(65,90):
        print(chr(j),end=" ")
    print()
'''













