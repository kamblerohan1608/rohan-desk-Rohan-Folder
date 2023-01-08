'''
a= int(input("Enter number : "))
b= int(input("Enter number : "))
print(a-b)

'''

def reverse(n):
    s=[]
    for i in n:
        if i not in s:
            s.append(i)
    print(s)
    
reverse([1,1,1,1,2,3])
