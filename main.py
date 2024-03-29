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

            if int_option == 5:
                valid = True
                print("Selected option: " + str(option))
                sql_show_all()

        except ValueError:
            print("Please select a valid option: 1, 2, 3, 4\n")


# STANDALONE FUNCTIONS


# Checks barcode id is numeric
def barcode_numeric(barcode):
    valid = False

    if barcode.isnumeric():
        # Check that barcode is a number.
        valid = True

    return valid


# Checks if an entry exists
def sql_entry_exists(barcode):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()
    c.execute('''SELECT id FROM sample WHERE id = ?;''', (barcode,))
    result = c.fetchone()
    conn.commit()
    conn.close()

    return result


# Displays the whole database
def sql_show_all():
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM sample;''')
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()


# Displays a selected entry
def sql_show_one(barcode):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM sample WHERE id = ?;''', (barcode,))
    result = c.fetchone()
    conn.commit()
    conn.close()

    print(result)


# Adds a single entry to database
def sql_add_one(barcode, item, category, quantity, unit, expiry_date):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''INSERT INTO sample VALUES (?,?,?,?,?,?,datetime('now','localtime'),datetime('now','localtime'));''',
              (barcode, item, category, quantity, unit, expiry_date))

    conn.commit()
    conn.close()


# Adds to value in quantity column for a single entry
def sql_add_quantity(barcode, quantity_add):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''UPDATE sample SET quantity = quantity + ?, last_updated = datetime('now','localtime')
                    WHERE id = ?;''',
              (quantity_add, barcode))

    conn.commit()
    conn.close()


def new_expiry_date(expiry_date,barcode):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''UPDATE sample SET expiry_date = ?, last_updated = datetime('now','localtime')
                    WHERE id = ?;''',
              (expiry_date, barcode))

    conn.commit()
    conn.close()


# Subtracts from value in quantity column for a single entry
def sql_subtract_quantity(barcode, quantity_used):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''UPDATE sample SET quantity = quantity - ?, last_updated = datetime('now','localtime')
                    WHERE id = ?;''',
              (quantity_used, barcode))

    conn.commit()
    conn.close()




# Replaces value of a specific column for a single entry
def sql_update_variable(barcode, new_info, variable):
    # Query: match variable name with column name, replace value with new info
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    # Get column name
    sql_command = '''UPDATE sample SET {} = (?), last_updated = datetime('now','localtime')
                            WHERE id = (?);'''.format(variable)

    c.execute(sql_command,
              (new_info, barcode))

    conn.commit()
    conn.close()


# Deletes a single entry
def sql_delete_one(barcode):
    conn = sqlite3.connect('barcode.db')
    c = conn.cursor()

    c.execute('''DELETE FROM sample WHERE id = ?;''', (barcode,))

    conn.commit()
    conn.close()


# MAIN FUNCTIONS


def new_item():
    valid = False
    while not valid:
        # Get barcode id
        barcode = input("Please scan/enter the item's barcode.\n")

        # Check if barcode is a number
        valid = barcode_numeric(barcode)

    # Check if barcode exists in the database.
    result = sql_entry_exists(barcode)

    # If barcode does not exist, get details to create new entry.
    if result is None:
        print('Enter the following details.\n')
        item = input("Item name: ")
        category = input("Category: ")
        unit = input("Unit (g or ml only): ")
        quantity = input("Quantity: ")
        expiry_date = input("Date of expiry (YYYY-MM-DD): ")

        sql_add_one(barcode, item, category, quantity, unit, expiry_date)

        print("\nNew entry added!\n")
        sql_show_one(barcode)

    # If barcode exists, get quantity and/or expiry date (if necessary) to update details.
    else:
        # Display current entry
        print("\nSelected item:")
        sql_show_one(barcode)

        # Get quantity to be added
        quantity_add = input("\nQuantity to be added: ")
        sql_add_quantity(barcode, quantity_add)

        # Check if expiry date needs to be updated - set the closest expiry date as value
        expiry_date = input("Please input the closest expiry date for this item in YYYY-MM-DD format.\n"
                            "If this does not need to be updated, press 'q' to exit.")
        if not expiry_date == 'q' or expiry_date =='Q':
            new_expiry_date(expiry_date,barcode)



# UPDATE - Record usage of an item
def decrease_item():
    valid = False
    while not valid:
        # Get barcode id
        barcode = input("Please scan/enter the item's barcode.\n")

        # Check if barcode is a number
        valid = barcode_numeric(barcode)

    # Check if barcode exists in the database.
    result = sql_entry_exists(barcode)

    if result is None:
        print("No id match. Select option 1 to add a new item.")

    # Get quantity used
    else:
        print("\nSelected item:")
        sql_show_one(barcode)
        quantity_used = input("\nQuantity used: ")

        sql_subtract_quantity(barcode, quantity_used)

        print("\nEntry updated!\n")
        sql_show_one(barcode)


# EDIT - Change details of an existing item
def edit_details():
    valid = False
    while not valid:
        # Get barcode id
        barcode = input("Please scan/enter the item's barcode.\n")

        # Check if barcode is a number
        valid = barcode_numeric(barcode)

    # Check if barcode exists in the database.
    result = sql_entry_exists(barcode)

    if result is None:
        print("No id match. Select option 1 to add a new item.")

    # Select which variable to change
    else:
        valid = False
        while not valid:
            try:
                print("\nSelected item:")
                sql_show_one(barcode)
                option = input("\nWhat would you like to edit?\n"
                               "1 - Id\n"
                               "2 - Item name \n"
                               "3 - Category\n"
                               "4 - Quantity\n"
                               "5 - Unit\n"
                               "6 - Expiry Date\n")
                int_option = int(option)

                if not 1 <= int_option <= 6:
                    print("Please select a valid option: 1, 2, 3, 4, 5, 6\n")

                if int_option == 1:
                    valid = True
                    variable = "id"
                    new_info = input("New id: ")

                    # Update entry with new info
                    sql_update_variable(barcode, new_info, variable)

                    # Display updated entry
                    print("\nEntry updated!\n")
                    sql_show_one(barcode)

                if int_option == 2:
                    valid = True
                    variable = "item"
                    new_info = input("New item name: ")

                    # Update entry with new info
                    sql_update_variable(barcode, new_info, variable)

                    # Display updated entry
                    print("\nEntry updated!\n")
                    sql_show_one(barcode)

                if int_option == 3:
                    valid = True
                    variable = "category"
                    new_info = input("New category: ")

                    # Update entry with new info
                    sql_update_variable(barcode, new_info, variable)

                    # Display updated entry
                    print("\nEntry updated!\n")
                    sql_show_one(barcode)

                if int_option == 4:
                    valid = True
                    variable = "quantity"
                    new_info = input("New quantity: ")

                    # Update entry with new info
                    sql_update_variable(barcode, new_info, variable)

                    # Display updated entry
                    print("\nEntry updated!\n")
                    sql_show_one(barcode)

                if int_option == 5:
                    valid = True
                    variable = "unit"
                    new_info = input("New unit: ")

                    # Update entry with new info
                    sql_update_variable(barcode, new_info, variable)

                    # Display updated entry
                    print("\nEntry updated!\n")
                    sql_show_one(barcode)

                if int_option == 6:
                    valid = True
                    variable = "expiry_date"
                    new_info = input("New expiry date (YYYY-MM-DD): ")

                    # Update entry with new info
                    sql_update_variable(barcode, new_info, variable)

                    # Display updated entry
                    print("\nEntry updated!\n")
                    sql_show_one(barcode)

            except ValueError:
                print("Please select a valid option: 1, 2, 3, 4, 5, 6\n")


# DELETE - Delete from inventory
def delete_item():
    valid = False
    while not valid:
        # Get barcode id
        barcode = input("Please scan/enter the item's barcode.\n")

        # Check if barcode is a number
        valid = barcode_numeric(barcode)

    # Check if barcode exists in the database.
    result = sql_entry_exists(barcode)

    if result is None:
        print("Item does not exist in database.")
    else:
        print("\nSelected item:")
        sql_show_one(barcode)
        confirm = input("Are you sure you want to delete this entry?\n"
                        "Press 'y' to confirm. Press any other key to exit.")

        if confirm == "y" or confirm == "Y":
            sql_delete_one(barcode)


display_menu()
