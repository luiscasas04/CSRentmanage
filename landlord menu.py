# added by Diaz, Bryan 11/26/21
# Landlord Login Verifcation function
granted = False
def grant(): #grant access function
    global granted
    granted = True
def login(username,password):#logging in function
    success = False
    file = open("C:\\Users\\luisi\\Desktop\\Logging System\\landlord_username.txt","r")#reads files 
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
    file = open("C:\\Users\\luisi\\Desktop\\Logging System\\landlord_username.txt","a+")
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
    print("_______________________________________________")
    print("                                               ")
    print("Welcome Landlord to the rent management system!")
    print("_______________________________________________")
    option = input("To Login or Register please type (login or reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
# added by Baxi, Utsav 11/25/21 
begin()
access(option)

if(granted):
    print("Landlord Access Menu")
    print("[1] Profile")
    print("[2] Maintenance")

    choice = input("Chose From The Menu Above")

# printed menu if user chooses profile
    if choice == "1":
        print("[1] View Lease Info")
        print("[2] Edit Lease Info")
        print("[3] View Tenant Info")
        print("[4] Edit Tenant Info")
        print("[5] Add Tenant")
        print("[6] Remove Tenant")
        print("[7] View Employee Info")
        print("[8] Edit Employee Info")
        print("[9] Add Employee")
        print("[10] Remove Employee")
        print("[11] View Payment History")
        print("[12] Exit")

        choice_2 = input("Chose from the menu above: ")

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
        elif choice_2 == "7":
            pass
        elif choice_2 == "8":
            pass
        elif choice_2 == "9":
            pass
        elif choice_2 == "10":
            pass
        elif choice_2 == "11":
            pass
        elif choice_2 == "12":
            pass
        else:
            print("Invalid Choice")

# printed menu if user chose maintenance
    elif choice == "2":
        print("View Maintenance Request")
        print("Approve/Deny Maintenance Request")

        choice_2 = input("Chose from the menu above")

# missing methods
        if choice_2 == "1":
            pass
        elif choice_2 == "2":
            pass
        else:
            print("Invalid Choice")

    else:
        print("Invalid Choice")
