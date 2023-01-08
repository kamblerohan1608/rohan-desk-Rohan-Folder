#Type casting
'''
a=10
print(type(a))
print(a)

a=str(a)
print(type(a))
print(a)

a=float(a)
print(type(a))
print(a)

a=complex(a)
print(type(a))
print(a)

a=12
a=bin(a)
print(type(a))
print(a)

a=list(a)
print(type(a))
print(a)
]
a=tuple(a)
print(type(a))
print(a)


The bin(),hex() and oct() are not directly supported by python hence even if we mention variable in this number systems
we will be able to see a decimal(int) output of print function.
'''
#examples

a1=0b10000     # prints in int form i.e 16
print(a1)
print(type(a1))  

b=16          #convert int into binary i.e 10000
b=bin(b) 
print(b)
print(type(b))  


c=32          #convert into hex i.e 20
c=hex(c)
print(c)
print(type(c))


d=38         #convert into oct i.e 46
d=oct(d)
print(d)
print(type(d))

'''

#if number is directly mentioned as bin(),oct() and hex() still the system will consider it or save it as int only.
#If a number is first mentioned as int and then changed to bin(),oct() or hex() then the type of data is considered as 'str'.
#as bin(),oct() or hex() are not directly supported by python.

a2=0b10000    #16
print(type(a2))

a3=0x1d   #29
print(type(a3))

a4=0o47    #57
print(type(a4))

a5=12    #12
print(type(a5))
'''









