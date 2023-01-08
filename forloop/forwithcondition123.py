'''
#problem 1
#take input from user and print numbers upto entered number.
#also show invalid number if entered number is negative or above 50.

a=int(input("Enter the number : "))
if (a>0) and (a<=50):
    for i in range(1,a+1):
        print(i)
else:
    print("invalid number!!! Enter a positive number from 1 to 50. ")


#problem 2
#take list of 8 names and find whether 'a' includes in each name or not.
#also calculate how many times it has been in the name.

ls=["rohan","samarth","simran","kishor","seema","roy","moksh","ramesh","raja","pratiksha"]
for i in ls:
    if "a" in i:
        print("a is present in "+i)
        s=0
        for j in i:
            if "a" in j:
                s=s+1
        print("a is present for ",s,"times in",i)
    else:
        print("a is not present in "+i)



#problem 3
#take a list of 15 numbers and print even nmbers in the list.
#also mention total count of all even numbers in the list.

ls=[4,61,65,348,246,46,34,64,779,464,8475,2,49,2,978,6,897,8,79,5,7,12,1,6,4]
s=0
p=0
k=0
for i in ls:
    k=k+1
    if i%2==0:
        print(str(i)+" is a even number.")
        s=s+1
    else:
        print(str(i)+" is odd number.")
        p=p+1
print("Total entries in the list are " + str(k))
print("Total even numbers in the list are " + str(s))
print("Total odd numbers in the list are " + str(p))

'''

for i in range(1,5):
    print("outer loop"+str(i))
    for j in range(10,0,-1):
        print("inner loop"+ str(j))




















