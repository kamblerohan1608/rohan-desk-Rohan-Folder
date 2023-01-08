# Recursive function 

# def factorial(n):
#     if n==0:
#         result = 1
#     else:
#         result=n*(factorial(n-1))
#     return result

# print(factorial(5))

# def main(n):
#     if n==0:
#         s=0
#     else:
#         s=n+(main (n-1))
#     return s

# print(main(10))

#fibonaciin series : 

n=int(input("Enter the limit : "))
addition=0
b=1
m=1
while m<=n:
    if m==1:
        print(addition,end=" ")
    else:

        c=addition
        addition=c+b
        print(addition,end=" ")
        b=c

    m+=1
