from Employee import Employee
import re 
import os
import logging

#Function to get the users action selction
def get_selection():
    choice = int(input("Please make your selection: "))

    if choice == 1:
        createEmp()
    elif choice == 2:
        createPass()
    elif choice == 3:
        print("Edit availability for employee")
    elif choice == 4:
        print("Generate email list")
    elif choice == 5:
        print("Quit")
    else:
        return choice

# Function to add an employee
def createEmp():
    # TODO add logging info

    with open('empData.txt', 'a') as f:
        addFirst = input("Enter the employee's first name: ")
        addLast = input("Enter the employyee's last name: ")

        newEmp = Employee(addFirst, addLast)
        f.write(f'Name: {newEmp.full_name}, Email: {newEmp.email}\n')
    
    get_selection()

# Function to create a user password
def createPass():
    empPassInstruction()
    
    password = input('Enter new password: ')
    flag = 0
    while True: 
        if (len(password)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[_@$]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            print("Valid Password")
            break

    if flag ==-1: 
        print("Not a Valid Password")

    get_selection()

def empPassInstruction():
    print('We need to set your password, please choose a password with the following:')
    print('Must be a minimum of 8 characters.')
    print('The alphabets must be between [a-z]')
    print('Must have at least one upper case letter')
    print('Must contain at least one number from 0-9')
    print('Must have at least one special character from [ _ or @ or $ ].')

print('Welcome to the Employee Management console. \n Please select from the following Items:')
print('1: Create new employee \n2: Manage login cradentials \n3: Edit availability for employee \n4: Generate email list \n5: Quit')

get_selection()
