# Inventory program with barcode scanner
"""Inventory of all food items in the kitchen. User will be able to add a new item,
update an existing item or delete an item.

Database will have the following columns:
barcode, item, category, quantity, unit, expiry_date, date_added, last_updated


FUNTIONALITY
User will be prompted to select an option in the display menu; add, update (increase, decrease, correct), delete

ERROR CHECKS
Check for duplicate entries"""

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
                           "4 - Delete from inventory\n")
            int_option = int(option)

            if not 1 <= int_option <= 4:
                print("Please select a valid option: 1, 2, 3, 4\n")

            if int_option == 1:
                valid = True
                print("Selected option: " + str(option))
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

        except ValueError:
            print("Please select a valid option: 1, 2, 3, 4\n")

# Function to add entry to database
def add_one(barcode,item,category,quantity,unit,expiry_date):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''
    INSERT INTO sample VALUES
        (?,?,?,?,?,?,datetime('now','localtime'),datetime('now','localtime'));''',(barcode,item,category,quantity,unit,expiry_date))
    conn.commit()
    conn.close()

def show_all():
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM sample;''')
    conn.commit()
    conn.close()

def new_item():
    # ADD - Add to inventory
    # Scan barcode
    # If new, request for all information and append to the database.
    # If existing, request for relevant information and update the entry.
    valid = False
    while not valid:
        barcode = input("Please scan/enter the item's barcode.\n")

        if barcode.isnumeric():
            # Check that barcode is a number.
            valid = True


            # Check if barcode exists in the database.
            conn = sqlite3.connect('barcode.db')
            c = conn.cursor()
            c.execute('''SELECT id FROM sample WHERE id = (?)''',(barcode,))
            result = c.fetchone()
            conn.commit()
            conn.close()


            # If barcode does not exist, get details to create new entry.
            if result is None:
                print("Enter the following details.\n")
                item = input("Item name: ")
                category = input("Category: ")
                unit = input("Unit (g or ml only): ")
                quantity = input("Quantity: ")
                expiry_date = input("Date of expiry (YYYY-MM-DD): ")

                add_one(barcode,item,category,quantity,unit,expiry_date)

                # TODO: show_all() doesn't work
                show_all()


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




            # If barcode is not in database,
            # Get input:
            #   - item (string)
            #   - category (multi-select)
            #   - quantity (numeric)
            #   - unit (multi-select)
            #   - expiry_date (YYYY-MM-DD format)
            # Add to database

            # TODO: In SQL, write code for existing entry - update record in database
            # If barcode exists in database,
            # Get input:
            #   - quantity (display current unit for user)
            #   - expiry_date (YYYY-MM-DD format)
            # Update database
            # TODO: Determine logic for identical items but different expiry dates


# UPDATE - Record usage of an item
def decrease_item():
    pass


# EDIT - Change details of an existing item
def edit_details():
    pass


# DELETE - Delete from inventory
def delete_item():
    pass

display_menu()






