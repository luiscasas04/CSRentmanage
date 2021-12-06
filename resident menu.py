# added by Diaz, Bryan 11/26/21
# Resident Login verfication functions defined 

granted = False
def grant(): #grant access function
    global granted
    granted = True
def login(username,password):#logging in function
    success = False
    file = open("C:\\Users\\luisi\\Desktop\\Logging System\\resident_username.txt","r")#reads files 
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
    file = open("C:\\Users\\luisi\\Desktop\\Logging System\\resident_username.txt","a+")
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
    print("___________________________________________________")
    print("                                                   ")
    print("Welcome Valued Resident the Rent Management System!")
    print("___________________________________________________")
    option = input("To Login or Register please type (login or reg): ")
    if(option!="login" and option!="reg"):
        begin()

# added by Baxi, Utsav 11/26/21
# menu options presented at log in
begin()
access(option)

if(granted):# menu for resident and choices
    print("")
    print("Welcome: ",username)
    print("")
    print("Please choose a selection:")
    print("")
    print("Resident Access Menu")
    print("[1] Profile")
    print("[2] Payment")
    print("[3] Maintenance")
    print("[4] Exit")

# take user input
    choice = input("Choose From The Menu (1-4):")

# printed menu if user chose profile
    if choice == "1":
        print("[1] View Personal Info")
        print("[2] Update Personal Info")
        print("[3] View Lease Info")
        print("[4] View Insurance Info")
        print("[5] View Reminders")

        choice_2 = input("Choose From The Menu above:")

# methods missing here
        if choice_2 == "1":
            pass
        elif choice_2 == "2":
            pass
        elif choice_2 == "3":
            pass
        elif choice_2 == "4":
            pass
        else:
            print("Invalid Choice")

# printed second menu if user picked payment
    elif choice == "2":
        print("[1] View Payment")
        print("[2] Make Payment")
        print("[3] Change Payment Date")
        print("[4] Change Payment Method")

        choice_2 = input("Choose From The Menu above:")

# missing methods here
        if choice_2 == "1":
            pass
        elif choice_2 == "2":
            pass
        elif choice_2 == "3":
            pass
        else:
            print("Invalid Choice")

# printed second menu if user picked maintenance
    elif choice == "3":
        print("[1] Send Maintenance Request")
        print("[2] View Maintenance Request Status")

        choice_2 = input("Choose From The Menu above:")

# missing methods
        if choice_2 == "1":
            pass
        elif choice_2 == "2":
            pass
        else:
            print("Invalid Choice")

    elif choice == "4":
        quit()

    else:
        print("Invalid Choice")
    
