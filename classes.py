
from _typeshed import Self
import smtplib
from email.message import EmailMessage

class Employee:
    # initialize the attributes
    def __init__(self,  employee_ID, employee_name, employee_age, employee_gender):
        self.employee_ID = employee_ID
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_gender = employee_gender

    # set the attribute 
    def set_id(self, employee_ID):
        self.employee_ID = employee_ID
        
    def set_name(self, employee_name):
        self.employee_name = employee_name

    def set_age(self, employee_age):
        self.employee_age = employee_age

    def set_gender(self, employee_gender):
        self.employee_gender = employee_gender

    # return the attributes
    def get_id(self):
        return self.employee_ID
    
    def get_name(self):
        return self.employee_name

    def get_age(self):
        return self.employee_age

    def get_gender(self):
        return self.employee_gender

    # return the objects state as a string
    def __str__(self):
        return 'ID Number: ' + self.employee_ID + \
               '\nName: ' + self.employee_name + \
               '\nAge: ' + self.employee_age + \
               '\nGender: ' + self.employee_gender


#################################################


class Resident:
    # initialize the attributes
    def __init__(self, resident_apt_num, resident_name, resident_age, resident_ID, resident_gender, resident_password,):
        self.resident_apt_num = resident_apt_num
        self.resident_name = resident_name
        self.resident_age = resident_age
        self.resident_ID = resident_ID
        self.resident_gender = resident_gender

    # set the attributes
    def set_apt_num(self, resident_apt_num):
        self.resident_apt_num = resident_apt_num
    
    def set_name(self, resident_name):
        self.resident_name = resident_name

    def set_id(self, resident_ID):
        self.resident_ID = resident_ID

    def set_age(self, resident_age):
        self.employee_age = employee_age

    def set_gender(self, resident_gender):
        self.resident_gender = resident_gender
        
    def set_password(self, resident_password):
        self.resident_password = resident_password

    # return the attributes
    def get_apt_num(self):
        return self.resident_apt_num
    
    def get_name(self):
        return self.resident_name

    def get_age(self):
        return self.resident_age

    def get_id(self):
        return self.resident_ID

    def get_gender(self):
        return self.resident_gender
        
            
    def get_password(self):
       return self.resident_password
   
   def edit_resident(self, resident_apt_num, resident_name, resident_age, resident_ID, resident_gender, resident_password):
       self.resident_apt_num = resident_apt_num
       self.resident_name = resident_name
       self.resident_age = resident_age
       self.resident_ID = resident_ID
       self.resident_gender = resident_gender
       self.resident_password = resident_password
       print("You have succesfully updated:" + self.resident_name)

    # return the objects state as a string
    def __str__(self):
        return 'Apartment: ' + self.resident_apt_num + \
               '\nName: ' + self.resident_name + \
               '\nID number: ' + self.resident_ID + \
               '\nAge: ' + self.resident_age + \
               '\nGender: ' + self.resident_gender


###################################
class Landlord:
    # initialize landlord attributes
    def __init__(self, landlord_name, landlord_age, landlord_ID, landlord_gender):
        self.landlord_name = landlord_name
        self.landlord_age = landlord_age
        self.landlord_ID = landlord_ID
        self.landlord_gender = landlord_gender

    # set the attributes
    def set_name(self, landlord_name):
        self.landlord_name = landlord_name

    def set_id(self, landlord_ID):
        self.landlord_ID = landlord_ID

    def set_age(self, landlord_age):
        self.landlord_age = landlord_age

    def set_gender(self, landlord_gender):
        self.landlord_gender = landlord_gender

    # return the attributes
    def get_name(self):
        return self.landlord_name

    def get_age(self):
        return self.landlord_age

    def get_id(self):
        return self.landlord_ID

    def get_gender(self):
        return self.landlord_gender

    # return the objects state as a string
    def __str__(self):
        return 'Name: ' + self.landlord_name + \
               '\nID number: ' + self.landlord_ID + \
               '\nAge: ' + self.landlord_age + \
               '\nGender: ' + self.landlord_gender


##################################

class Apartment:
    # initialize the apartment attributes
    def __init__(self, apartment_number, flat_size, number_of_bedrooms):
        self.apartment_number = apartment_number
        self.flat_size = flat_size
        self.number_of_bedrooms = number_of_bedrooms

    # set the attributes
    def set_apartment_number(self, apartment_number):
        self.apartment_number = apartment_number

    def set_flat_size(self, flat_size):
        self.flat_size = flat_size

    def set_number_of_bedrooms(self, number_of_bedrooms):
        self.number_of_bedrooms = number_of_bedrooms

    # return the attributes
    def get_apartment_number(self):
        return self.apartment_number

    def get_flat_size(self):
        return self.flat_size

    def get_number_of_bedrooms(self):
        return self.number_of_bedrooms

    # return the objects state as a string
    def __str__(self):
        return 'Apartment Number: ' + self.apartment_number + \
               '\nFlat Size: ' + self.flat_size + \
               '\nNumber Of Bedrooms: ' + self.number_of_bedrooms


##########################

class Lease:

    def __init__(self, leaseID, lengthOfLease, securityDeposit, endOfLease):
        self.leaseID = leaseID
        self.lengthOfLease = lengthOfLease
        self.securityDeposit = securityDeposit
        self.endOfLease = endOfLease

    # set the attributes
    def set_leaseID(self, leaseID):
        self.leaseID = leaseID

    def set_lengthOfLease(self, lengthOfLease):
        self.lengthOfLease = lengthOfLease

    def set_securityDeposit(self, securityDeposit):
        self.securityDeposit = securityDeposit

    def set_endOfLease(self, endOfLease):
        self.endOfLease = endOfLease

    # return the attributes
    def get_leaseID(self):
        return self.leaseID

    def get_lengthOfLease(self):
        return self.lengthOfLease

    def get_securityDeposit(self):
        return self.securityDeposit

    def get_endOfLease(self):
        return self.endOfLease

    # return the objects state as a string
    def __str__(self):
        return 'Lease ID: ' + self.leaseID + \
               '\nLength of Lease: ' + self.lengthOfLease + \
               '\nSecurity Deposit: ' + self.SecurityDeposit + \
               '\nEnd Of Lease: ' + self.endOfLease


class Rent:

    def __init__(self, rentInfo, paymentDueDate, paymentHistory):

        self.rentInfo = rentInfo
        self.paymentDueDate = paymentDueDate
        self.paymentHistory = paymentHistory

        # set the attributes
    def set_rentInfo(self, rentInfo):
        self.rentInfo = rentInfo

    def set_paymentDueDate(self, paymentDueDate):
        self.paymentDueDate = paymentDueDate

    def set_PaymentHistory(self, securityDeposit):
        self.securityDeposit = securityDeposit

        # return the attributes

    def get_rentInfo(self):
        return self.rentInfo

    def get_paymentDueDate(self):
        return self.paymentDueDate

    def get_paymentHistory(self):
        return self.paymentHistory

    # return the objects state as a string

    def __str__(self):
        return 'Rent Info: ' + self.rentInfo + \
               '\nPayment Due Date: ' + self.paymentDueDate + \
               '\nPayment History: ' + self.paymentHistory


class reminder:
    

   options = {
        'A': 'Regular reminder',
        'B': 'Email reminder',
        'C': 'Text message reminder'
            }

   for option, description in options.items():
        print(f'{option}) {description}')

   choice = input('Please choose an option: ')

   if choice in options:
        print(f'You have chosen a {options[choice]}')

   else:
        print(f'Unknown option {choice}')
    
 
   def email_alert(subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg["subject"] = subject
        msg["to"] = to

        user = "rentmanagement10@gmail.com"
        msg["from"] = user
        password = "xeiikjzehifdhkep"

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        server.login(user, password)
        server.send_message(msg)
        server.quit()

   if __name__ == '__main__':
        email_alert("Rent Payment Reminder", "Hi,  just a friendly reminder that your rent is due, please make a payment before the end of the month or a late charge of $50.00 will occur.              Thank you,                                                        Management.", "luis.ivan.casas@gmail.com")

   def send_sms_via_email(subject, body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg["subject"] = subject
        msg["to"] = to

        user = "rentmanagement10@gmail.com"
        msg["from"] = user
        password = "kjhgqnkjalernabf"

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        server.login(user, password)
        server.send_message(msg)
        server.quit()

   if __name__ == '__main__':
        email_alert("Rent Payment Reminder", " Hi,  just a friendly reminder that your rent is due, please make a payment before the end of the month or a late charge of $50.00 will occur.              Thank you,                                                        Management.", "8329092803@tmomail.net")

   def snail_mail(s):

            print("please email management @ rentmanagement10@gmail.com for regular mail reminder", s)


   def invalid_selection():
            print("invalid selection, please try again")
        
###########################################################################

 class AddResident(Resident):
 
   #AddResident is a a child class derived from Resident class so we pass the attributes from __init__(self):
   def __init__(self, resident_name, resident_age, resident_ID, resident_gender):
       Employee.__init__(resident_name, resident_age, resident_ID, resident_gender)

   #function to add a new instance of employee; then will print out to cofirm success
   def add_resident(self, resident_name, resident_age, resident_ID, resident_gender):
       self.resident_name = resident_name
       self.resident_age = resident_age
       self.resident_ID = resident_ID
       self.resident_gender = resident_gender
       print("You have succesfully added:" + self.resident_name)

   #function to remove the instance that is called
   def remove_resident(self):
       print("You have successfully removed resident:" + self.resident_name)
       del self.resident_name
       del self.resident_age
       del self.resident_ID
       del self.resident_gender

   #function to update the contents of a instance
   def edit_resident(self, new_resident_name, new_resident_age, new_resident_ID, new_resident_gender):
       self.resident_name = new_resident_name
       self.resident_age = new_resident_age
       self.resident_ID = new_resident_ID
       self.resident_gender = new_resident_gender
       print("You have succesfully updated:" + self.resident_name)
 
        
        
class Insurance:
    insurance_name = None
    expiration = None
    paid = None
    def __init__(self, insurance_name, expiration, paid ):
        self.insurance_name = insurance_name
        self.insurance_expiration = insurance_expiration
        self.insurance_paid = insurance_paid
        
       #function to remove the instance that is called
   def remove_insurance(self):
       print("You have successfully removed insurance:" + self.insurance_name)
       del self.insurance_name
       del self.insurance_expiration
       del self.insurance_paid
     

   #function to update the contents of a instance
   def edit_insurance(self, insurance_name, insurance_expiration, insurance_paid):
       self.insurance_name = insurance_name
       self.insurance_expiration = insurance_expiration
       self.insurance_paid = insurance_paid
       print("You have succesfully updated:" + self.insurance_name)
 



###########################################################################
        class Employee:
    # initialize the attributes
    def __init__(self, employee_name, employee_age, employee_ID, employee_gender):
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_ID = employee_ID
        self.employee_gender = employee_gender

    # set the attributes
    def set_name(self, employee_name):
        self.employee_name = employee_name

    def set_id(self, employee_ID):
        self.employee_ID = employee_ID

    def set_age(self, employee_age):
        self.employee_age = employee_age

    def set_gender(self, employee_gender):
        self.employee_gender = employee_gender

    # return the attributes
    def get_name(self):
        return self.employee_name

    def get_age(self):
        return self.employee_age

    def get_id(self):
        return self.employee_ID

    def get_gender(self):
        return self.employee_gender

    # return the objects state as a string
    def __str__(self):
        return 'Name: ' + self.employee_name + \
               '\nID number: ' + self.employee_ID + \
               '\nAge: ' + self.employee_age + \
               '\nGender: ' + self.employee_gender


#################################################

class Apartment:
    # initialize the apartment attributes
    def __init__(self, apartment_number, flat_size, number_of_bedrooms):
        self.apartment_number = apartment_number
        self.flat_size = flat_size
        self.number_of_bedrooms = number_of_bedrooms

    # set the attributes
    def set_apartment_number(self, apartment_number):
        self.apartment_number = apartment_number

    def set_flat_size(self, flat_size):
        self.flat_size = flat_size

    def set_number_of_bedrooms(self, number_of_bedrooms):
        self.number_of_bedrooms = number_of_bedrooms

    # return the attributes
    def get_apartment_number(self):
        return self.apartment_number

    def get_flat_size(self):
        return self.flat_size

    def get_number_of_bedrooms(self):
        return self.number_of_bedrooms

    # return the objects state as a string
    def __str__(self):
        return 'Apartment Number: ' + self.apartment_number + \
               '\nFlat Size: ' + self.flat_size + \
               '\nNumber Of Bedrooms: ' + self.number_of_bedrooms

######################################################################

class MonthlyPayment(Apartment):
    def __init__(self, apartment_number, flat_size, number_of_bedrooms, payment, price, date):
        Apartment.__init__(self, apartment_number, flat_size, number_of_bedrooms)
        self.payment = payment
        self.price = price
        self.date = date

    def montly_payment(self):
        if self.payment == self.price:
            print("You have succesfully paid your rent.")
        else:
            print("You still have to pay: " + (self.price - self.payment))

    def change_pay_date(self, change_date):
        self.date = change_date

###########################################################

class AddEmployee(Employee):
   #AddEmploye is a a child class derived from Employee so we pass the attributes from __init__(self):
   def __init__(self, employee_name, employee_age, employee_ID, employee_gender):
       Employee.__init__(employee_name, employee_age, employee_ID, employee_gender)

   #function to add a new instance of employee; then will print out to cofirm success
   def add_employee(self, employee_name, employee_age, employee_ID, employee_gender):
       self.employee_name = employee_name
       self.employee_age = employee_age
       self.employee_ID = employee_ID
       self.employee_gender = employee_gender
       print("You have succesfully added:" + self.employee_name)

   #function to remove the instance that is called
   def remove_employee(self):
       print("You have successfully removed employee:" + self.employee_name)
       del self.employee_name
       del self.employee_age
       del self.employee_ID
       del self.employee_gender

   #function to update the contents of a instance
   def edit_employee(self, new_employee_name, new_employee_age, new_employee_ID, new_employee_gender):
       self.employee_name = new_employee_name
       self.employee_age = new_employee_age
       self.employee_ID = new_employee_ID
       self.employee_gender = new_employee_gender
       print("You have succesfully updated:" + self.employee_name)

###########################################################

class MaintenanceRecord:
    #initialize attributes
    def __init__(self, date, type_of_repair, apt_number, firstName, lastName):
        self.date = date
        self.type_of_repair = type_of_repair
        self.apt_number = apt_number
        self.firstname = firstName
        self.lastName = lastName

    #set attributes
    def set_date(self, date):
        self.date =date

    def set_type_of_repair(self, type_of_repair):
        self.type_of_repair = type_of_repair

    def set_apt_number(self, apt_number):
        self.apt_number=apt_number

    def set_firtName(self, firstName):
        self.firstname=firstName

    def set_lastName(self, lastName):
        self.lastName=lastName

    #get atrributes
    def get_date(self):
        return self.date

    def get_type_of_repair(self):
        return self.type_of_repair

    def get_apt_number(self):
        return self.apt_number

    def get_firstName(self):
        return self.firstname

    def get_lastName(self):
        return self.lastName

#############################################################

class ManageMaintenance(MaintenanceRecord):
    #initialize attributes
    def __init__(self, date, type_of_repair, apt_number, firstName, lastName):
        MaintenanceRecord.__init__(self, date, type_of_repair, apt_number, firstName, lastName)

    def view_resident_request(self):
        print(self.date)
        print(self.type_of_repair)
        print(self.apt_number)
        print(self.firstname)
        print(self.lastName)

    def edit_resident_request(self, new_date, new_type_of_repair, new_apt_number, new_firstName, new_lastName):
        self.date = new_date
        self.type_of_repair = new_type_of_repair
        self.apt_number = new_apt_number
        self.firstname = new_firstName
        self.lastName = new_lastName
        print("You have succesdfully edit request: " + self.firstname)

    def remove_resident_request(self):
        print("You have succesfully deleted request from " + self.firstname + " " + self.lastName)
        del self.date
        del self.type_of_repair
        del self.apt_number
        del self.firstname
        del self.lastName
