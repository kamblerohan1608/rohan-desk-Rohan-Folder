
# Basics of functions

#Without parameters
'''

def add():
    addition=a+b
    print(addition)

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
add()


#with parameters

def sub(a,b):
    print("Substraction is : " , a-b )
sub(50,30)


#default parameters

def percentages(obt,total=500):
    '''#This program is to calculate the percentage using a single input'''
'''
    if obt>total:
        obt,total=total,obt
    print("The percentages are",obt*100/total,"%")
percentages()


#variable length argument 

def add(*args):
    s=0
    for i in args:
        s=s+i
    print("addition is : ",s)

#a=int(input("Enter the number : "))
#b=int(input("Enter the number : "))
    
add(10,20,30,40)


#printing doc string

def percentages(obt,total=500):
    ''' # This program is to calculate the percentage using a single input '''
'''
    print("The percentages are",obt*100/total,"%")
print(percentages.__doc__)

'''

def add():
    a=int(input("Enter the number : "))
    b=int(input("Enter the number : "))
    print("addition is",a+b)

add()














