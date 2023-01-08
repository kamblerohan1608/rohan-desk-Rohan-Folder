


from functools import reduce

l=[1,2,3,4,5]

def a(n):
    return n*2
    

b=map(a,l)
print('The result of map fucntion',list(b))
# b=list(b)
# print(b)


# for i in b:
#     print(i)

z=filter((lambda i: i if i>2 else None),l)
    
print(z)
print(list(z))

# for i in z:
#     print(i)
    

def fib(a,b):
    # print(a)
    print(b)
    print(a+b)
    # print(s)

# c = reduce(fib,l)
# print(c)

n=reduce(lambda a,b:a+b,l)
print(n)
