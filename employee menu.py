# added by Diaz, Bryan 11/25/21

granted = False
def grant(): #grant access function
    global granted
    granted = True
def login(username,password):#logging in function
    success = False
    file = open("C:\\Users\\luisi\\Desktop\\Logging System\\employee_username.txt","r")#reads files 
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==username and b==password):
             success = True
             break
    file.close()
    if(success):
        print("")
        print("Login Successful")
        grant()
    else:
        print("")
        print("wrong username or password")
        
        
        
def register(username,password):#Registration function
    file = open("C:\\Users\\luisi\\Desktop\\Logging System\\employee_username.txt","a+")
    file.write("\n"+username+","+password)
    grant()
def access(option):
    global username
    if(option=="login"):
        username = input("Username: ")
        password = input("Password: ")
        login(username,password)
    else:
        print("Enter your username and password to register")
        username = input("Username: ")
        password = input("Password: ")
        register(username,password)
        
        

def begin():# Starts the program if log in successful, begin function
    global option
    print("______________________________________________________")
    print("                                                      ")
    print("Welcome Valued Employee to the Rent Management System!")
    print("______________________________________________________")
    option = input("To Login or Register please type (login or reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
# added by Baxi, Utsav 11/25/21        
begin()
access(option)
if(granted):
    print("Employee Access Menu")
    print("[1] Profile")
    print("[2] Maintenance")

    choice = input("Chose From The Menu Above:")
    
# printed second menu if user chose profile
    if choice == "1":
        print("[1] View Tenant Info")
        print("[2] View Lease Info")
        print("[3] View Employee Info")
        print("[4] Edit Employee Info")
        print("[5] View Payment History")
        print("[6] Exit")

        choice_2 = input("Chose From The Menu Above:")

# missing methods
        if choice_2 == "1":
            pass
        elif choice_2 == "2":
            pass
        elif choice_2 == "3":
            pass
        elif choice_2 == "4":
            pass
        elif choice_2 == "5":
            pass
        elif choice_2 == "6":
            pass
        else:
            print("Invalid Choice")

# To view Maintenance (No Secondary Menu)
    elif choice == "2":
        pass
    else:
        print("Invalid Choice")
