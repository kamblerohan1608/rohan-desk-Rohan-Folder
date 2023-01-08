'''
#

* 
* * 
* * * 
* * * * 
* * * * * 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=1
    while j<=i:
        print("*", end=" ")
        j+=1
    i+=1
    print()


* * * * * 
* * * * 
* * * 
* * 
* 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=a
    while j>=i:
        print("*",end=" ")
        j-=1
    i+=1
    print()



        * 
      * * 
    * * * 
  * * * * 
* * * * * 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=a
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    print()
    i+=1


* * * * * 
  * * * * 
    * * * 
      * * 
        * 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=a
    while k>=i:
        print("*",end=" ")
        k-=1
    print()
    i+=1



        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=a
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
    i+=1
    print()



* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=a
    while k>=i:
        print("*",end=" ")
        k-=1
    l=a
    while l>i:
        print("*",end=" ")
        l-=1
    i+=1
    print()



* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()
k=1
while k<a:
    l=a
    while l>k:
        print("*",end=" ")
        l-=1
    print()
    k+=1
        


        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 



a=int(input("Enter the number : "))
i=1
while i<=a:
    j=a
    while j>i:
        print(" ",end=" ")
        j-=1
    k=1
    while k<=i:
        print("*",end=" ")
        k+=1
    i+=1
    print()
l=1
while l<a:
    m=1
    while m<=l:
        print(" ",end=" ")
        m+=1
    n=a
    while n>l:
        print("*", end=" ")
        n-=1
    print()
    l+=1



* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 


a=int(input("Enter the number : "))

i=1
while i<=a:
    j=1
    while j<i:
        print(" ",end=" ")
        j+=1
    k=a
    while k>=i:
        print("*",end=" ")
        k-=1
    l=a
    while l>i:
        print("*",end=" ")
        l-=1
    i+=1
    print()
m=1
while m<a:
    n=a-2
    while n>=m:
        print(" ",end=" ")
        n-=1
    o=0
    while o<=m:
        print("*",end=" ")
        o+=1
    p=1
    while p<=m:
        print("*",end=" ")
        p+=1
    m+=1
    print()
    


*               * 
* *           * * 
* * *       * * * 
* * * *   * * * * 
* * * * * * * * * 
* * * *   * * * * 
* * *       * * * 
* *           * * 
*               * 


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    k=a
    while k>i:
        print(" ",end=" ")
        k-=1
    l=a-1
    while l>i:
        print(" ",end=" ")
        l-=1
    m=1
    while m<=i:
        if m<a:
            print("*",end=" ")
        m+=1
    print()
    i+=1
n=1
while n<a:
    o=a
    while o>n:
        print("*",end=" ")
        o-=1
    p=1
    while p<=n:
        print(" ",end=" ")
        p+=1
    q=1
    while q<n:
        print(" ",end=" ")
        q+=1
    r=a
    while r>n:
        print("*",end=" ")
        r-=1
    n+=1
    print()
    


        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 



x=int(input("Enter the height of pattern : "))
if x%2==0:
    x=x+1
    print("Entered value is even hence added 1 i.e",x )
a=(x+1)/2

i=1
while i<=a:
    j=a
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
    print()
    i+=1
m=1
while m<a:
    n=1
    while n<=m:
        print(" ",end=" ")
        n+=1
    o=a
    while o>m:
        print("*",end=" ")
        o-=1
    p=a-1
    while p>m:
        print("*",end=" ")
        p-=1
    m+=1
    print()
        


1	2	3	4	5	
2	4	6	8	10	
3	6	9	12	15	
4	8	12	16	20	
5	10	15	20	25	


a=int(input("Enter the number : "))
i=1
while i<=a:
    j=1
    while j<=a:
        print(i*j,end="\t")
        j+=1
    i+=1
    print()

'''






















