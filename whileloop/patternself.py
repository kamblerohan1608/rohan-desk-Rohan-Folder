
#patterns:

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


i=1
while i<=10:
    j=1
    while j<=10:
        print(i*j,end="\t")
        j=j+1
    print( )
    i=i+1







#pattern 2


* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 



i=1
while i<=10:
    j=1
    while j<=10:
        print("*",end=" ")
        j+=1
    print()
    i+=1




#pattern 3



*
* *
* * *
* * * *
* * * * *



i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print( )
    i+=1




#pattern 4



* * * * * 
* * * *
* * *
* *
*



i=1
while i<=5:
    j=5
    while j>=i:
        print("*",end=" ")
        j-=1
    print( )
    i+=1





#pattern 5



        *
      * *
    * * *
  * * * *
* * * * *


i=1
while i<=5:
    j=5
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    print()
    i+=1





#pattern 6



* * * * *
  * * * *
    * * *
      * *
        *


i=1
while i<=5:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=5
    while k>=i:
        print("*",end=" ")
        k-=1
    print()
    i+=1




#pattern 7



        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *



i=1
while i<=5:
    j=5
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    l=1
    while l<i:
        print("*",end=" ")
        l+=1
    print( )
    i+=1




#pattern 8



* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *



i=1
while i<=5:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=5
    while k>=i:
        print("*",end=" ")
        k-=1
    l=5
    while l>i:
        print("*",end=" ")
        l-=1
    print()
    i+=1
        
        




#pattern 9



*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()
k=1    
while k<=5:
    l=5
    while l>k:
        print("*",end=" ")
        l-=1
    k+=1
    print()


   
    
#pattern 10



        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *



i=1
while i<=5:
    j=5
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    i+=1
    print( )
l=1
while l<=5:
    m=1
    while m<=l:
        print(" ",end=" ")
        m+=1
    n=5
    while n>l:
        print("*",end=" ")
        n-=1
    l+=1
    print( )
        






#pattern 11



* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 



i=1
while i<=5:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=5
    while k>=i:
        print("*",end=" ")
        k-=1
    l=5
    while l>i:
        print("*",end=" ")
        l-=1
    print()
    i+=1
m=1
while m<=4:
    n=4
    while n>m:
        print(" ",end=" ")
        n-=1
    o=1
    while o<=m+1:
        print("*",end=" ")
        o+=1
    p=1
    while p<=m:
        print("*",end=" ")
        p+=1
    print( )
    m+=1
        




#pattern 12




*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * * 
* * * *   * * * * 
* * *       * * *
* *           * *
*               *



i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    k=5
    while k>i:
        print(" ",end=" ")
        k-=1
    l=4
    while l>i:
        print(" ",end=" ")
        l-=1
    m=1
    while m<=i:
        if m<5:
            print("*",end=" ")
        m+=1
        
    print( )
    i+=1
n=1
while n<=4:
    o=4
    while o>=n:
        print("*",end=" ")
        o-=1
    p=1
    while p<=n:
        print(" ",end=" ")
        p+=1
    q=2
    while q<=n:
        print(" ",end=" ")
        q+=1
    r=4
    while r>=n:
        print("*",end=" ")
        r-=1
    print()
    n+=1





#pattern 13



        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 
  * * * * * * *
    * * * * *
      * * *
        *




i=1
while i<=5:
    j=5
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    l=1
    while l<i:
        print("*",end=" ")
        l+=1
    print( )
    i+=1
k=1
while k<=4:
    l=1
    while l<=k:
        print(" ",end=" ")
        l+=1
    m=4
    while m>=k:
        print("*",end=" ")
        m-=1
    n=4
    while n>k:
        print("*",end=" ")
        n-=1
    print()
    k+=1




i=1
while i<=5:
    j=5
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    i+=1
    print()
        


i=1
while i<=5:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=5
    while k>=i:
        print("*",end=" ")
        k-=1
    print()
    i+=1
'''


















