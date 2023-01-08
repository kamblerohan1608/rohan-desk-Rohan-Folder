#Identity operator

a=10
b=10
print(id(a))
print(id(b))
print(a)

a="10"
b="10"
print(id(a))
print(id(b))
print(a)

a=10.1
b=10.1
print(id(a))
print(id(b))
print(a)

a=10+0j
b=10+0j
print(id(a))
print(id(b))
print(a)

a="true"
b="true"
print(id(a))
print(id(b))
print(a)

a=[1,2,3,4,5]     #list does not share memory location
b=[1,2,3,4,5]     
print(id(a))
print(id(b))
print(a)

a=(1,2,3,4,5)
b=(1,2,3,4,5)
print(id(a))
print(id(b))
print(a)
