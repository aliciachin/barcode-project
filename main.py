# Inventory program with barcode scanner
"""Inventory of all food items in the kitchen. User will be able to add a new item,
update an existing item or delete an item.

Database will have the following columns:
barcode, item, category, quantity, unit, expiry_date, date_added, last_updated


FUNTIONALITY
User will be prompted to select an option in the display menu; add, update (increase, decrease, correct), delete

ERROR CHECKS
Check for duplicate entries"""


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


def new_item():
    # TODO: Create test database in SQL to check input against
    # ADD - Add to inventory
    # Scan barcode
    # If new, request for all information and append to the database.
    # If existing, request for relevant information and update the entry.
    valid = False
    while not valid:
        barcode = input("Please scan/enter the item's barcode.\n")

        if barcode.isnumeric():
            # check that barcode is a number.
            valid = True
            pass

            # TODO: Write code for new entry - append to database
            # If barcode is not in database,
            # Get input:
            #   - item (string)
            #   - category (multi-select)
            #   - quantity (numeric)
            #   - unit (multi-select)
            #   - expiry_date (YYYY-MM-DD format)
            # Add to database

            # TODO: Write code for existing entry - update record in database
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






