import csv
import sys
import time
import os
import random
from getpass import getpass
import colorama
from colorama import Fore
from rich.console import Console
from rich.text import Text
console= Console()

#Banners for the project
def banner():

    a = '''
     ██████     ███    ███ 
    ██          ████  ████ 
    ██ ontact   ██ ████ ██ anagement 
    ██          ██  ██  ██ 
     ██████     ██      ██ 
    '''

    b = '''
     ______      __    __   
    /\  ___\    /\ "-./  \  
    \ ontact_   \ anagement  
     \ \_____\   \ \_\ \ \_\ 
      \/_____/    \/_/  \/_/

    '''
    c = '''
     .o88b.    .88b  d88. 
    d8P  Y8    88'YbdP`88 
    8P         88  88  88 
    8b         88  88  88 
    Y8b  d8    88  88  88 
     `Y88P'    YP  YP  YP 
    Contact    Management                
    '''

    d = '''
    ============================
    ===     ======  =====  ===
    ==  ===  =====   ===   ===
    =  ===========  =   =  ===
    =  ===========  == ==  ===
    =  ===========  =====  ===
    =  ===========  =====  ===
    =  ===========  =====  ===
    ==  ===  =====  =====  ===
    ===     ======  =====  ===
    ============================
       Contact     Management
    '''

    e = '''
      /$$$$$$      /$$      /$$
     /$$__  $$    | $$$    /$$$
    | $$  \__/    | $$$$  /$$$$
    | $$          | $$ $$/$$ $$
    | $$          | $$  $$$| $$
    | $$    $$    | $$\  $ | $$
    |  $$$$$$/    | $$ \/  | $$
     \______/     |__/     |__/
      Ontact        anagement                           
    '''
    banner_list = [a,b,c,d,e]
    random_num = random.randint(0,4)
    print(Fore.WHITE,banner_list[random_num]+"\n\n")
###################################################

#Function to take password input as *****
def get_password(prompt):
    password = ""
    print(prompt, end="", flush=True)
    if os.name == 'nt':
        import msvcrt
        while True:
            key = msvcrt.getch() 
            if key == b"\r" or key == b"\n":
                print()
                return password
            elif key == b"\b":
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            elif key == b"\x03":
                raise KeyboardInterrupt
            else:
                password += key.decode("utf-8")
                print("*", end="", flush=True)
    else:
        password = getpass('')
        return password

############################################################

def clear_terminal(): # to clear the terminal
    """Clears the terminal screen."""

    if os.name == "nt": #for Windows
        os.system("cls")
    else:
        os.system("clear") # for Linux and Mac os

##############################################################

# Function to register a new user
def register():
    clear_terminal()
    banner()

    console.print(f'\t\tRegister\n\n',style='bold magenta')

    while True:
        username = input(f"{Fore.BLUE}Enter a username: {Fore.GREEN}")
        password = get_password(f"{Fore.BLUE}Enter a password: {Fore.GREEN}")

        with open("users.txt","a") as f: #open the users.txt file as appendable
            f.write(f"{username}:{password}\n") #Write the credentials to user credentials

        print(f"\n\n\t\t{Fore.CYAN}Registered Successfully. You can Log in now.")#confirmation
        time.sleep(2)
        main_menu_not_logged_in()

###############################################################

#Funciton to add a new user for admin
def add_user():
    clear_terminal()
    banner()

    console.print(f'\t\tAdd User\n\n',style='bold magenta')

    while True:
        username = input(f"{Fore.BLUE}Enter a username: {Fore.GREEN}")
        password = get_password(f"{Fore.BLUE}Enter a password: {Fore.GREEN}")

        with open("users.txt","a") as f: #open the users.txt file as appendable
            f.write(f"{username}:{password}\n") #Write the credentials to user credentials

        print(f"\n\n\t\t{Fore.CYAN}User Added")#confirmation
        time.sleep(2)
        admin_panel()


###########################################################

# Function to log in as an existing user
def login():
    clear_terminal()
    banner()

    console.print(f"\t\tLogin\n\n",style='bold magenta')

    while True:
        username = input(f"{Fore.BLUE}Enter your Username: {Fore.GREEN}")
        password = get_password(f"{Fore.BLUE}Enter your Password: {Fore.GREEN}")
        if username == "tamim" and password =="verystrongpassword": #admin login
            print(f"\t\t{Fore.LIGHTRED_EX}Logged in as Admin")
            time.sleep(2)
            admin_panel()

        with open("users.txt") as f: #open the users.txt file
            for line in f:
                if line.strip() == f"{username}:{password}":
                    time.sleep(1)
                    print(f"\n\n\t\t{Fore.CYAN}Welcome  "+username+"\n") # Welcome on successful logon
                    time.sleep(2)
                    main_menu_logged_in() # redirect to main menu
            else:
                time.sleep(1)
                print(f"{Fore.RED}Invalid username or password.\n")
                time.sleep(1)
                while True:
                    x = input(f'{Fore.BLUE}Try again?  y/n:{Fore.GREEN} ')
                    if x.lower()=='y':
                        login()
                    elif x.lower() == 'n':
                        main_menu_not_logged_in()
                    else:
                        print(f'{Fore.RED}Invalid Choice')

##############################################################

# Function to add a new contact for admin
def add_contact_admin():
    clear_terminal()
    banner()

    console.print(f"\t\tAdd A Contact\n\n",style='bold magenta')

    # Get the contact information from the user
    name = input(f"{Fore.BLUE}\nName: {Fore.GREEN}")
    address = input(f"{Fore.BLUE}Address: {Fore.GREEN}")
    contact = input(f"{Fore.BLUE}Contact No: {Fore.GREEN}")
    email = input(f"{Fore.BLUE}E-mail: {Fore.GREEN}")
    phone = input(f"{Fore.BLUE}Phone: {Fore.GREEN}")
    id_no = input(f"{Fore.BLUE}ID number: {Fore.GREEN}")

    # Write the contact information to the CSV file
    with open("contacts.csv", "a", newline='') as file: #open the csv file as appendable
        writer = csv.writer(file)
        writer.writerow([name, address, contact, email, phone, id_no]) # write the data to csv

    print(f"\n\t\t{Fore.GREEN}Contact added successfully!\n") #confirmation
    time.sleep(2)

    while True:
        x = input(f"{Fore.BLUE}Add More: y/n\n{Fore.RED} -> {Fore.GREEN} ")
        if x.lower() == 'y':
            add_contact_admin()
        elif x.lower() == 'n':
            admin_panel()
        else:
            print(f'{Fore.RED}Invalid Choice.\n')


#########################################################################


# Function to add a new contact
def add_contact():
    clear_terminal()
    banner()
    
    console.print(f'\t\tAdd A Contact\n\n',style='bold magenta')

    # Get the contact information from the user
    name = input(f"{Fore.BLUE}\nName: {Fore.GREEN}")
    address = input(f"{Fore.BLUE}Address: {Fore.GREEN}")
    contact = input(f"{Fore.BLUE}Contact No: {Fore.GREEN}")
    email = input(f"{Fore.BLUE}E-mail: {Fore.GREEN}")
    phone = input(f"{Fore.BLUE}Phone: {Fore.GREEN}")
    id_no = input(f"{Fore.BLUE}ID number: {Fore.GREEN}")

    # Write the contact information to the CSV file
    with open("contacts.csv", "a", newline='') as file: #open the csv file as appendable
        writer = csv.writer(file)
        writer.writerow([name, address, contact, email, phone, id_no]) # write the data to csv

    print(f"\n\t\t{Fore.CYAN}Contact added successfully!\n") #confirmation
    time.sleep(2)

    while True:
        x = input(f"{Fore.BLUE}Add More: y/n\n{Fore.RED} -> {Fore.GREEN} ")
        if x.lower() == 'y':
            add_contact()
        elif x.lower() == 'n':
            main_menu_logged_in()
        else:
            print(f'{Fore.RED}Invalid Choice.\n')


########################################################################################


# Function to search a contact for admin
def search_contact_admin():
    def l_search_agian(): #search again for not logged in user
        while True:
            x = input(f"{Fore.BLUE}\nSearch Again: y/n\n{Fore.RED} -> {Fore.GREEN} ")
            if x.lower() == 'y':
                search_contact_admin()
            elif x.lower() == 'n':
                admin_panel()
            else:
                print(f"{Fore.RED}Invalid Choice.\n")

    clear_terminal()
    banner()

    console.print(f'\t\tSearch For Contacts\n\n',style='bold magenta')

    while True:
        # Get the search term from the user
        term = input(f"{Fore.BLUE}Enter name/e-mail/phone: {Fore.GREEN}")

        print(f"{Fore.GREEN}Searching.... Please Wait.....\n")
        
        time.sleep(2)

        # Search for the contact in the CSV file
        with open("contacts.csv") as file:

            reader = csv.reader(file)

            for row in reader:
                if term in [row[0], row[3], row[4]]:
                    print(f"{Fore.CYAN}Name: ", row[0])
                    print("Address: ", row[1])
                    print("Contact: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("ID Number: ", row[5])

                    l_search_agian() #asks the users if he wants to search again or not
            else:
                print(f"{Fore.RED}Contact not found.")
                l_search_agian()


#######################################################################################                


# Function to search for a contact by name, email, or phone
def search_contact_logged_in():
    def l_search_agian(): #search again for not logged in user
        while True:
            x = input(f"{Fore.BLUE}\nSearch Again: y/n\n{Fore.RED} -> {Fore.GREEN} ")
            if x.lower() == 'y':
                search_contact_logged_in()
            elif x.lower() == 'n':
                main_menu_logged_in()
            else:
                print(f"{Fore.RED}Invalid Choice.\n")

    clear_terminal()
    banner()

    console.print(f'\t\tSearch For Contacts\n\n',style='bold magenta')


    while True:
        # Get the search term from the user
        term = input(f"{Fore.BLUE}Enter name/e-mail/phone: {Fore.GREEN}")

        print(f"{Fore.GREEN}Searching.... Please Wait.....\n")
        
        time.sleep(2)

        # Search for the contact in the CSV file
        with open("contacts.csv") as file:

            reader = csv.reader(file)

            for row in reader:
                if term in [row[0], row[3], row[4]]:
                    print(f"{Fore.CYAN}Name: ", row[0])
                    print("Address: ", row[1])
                    print("Contact: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("ID Number: ", row[5])

                    l_search_agian() #asks the users if he wants to search again or not
            else:
                print(f"{Fore.RED}Contact not found.")
                time.sleep(1)
                l_search_agian()


##############################################################################

#Function to search contact while not logged in
def search_contact_not_logged_in():
    def n_l_search_agian(): #search again for not logged in user

        while True:
            x = input(f"{Fore.BLUE}\nSearch Again: y/n\n{Fore.RED} -> {Fore.GREEN} ")
            if x.lower() == 'y':
                search_contact_not_logged_in()
            elif x.lower() == 'n':
                main_menu_not_logged_in() # redirect to main menu
            else:
                print(f"{Fore.RED}Invalid Choice.\n")

    clear_terminal()
    banner()

    console.print(f'\t\tSearch For Contacts\n\n',style='bold magenta')

    while True:
        # Get the search term from the user
        term = input(f"{Fore.BLUE}Enter name/e-mail/phone: {Fore.GREEN}")

        print(f"{Fore.GREEN}Searching.... Please Wait.....\n")

        time.sleep(2)

        # Search for the contact in the CSV file
        with open("contacts.csv") as file:

            reader = csv.reader(file)

            for row in reader:
                if term in [row[0], row[3], row[4]]:
                    print(f"{Fore.CYAN}Name: ", row[0])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print(f"{Fore.RED}\n\n TO View Detailed Information, Please Log in.\n")
                    n_l_search_agian()
            else:
                print(f"{Fore.RED}Contact not found.")
                n_l_search_agian()


###################################################################

#Delte Contact 
def delete_contact_admin():
    clear_terminal()
    banner()

    console.print(f'\t\tDelete Contact\n\n',style='bold magenta')

    # Get the search term from the user
    term = input(f"{Fore.BLUE}Enter name/e-mail/phone: {Fore.GREEN}")

    print(f"{Fore.GREEN}Searching.... Please Wait.....\n")
    time.sleep(2)

    def delete_data(y): #  Nested Function to delete actual data from csv cause I was facing errors trying other techniques. That's why added so many fuking functions.
        
        # Open the CSV file
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            rows = []
            # Iterate over the rows in the file
            for row in reader:
                if y in row:
                    continue
                rows.append(row)

        with open('contacts.csv', 'w', newline='') as file:

            # Write the rows from the new list to the file
            writer = csv.writer(file)
            writer.writerows(rows)


    def search_to_delete(x): # confirmation of deletion 
        
        def delete_or_not():

            while True:
                b = input(f"\n{Fore.BLUE}1. Delete\n2. Cancel\n3. Select another\n{Fore.RED} ->{Fore.GREEN} ")
                if b == '1':
                    delete_data(x)
                    print(f"{Fore.CYAN}Contact Deleted.")
                    time.sleep(1)
                    admin_panel()
                    break
                elif b=='2':
                    admin_panel()
                elif b == '3':
                    delete_contact_admin() # redirect to main delete_contact func that asks to search again. Don't be confused by my code. 
                else:
                    print(f"{Fore.RED}Invalid Choice")



        # Search for the contact in the CSV file
        with open("contacts.csv") as file:

            reader = csv.reader(file)

            for row in reader:
                if x in [row[0], row[3], row[4]]:
                    print(f"{Fore.CYAN}Name: ", row[0])
                    print("Address: ", row[1])
                    print("Contact: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("ID Number: ", row[5])
                    delete_or_not()
                                                   
            else:
                print(f"{Fore.RED}Contact not found.")
                time.sleep(1)
                while True:
                    x = input(f"{Fore.BLUE}\nSearch Again: y/n\n{Fore.RED} -> {Fore.GREEN} ")
                    if z == 'y':
                        delete_contact_admin()
                    elif z == 'n':
                        admin_panel()
                    else:
                        print(f"{Fore.RED}Invalid Choice")
    
    search_to_delete(x= term) # calls the delete confirmation function


#########################################################################################

#Delte Contact 
def delete_contact():
    clear_terminal()
    banner()

    console.print(f'\t\tDelete Contact\n\n',style='bold magenta')

    # Get the search term from the user
    term = input(f"{Fore.BLUE}Enter name/e-mail/phone: {Fore.GREEN}")

    print(f"{Fore.GREEN}Searching.... Please Wait.....\n")
    time.sleep(2)

    def delete_data(y): #  Nested Function to delete actual data from csv cause I was facing errors trying other techniques. That's why added so many fuking functions.
        
        # Open the CSV file
        with open('contacts.csv', 'r') as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                if y in row:
                    continue
                rows.append(row)

        # Open the file again in write mode
        with open('contacts.csv', 'w', newline='') as file:
            # Write the rows from the new list to the file
            writer = csv.writer(file)
            writer.writerows(rows)


    def search_to_delete(x): # confirmation of deletion 
        
        def delete_or_not():

            while True:
                b = input(f"\n{Fore.BLUE}1. Delete\n2. Cancel\n3. Select another\n{Fore.RED} ->{Fore.GREEN} ")
                if b == '1':
                    delete_data(x)
                    print(f"{Fore.CYAN}Successfully Deleted")
                    time.sleep(1)
                    main_menu_logged_in()
                    break
                elif b == '2':
                    main_menu_logged_in()
                elif b=='2':
                    delete_contact() # redirect to main delete_contact func that asks to search again. Don't be confused by my code. 
                else:
                    print(f"{Fore.RED}Invalid Choice")



        # Search for the contact in the CSV file
        with open("contacts.csv") as file:
            reader = csv.reader(file)

            for row in reader:
                if x in [row[0], row[3], row[4]]:
                    print(f"{Fore.CYAN}Name: ", row[0])
                    print("Address: ", row[1])
                    print("Contact: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    print("ID Number: ", row[5])
                    delete_or_not()
                                                   
            else:
                print(f"\n{Fore.RED}Contact not found.")
                time.sleep(1)
                while True:
                    z = input(f"{Fore.BLUE}Search Again: y/n \n{Fore.RED} ->{Fore.GREEN} ")
                    if z == 'y':
                        delete_contact()
                    elif z == 'n':
                        main_menu_logged_in()
                    else:
                        print(f"{Fore.RED}Invalid Choice")

    
    search_to_delete(x= term) # calls the delete confirmation function


######################################################################################

#Function to delete user (only accesible for admin)
def delete_user():
    def delete_user_data(x):
        with open("users.txt","r") as file:
            lines = list()
            for line in file:
                if x== line.strip().split(":")[0]:
                    continue
                else:
                    lines.append(line)

        with open("users.txt","w") as f:
            for i in lines:
                f.write(f"{i}\n")
        print(f"{Fore.CYAN}Successfully deleted.")
        time.sleep(1)
        admin_panel()

    clear_terminal()
    banner()

    console.print(f"\t\tDelete User\n\n",style='bold magenta')

    username = input(f"{Fore.BLUE}Enter the username:{Fore.GREEN} ")#username of the user to delete

    with open("users.txt",'r')as file:
        for line in file:
            cred = line.strip().split(":")
            if username == cred[0]:
                print(f"{Fore.GREEN}Found: \nUsername: {cred[0]}, Password: {cred[1]}\n")
                while True:
                    x = input(f"{Fore.BLUE}1. Delete\n2. Cancel\n3. Search Again\n {Fore.RED}->{Fore.GREEN} ")
                    if x == '1':
                        delete_user_data(x=username)
                    elif x == '2':
                        admin_panel()
                    elif x == '2':
                        delete_user()
                    else:
                        print(f'{Fore.RED}Invalid Choice.\n')
        else:
            print(f"{Fore.RED}No Users found with that Username.\n")
            while True:
                x = input(f"{Fore.BLUE}Search Again: y/n\n {Fore.RED}->{Fore.GREEN} ")
                if x.lower() == 'y':
                    delete_user()
                elif x.lower()=='n':
                    admin_panel()
                else:
                    print(f"{Fore.RED}Invalid Choice.\n")


##################################################################################

# main menu while not logged in 
def main_menu_not_logged_in():
    clear_terminal()
    banner()

    console.print(f"\t\tHome\n\n",style='bold magenta')

    while True:
        x = input(f"{Fore.BLUE}1. Login\n2. Register\n3. Search Contact\n0. Exit\n{Fore.RED} -> {Fore.GREEN}")
        if x == '1':
            login()
        elif x=='2':
            register()
        elif x == '3':
            search_contact_not_logged_in()
        elif x == '0':
            sys.exit()
        else:
            print(f'\n{Fore.RED}Invalid Choice.\n')
            time.sleep(1)
            main_menu_not_logged_in()



##########################################################################


#main menu while logged in
def main_menu_logged_in():
    clear_terminal()
    banner()

    console.print(f'\t\tDashboard\n\n',style='bold magenta')

    while True:
        x = input(f"{Fore.BLUE}1. Add Contact\n2. Edit Contact\n3. Search Contact\n4. Delete Contact\n5. Logout\n0. Exit\n{Fore.RED} ->{Fore.GREEN} ")
        if x == '1':
            add_contact()
        elif x=='2':
            print(f"{Fore.YELLOW}Under Development")
            time.sleep(2)
            main_menu_logged_in()
        elif x=='3':
            search_contact_logged_in()
        elif x=='4':
            delete_contact()
        elif x=='5':
            main_menu_not_logged_in()
        elif x=='0':
            sys.exit()
        else:
            print(f'\n{Fore.RED}Invalid Choice')
            time.sleep(1)
            main_menu_logged_in()

####################################################################################

#Admin panel
def admin_panel():
    clear_terminal()
    banner()

    console.print(f'\t\tAdmin Panel\n\n',style='bold magenta')

    while True:
        x = input(f"{Fore.BLUE}1. User Management\n2. Contact Management\n3. Log Out\n0. Exit\n{Fore.RED} ->{Fore.GREEN} ")
        if x == '1':
            clear_terminal()
            banner()
            print(f"\t\t{Fore.CYAN}User Management Dashbord\n\n")
            while True:
                y = input(f"{Fore.BLUE}1. Add user\n2. Delete User\n3. Edit User Config\n0. Main Menu\n{Fore.RED} ->{Fore.GREEN} ")
                if y == '1':
                    add_user()
                elif y == '2':
                    delete_user()
                elif y == '3':
                    print(f"\n\n{Fore.YELLOW}Under Development\n\n")
                elif y == '0':
                    admin_panel()
                else:
                    print(f"{Fore.RED}Invalid Choice")
                    time.sleep(1)
        elif x == '2':
            clear_terminal()
            banner()
            print(f"\t\t{Fore.CYAN}Contact Management Dashbord\n\n")
            while True:
                y = input(f"{Fore.BLUE}1. Add Contact\n2. Delete Contact\n3. Search Contact\n4. Edit Contact\n0. Main Menu \n {Fore.RED}>{Fore.GREEN} ")
                if y == '1':
                    add_contact_admin()
                elif y == '2':
                    delete_contact_admin()
                elif y == '3':
                    search_contact_admin()
                elif y == '4':
                    print(f"\n\n{Fore.YELLOW}Under Development\n\n")
                elif y == '0':
                    admin_panel()
                else:
                    print(f"{Fore.RED}Invalid Choice")
                    time.sleep(1)
        
        elif x == '3':
            main_menu_not_logged_in()
        elif x=='0':
            sys.exit()
        else:
            print(f'\n{Fore.RED}Invalid Choice')
            time.sleep(1)
            admin_panel()
    

if os.name=='nt':
    t = [i for i in os.walk('.')]
    if 'test.csv' not in t:
        os.system("type nul > conatcts.csv")
        with open("contacts.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Address', 'Contact', 'E-mail', 'Phone', 'Id_No'])

    if 'test.txt' not in t:
        os.system("type nul > users.txt")

else:
    t = [i for i in os.walk('.')]
    if 'test.csv' not in t:
        os.system("touch  contacts.csv")
        with open("contacts.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Address', 'Contact', 'E-mail', 'Phone', 'Id_No'])

    if 'test.txt' not in t:
        os.system("touch users.txt")


main_menu_not_logged_in() # Start the program. Not logged in as usual. Program starts here
