
# main

from new import sign_in,log_in

def front():
    print('''
    *****************************************************************************
    *                      Welcome to the Application 3                         *
    *****************************************************************************

     -----------------------
    |  Sign up  :  Press 1  |
     -----------------------
     -----------------------
    |  log in   :  Press 2  |
     -----------------------
     -----------------------
    |  exit     :  Press 3  |
     -----------------------
    ''')
front()
print()
while True:
    ch = int(input("Enter your choice : "))
    if ch==1:
        d = sign_in.sign_up()
        front()
        print()
    elif ch== 2:
        d = log_in.log_in()
        c = "" 
        if (type(d) == type(c)):
            print(d)
            print("\n\n Enjoy your games...\n -------------------\n\n")
            break
        else:
            print("\nInvalid id or password.\nTry Again...\n")
            front()
            print()
    elif ch ==3 :

        print('''
          ****************************************
        *         Thank You...Visit Again          *
          ****************************************
        ''')
        break
    else:
        print("******Invalid Input...Try Again******")

