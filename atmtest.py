from datetime import datetime

now = datetime.now()

import random
import database
import validation
from getpass import getpass


print(now)
def init():

    print("Weclome to RP Bank")

    haveAccount = int(input("Do you have a bank account with us: 1 (yes) 2 (no) \n"))
  
    if(haveAccount == 1):
        login()

  #don't have an account
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")
        #makes password invisible
        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


 #value error- to confirm that the correct account number is being typed
 #check if account_number is not empty
 #if account_number is 10 digits (have to convert to a string in order to check the length)
 #if the account_number is an integer


def register():
    
    print("***********Registeration***********")
    
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n" )
    last_name = input("What is your last name? \n")
    password = getpass("Enter a new password \n")
    balance = int(input("How much money would you like to deposit? \n"))

    account_number = generation_account_number()
    
    is_user_created = database.create(account_number, first_name, last_name, email, password, balance)
    #using database module to create new user record

    if is_user_created:
        print("Your Account Has been created \n")
        print("********************************")
        print("Your account number is %d" % account_number)
        print("********************************")
        
        login()
    else:
        print("Something went wrong, please try again")
        register()

def bank_operation(user, balance):
    print("Welcome %s %s" % (user[0], user[1])) #user[0] = first name
  
    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) log out (4) exit "))

    if(selectedOption == 1):
        depositOperation(user, balance)

    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        print("You have now logged out")
        logout()

    elif(selectedOption == 4):
        exit()

    else:
        print("Invalid option selected")
        bank_operation(user)


def depositOperation(user, balance):
    print("You have selected deposit")
    new_deposit = int(input ('How much would you like to deposit? \n'))
    
    user[5] = set_current_balance(user, balance) + new_deposit
    print ('The current balance is $ %d ' % balance)
    print ('\n')
    additionalOption()
    
# def withdrawalOperation(user):
#     print("You have selected withdrawal" )
#     #get current balance
#     print("Your current balance is %d" % get_current_balance(user[5])
#     cash = int(input('How much would you like to withdraw? \n'))
#     print("Your remaining balance is $ %d" % (get_current_balance(user[5]) - cash)
#     print('Take your cash')
#     print ('\n')
#     additionalOption()

# #get existing balance

def set_current_balance(user, balance):
    user[5] = balance


# def get_current_balance(user_details):
#     return user_details[5]

def generation_account_number():
    return random.randrange(1111111111,9999999999)

def logout():
    login()

def additionalOption(): 
    anythingElse = int(input('Can I help you with something else? Enter (1) yes, (2) No-Exit '))
    if(anythingElse == 1):
        return bank_operation(user)

    elif(anythingElse ==2):
        exit()
    else:
        print("Invalid option selected")
        additionalOption ()


###Actual Banking System ####

init()



