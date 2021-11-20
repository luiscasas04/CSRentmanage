
from _typeshed import Self

class Apartment:
    #Type of apartment and rent price
    def __init__(self, modelNum,rentPrice, squareFeet, apartmentNum, numOfRooms):
        self.model = modelNum
        self.rent = rentPrice
        self.squareft = squareFeet
        self.apartmentNumber = apartmentNum
        self.numberOfRooms = numOfRooms

        
class ManageRenter:
    renter_name = None
    age = None
    gender = None
    def __init__(self, renter_name, age, gender ):
        self.renter_name = renter_name
        self.age = age
        self.gender = gender



class Repair:
    #request maintenace repairs
    dateOfRepair = None
    renter_name = None
    apartment_number = None
    
    def __init__(self, renter_name , apartment_number, dateOfRepair ):
        self.name = renter_name
        self.apt = apartment_number
        self.date = dateOfRepair


class ManagePayment:
    #payment history
    renter_name = None
    payment = None
    def __init__(self, renter_name ):
        self.renter_name = renter_name

    def getPayement(self, payment):
        self.payment = payment


class Message:
    def __init__(self, renter_name ):
        self.renter_name = renter_name


class RenterApplication:
    #see a list of renter applications
    def __init__(self, renter_name ):
        self.renter_name = renter_name




class ManageEmployee:
    age = None
    gender = None
    employee_name = None
    def __init__(self, employee_name, age , gender ):
        self.employee_name = employee_name
        self.age = age
        self.gender = gender



class EditEmployee:
    employee_name = None
    def getEmployee(self, ManageEmployee):
        ManageEmployee.employee_name






class EditRenter:
    def __init__(self, renter_name ):
        self.renter_name = renter_name
    




class Repair:
    def __init__(self, renterName ):
        self.renter_name = renterName

    



# class Reminder:
class Reminder:
    def emailReminder(self,email_confirmation):
        self.email_reminder = email_confirmation
        
    def textReminder(self, text_confirmation):
        self.text = text_confirmation
    
    def mailReminder(self, mail_confirmation):
        self.mail = mail_confirmation

class Employee:
    def __init__(self, name,lastname, email):
        self.first_name = name
        self.last_name = lastname
        self.employee_email = email
    
    
   


    def add_employee(self, employee_name, age, gender):
        self.employee_name = employee_name
        self.age = age
        self.gender = gender
        print("New Resident "+ employee_name +  " is added")
        



class MaintenanceRecord:
    renter_name = None
    def __init__(self, renter_name ):
        self.renter_name = renter_name
        




class MakePayment:
    renter_name = None
    payment = None
    def __init__(self, renter_name, payment):
        self.renter_name = renter_name
        self.payment = payment
        

    def make_payment( payment):
        RENT = 1000.00
        if payment is RENT:
            print(" Payment Accepted.")
        else:
            print("Payment accepted, you still owe some money")



class PayementHistory:
    renter_name = None
    def __init__(self, renter_name ):
        self.renter_name = renter_name



class DenyApplication:
    renter_name = None
    def __init__(self, renter_name ):
        self.renter_name = renter_name

    




class AcceptApplication:
    def __init__(self, renter_name ):
        self.renter_name = renter_name

    def addResident(Resident_name):
        print("Congratulations, "+ Resident_name.renter_name +"'s application was accepted" )

#########################
