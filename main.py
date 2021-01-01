from Employee import Employee
import hashlib
import os
import re


# This function displays the menu that the user will encounter.
def display_menu():
    print()
    print('Welcome to the Employee Management console. \n Please select from the following Items:')
    print('1: Create new employee \n2: Manage login credentials \n3: Edit availability for employee \n'
          '4: Generate email list \n5: Quit')
    print()


# This function displays the password instructions.
def display_password_instructions():
    print()
    print('We need to set your password, please choose a password with the following:')
    print('Must be a minimum of 8 characters.')
    print('The alphabets must be between [a-z]')
    print('Must have at least one upper case letter')
    print('Must contain at least one number from 0-9')
    print('Must have at least one special character from [ _ or @ or $ ].')
    print()


# This function will cycle through the main menu
def make_menu_decision():
    while True:
        display_menu()
        choice = int(input("Please make your selection: "))
        if choice == 1:  # create new employee
            create_emp()
        elif choice == 2:  # manage login credentials
            create_pass()
        elif choice == 3:  # edit availability
            print("Edit availability for employee")
        elif choice == 4:  # generate email list
            print("Generate email list")
        elif choice ==5:
            print("\nHave a nice day.\n")
            break
        else:
            print("I am sorry; I do not recognize this option")


# This function will add the first and last name to empData file. 
# This will also create and store the email
def create_emp():
    # TODO add logging info
    with open('empData.txt', 'a') as f:
        add_first = input("Enter the employee's first name: ")
        add_last = input("Enter the employee's last name: ")
        new_emp = Employee(add_first, add_last)
        f.write(f'Name: {new_emp.full_name}, Email: {new_emp.email}\n')
        print("Employee successfully added.")


def check_emp_file():
    emp = input("Enter the employee's name: ")

    with open('empData.txt', 'r') as f:
        if emp in f.read():
            return True
        else:
            print("ERROR: No record of that name, please create employee first!")


# Function to create a user password
def create_pass():
    while check_emp_file() is True:
        display_password_instructions()
        password = input('Enter new password: ')
        errors = []  # Initialize this with zero elements. If an error occurs, then add it to array
        if len(password) < 8:
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

        if len(errors) > 0:  # If errors contains ANY elements, then print the errors and loop through again.
            print("The following error(s) occurred.")
            # Print each error using a new line to separate each error
            for error in errors:
                print(error)
        else:
            with open('empPass.txt', 'a') as f:
                user = input("Please enter the name of the employee to be stored: ")
                salt = os.urandom(32)
                key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

                f.write(f'Name: {user}\nSalt: {salt}\nKey: {key}')
            print("Valid password and stored")
            break


# This is the entry point to the application. This is the first line of code that will be executed.
make_menu_decision()

