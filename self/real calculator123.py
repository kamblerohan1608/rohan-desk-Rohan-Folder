

from glob import glob


def sign ():
    global k
    if act == "+":
        k=a+b
        print(k)
    elif act == "-":
        k=a-b
        print(k)
    elif act == "*":
        k=a*b
        print(k)
    elif act == "/":
        k=a/b
        print(k)
    elif act =="^":
        k=a**b
        print(k)


s=0

def main():
    global s
    if s == 0:
        global a
        a=int(input("Enter the number : "))
        global act
        i=1
        while i != 0 :

            act= input("Enter the sign : ")
            global ls
            ls=["+","-","*","/","^"]
            if act in ls or act == "c" or act == "C":
                break
            
            else:
                print("invalid input")
        if act == "c" or act =="C":
            s=0
        else:

            global b
            b=int(input("Enter the number : "))
            sign()
            s=1

    else:
        a=k
        i=1
        while i != 0 :

            act= input("Enter the sign : ")
            if act in ls or act =="c" or act == "C":
                break
            
            else:
                print("invalid input")
        if act =="c" or act =="C":
            s=0
        else :
            b=int(input("Enter the number : "))
            sign()

while True:

    main()
        


