
class Entry:
    def sign_up(self,f_name,l_name,age,email,password):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.email = email
        self.password = password
        with open("test1.txt","a") as file:
            data = (self.f_name + ',' + self.l_name + ',' +str(self.age) + ','+ self.email + ',' + self.password + '\n')
            file.write(data)
        print("\nSigned up Successfully...")

    def log_in(self,email,password):
        self.email = email
        self.password = password
        with open("test1.txt","r") as file:
            data = file.readlines()
        data_new = []
        for i in data:
            i = i.replace('\n','')
            data_new.append(i)
        # print(data_new)
        self.all_info = []
        for i in data_new:
            i = i.split(',')
            self.all_info.append(i)
        # print(self.all_info)
        for i in self.all_info:
            if (self.email in i ):
                if self.password in i :
                    return (f'''
                     ---------------------------------------------------
                    |       Welcome to the application {i[0].capitalize()}...        |
                     ---------------------------------------------------
                    ''')


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
        f_name = input("Enter your first name : ")
        l_name = input("Enter your last name : ")
        age = int(input("Enter your age : "))
        while True:    
            email = input("Enter the mail : ")
            with open("test1.txt","r") as file:
                data = file.readlines()
            #print(data)
            data_1 = []
            for i in data:
                i = i.replace('\n','')
                data_1.append(i)
            #print(data_1)
            data_1 = ','.join(data_1)
            #print(data_1)
            data_2 = data_1.split(',')
            #print(data_2)
            if "@" not in email:
                print("'@' is missing in the mail Id. Try again..")
            elif "." not in email:
                print("'.' is missing in mail Id. Try again..")
            elif email in data_2:
                print("Email already exists....Try another one...")
            else:
                break
        while True:
            password = input("Enter the password : ")
            if len(password) > 4:
                break
            else:
                print("Password must be more than 4 characters. Try again..")

        d = Entry()
        d.sign_up(f_name,l_name,age,email,password)
        print("You can log in now...")
        front()
        print()

    elif ch== 2:
        while True:    
            email_1 = input("Enter the mail : ")
            if "@" in email_1 and "." in email_1:
                break
            elif "@" not in email_1:
                print("'@' is missing in the mail Id. Try again..")
            elif "." not in email_1:
                print("'.' is missing in mail Id. Try again..")
        while True:
            password_1 = input("Enter the password : ")
            if len(password_1) > 4:
                break
            else:
                print("Password must be more than 4 characters. Try again..")

        d = Entry()
        D = d.log_in(email_1,password_1)
        c = "" 
        if (type(D) == type(c)):
            print(D)
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
