# Inventory program with barcode scanner
# Author: Alicia Chin
"""Inventory of all food items in the kitchen. User will be able to add a new item,
update an existing item or delete an item.

Database will have the following columns:
barcode, item, category, quantity, unit, expiry_date, date_added, last_updated


FUNTIONALITY
User will be prompted to select an option in the display menu; add, update (increase, decrease, correct), delete

ERROR CHECKS
Check for duplicate entries"""


# Imports of libraries
import sqlite3


def display_menu():
    # Prompts the user to select an option; add, update (increase, decrease, correct), delete
    # Loops if input is invalid (not 1 to 4 inclusive, varchar)
    valid = False
    while not valid:
        try:
            option = input("Select an option:\n"
                           "1 - Add to inventory\n"
                           "2 - Record usage of an item\n"
                           "3 - Change details of an existing item\n"
                           "4 - Delete from inventory\n"
                           "5 - Show all\n")
            int_option = int(option)

            if not 1 <= int_option <= 5:
                print("Please select a valid option: 1, 2, 3, 4\n")

            if int_option == 1:
                # valid = True
                # print("Selected option: " + str(option))
                #
                # if barcode_numeric() == True:
                #     new_item(barcode)
                valid = True
                print( "Selected option: " + str( option ) )
                new_item()

            if int_option == 2:
                valid = True
                print("Selected option: " + str(option))
                decrease_item()

            if int_option == 3:
                valid = True
                print("Selected option: " + str(option))
                edit_details()

            if int_option == 4:
                valid = True
                print("Selected option: " + str(option))
                delete_item()

            if int_option == 5:
                valid = True
                print("Selected option: " + str(option))
                show_all()

        except ValueError:
            print("Please select a valid option: 1, 2, 3, 4\n")



# STANDALONE FUNCTIONS

# Display database
def show_all():
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM sample;''')
    items = c.fetchall()

    for item in items:
        print(item)
        print(type(item))

    conn.commit()
    conn.close()

def show_one(barcode):
    conn = sqlite3.connect( 'barcode.db' )
    c = conn.cursor()
    c.execute( '''SELECT * FROM sample WHERE id = (?);''', (barcode,) )
    result = c.fetchone()
    conn.commit()
    conn.close()

    print(result)


# Check barcode is numeric
def barcode_numeric():
    valid = False
    while not valid:
        barcode = input("Please scan/enter the item's barcode.\n")

        if barcode.isnumeric():
            # Check that barcode is a number.
            valid = True
            return valid, barcode


# Function to add entry to database
def add_one(barcode, item, category, quantity, unit, expiry_date):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''INSERT INTO sample VALUES (?,?,?,?,?,?,datetime('now','localtime'),datetime('now','localtime'));''',
              (barcode, item, category, quantity, unit, expiry_date))

    conn.commit()
    conn.close()

def subtract_quantity(barcode,quantity_used):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''UPDATE sample SET quantity = quantity - (?), last_updated = datetime('now','localtime')
                    WHERE id = (?);''',
              (quantity_used, barcode))

    conn.commit()
    conn.close()



# MAIN FUNCTIONS

def new_item():
    valid = False
    while not valid:
        barcode = input( "Please scan/enter the item's barcode.\n" )

        if barcode.isnumeric():
            # Check that barcode is a number.
            valid = True

            # Check if barcode exists in the database.
            conn = sqlite3.connect('barcode.db')
            c = conn.cursor()
            c.execute('''SELECT id FROM sample WHERE id = (?);''', (barcode,))
            result = c.fetchone()
            conn.commit()
            conn.close()

            # If barcode does not exist, get details to create new entry.
            if result is None:
                print('Enter the following details.\n')
                item = input("Item name: ")
                category = input("Category: ")
                unit = input("Unit (g or ml only): ")
                quantity = input("Quantity: ")
                expiry_date = input("Date of expiry (YYYY-MM-DD): ")

                add_one(barcode, item, category, quantity, unit, expiry_date)

                print("New entry added!\n")
                show_one(barcode)

            # If barcode exists, get quantity (and expiry date) to update details.
            # TODO: Determine how to store same items with different expiry dates.
            else:
                # TODO: Retrieve entry to review details and capture unit
                # print("Enter the following details.\n")
                # quantity = input("Quantity (in " + str(unit) "): ")
                # expiry_date = input("Date of expiry: ")

                # def update(quantity,expiry_date):
                #     conn = sqlite3.connect('barcode.db')
                #     c = conn.cursor()
                #
                #     c.execute('''
                #     UPDATE...''')
                #
                #     c.execute('''
                #     SELECT * FROM sample''')
                # update(quantity,expiry_date)
                pass


# UPDATE - Record usage of an item
def decrease_item():
    valid = False
    while not valid:
        barcode = input("Please scan/enter the item's barcode.\n")

        if barcode.isnumeric():
            # Check that barcode is a number.
            valid = True

            # Check if barcode exists in the database.
            conn = sqlite3.connect('barcode.db')
            c = conn.cursor()
            c.execute('''SELECT id FROM sample WHERE id = (?);''', (barcode,))
            result = c.fetchone()
            conn.commit()
            conn.close()

            if result is None:
                print("Exit and select option 1.")

            # Get quantity used
            else:
                print("Selected item:\n" + str(result))
                quantity_used = input("Quantity used: ")

                subtract_quantity(barcode,quantity_used)

                print( "Entry updated!\n" )
                show_one(barcode)


# EDIT - Change details of an existing item
def edit_details():
    # Get barcode id
    # Fetch entry
    # Select option - which variable to change
    pass


# DELETE - Delete from inventory
def delete_item():
    # Get barcode id
    # Fetch entry
    # Request confirmation to delete entry
    # Delete entry
    pass


display_menu()
