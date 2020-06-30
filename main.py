from Employee import Employee
import os
import re
import logging

# This function displays the menu that the user will encounter.
def display_menu():
    print()
    print('Welcome to the Employee Management console. \n Please select from the following Items:')
    print('1: Create new employee \n2: Manage login credentials \n3: Edit availability for employee \n4: Generate email list \n5: Quit')
    print()

#This function displays the password instructions.
def display_password_instructions():
    print()
    print('We need to set your password, please choose a password with the following:')
    print('Must be a minimum of 8 characters.')
    print('The alphabets must be between [a-z]')
    print('Must have at least one upper case letter')
    print('Must contain at least one number from 0-9')
    print('Must have at least one special character from [ _ or @ or $ ].')
    print()

#This function will cycle through the menu 
def make_menu_decision():
    while True:
        display_menu()
        choice = int(input("Please make your selection: "))
        if choice == 1: #create new employee
            create_emp()
        elif choice == 2: #manage login credentials
            create_pass()
        elif choice == 3: #edit availability
            print("Edit availability for employee")
        elif choice == 4: #generate email list
            print("Generate email list")
        elif choice ==5:
            print("\nHave a nice day.\n")
            break
        else:
            print("I am sorry; I do not recognize this option")
            
# This function will add the first and last name to empData file.
def create_emp():
    # TODO add logging info
    with open('empData.txt', 'a') as f:
        addFirst = input("Enter the employee's first name: ")
        addLast = input("Enter the employyee's last name: ")
        newEmp = Employee(addFirst, addLast)
        f.write(f'Name: {newEmp.full_name}, Email: {newEmp.email}\n')
        print("Name successfully added.")

#Function to create a user password
def create_pass():
        
        while True:
            display_password_instructions()
            password = input('Enter new password: ')
            errors = []  # Initialize this with zero elements. If an error occurs, then add it to array
            if (len(password) < 8):
                    errors.append("Password length must be above 8 characters.")
            if not re.search("[a-z]", password):
                errors.append("Password must contain at least one lowercase letter.")
            if not re.search("[A-Z]", password):
                errors.append("Password must contain at least one uppercase letter.")
            if not re.search("[0-9]", password):
                errors.append("Password must contain at least one number.")
            if not re.search("[_@$]", password):
                errors.append("Password must contain at least one special character.")
            # This enables an error if any whitespace characters are detected. I don't think it's used correctly, though.
            # String constants need an 'r' prefix, so I think it should be (r"\s", password)
            if re.search("\s", password):
                errors.append("No whitespace characters are allowed.")

            if (len(errors) > 0):  # If errors contains ANY elements, then print the errors and loop through again.
                print("The following error(s) occured.")
                # Print each error using a new line to separate each error
                for error in errors:
                    print(error)
            else:
                print("Valid password and stored")
                break
                

# This is the entry point to the application. This is the first line of code that will be executed.
make_menu_decision()

#FINAL NOTES
# Don't be afraid to create multiple functions. Each function should do 1 and only 1 thing. This makes it
# easier to test. If you have a function that does 5 things and it doesn't work, what doesn't work? Is it
# the first thing, the second thing, etc. I would have a function that only stores the password and that's all that it does.
# You can call it once password verification is completed. Also, try not to have a function call another function unless it returns to it at the exact place.
# For example, any function that calls display_menu() does that and returns to the place it left off immediately.
# Good luck.