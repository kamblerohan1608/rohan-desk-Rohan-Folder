
def sign_up():
    with open("test2.txt","a") as file:
        first_name = input("Enter your first name : ")
        last_name = input("Enter your last name : ")
        age = input("Enter your age : ")
        while True:    
            id = input("Enter the mail : ")
            if "@" in id and "." in id:
                break                        
            elif "@" not in id:
                print("'@' is missing in the mail Id. Try again..")
            elif "." not in id:
                print("'.' is missing in mail Id. Try again..")
        while True:
            password = input("Enter the password : ")
            if len(password) > 4:
                break
            else:
                print("Password must be more than 4 characters. Try again..")
        
        file.write(f"{first_name},{last_name},{age},{id},{password}\n")
    print("\nSigned Up Successfully....\nYou can log in now....")

def log_in():
    with open("test2.txt","r") as file:
        data = file.readlines()
    #print(data)
    main = []
    for i in data:
        i = i.replace("\n","")
        main.append(i)
    #print(main)
    global main1
    main1 = []
    for i in main:
        j = i.split(",")
        main1.append(j)
    #print(main1)
    while True:    
        id_1 = input("Enter the mail : ")
        if "@" in id_1 and "." in id_1:
            break
        elif "@" not in id_1:
            print("'@' is missing in the mail Id. Try again..")
        elif "." not in id_1:
            print("'.' is missing in mail Id. Try again..")
    while True:
        password1 = input("Enter the password : ")
        if len(password1) > 4:
            break
        else:
            print("Password must be more than 4 characters. Try again..")
    
    for i in main1:
        if password1 in i and id_1 in i :
            name = i[0]
            global wel
            print(f"\nWelcome to the application {name.capitalize()} ...")
            wel = 1

def front():
    print('''
    -------------------- Welcome to the Application ------------------------

    Sign up  :  Press 1
    log in   :  Press 2
    exit     :  Press 3''')
front()
print()
while True:
    ch = int(input("Enter your choice : "))
    if ch==1:
        sign_up()
        front()
        print()
    elif ch== 2:
        wel = 0
        log_in()
        if wel == 1:
            print("\n\n Enjoy your games...\n\n")
            break
        else:
            print("\nInvalid id or password.\nTry Again...")
            front()
            print()
    elif ch ==3 :

        print("\n------ Thank You...Visit Again -------\n")
        break
    else:
        print("******Invalid Input...Try Again******")
