# added by Casas, Luis 11/26/21

import runpy #locates programs

#screen selection
print("                     Welcome!                ")
print("[1] Landlord")
print("[2] Employee")
print("[3] Resident")
    
    
choice = input("Please choose from the following selection (1 - 3): ")
    
if choice == "1":
    runpy.run_path("landlord menu.py" , run_name='__main__')#landlord menu.py file
elif choice =="2":
    runpy.run_path("employee menu.py" , run_name='__main__')#employee menu.py file
            
elif choice =="3":
     runpy.run_path("resident menu.py" , run_name='__main__')#resident menu.py file
        
        
else:
            print("Wrong Selection")
        
