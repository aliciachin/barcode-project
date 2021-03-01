# Inventory program with barcode scanner
"""Inventory of all food items in the kitchen. User will be able to add a new item,
update an existing item or delete an item.

Database will have the following columns:
barcode, item, category, quantity, unit, expiry_date, date_added, last_updated


FUNTIONALITY
User will be prompted to select an option in the display menu; add, update (increase, decrease, correct), delete

ERROR CHECKS
Check for duplicate entries"""

# Display menu
'''Prompts the user to select an option; add, update (increase, decrease, correct), delete'''




def display_menu():

    option = input("Select an option:\n"
              "1 - Add to inventory\n"
              "2 - Record usage of an item\n"
              "3 - Change details of an existing item\n"
              "4 - Delete from inventory\n")
    try:
        int_option = int(option)
        if not 1<=int_option<=4:
            print("Please select a valid option. (1, 2, 3, 4)")
        if int_option == 1:
            print("Selected option: " + str(option))
            new_item()
        if int_option == 2:
            print("Selected option: " + str(option))
            decrease_item()
        if int_option == 3:
            print("Selected option: " + str(option))
            edit_details()
        if int_option == 4:
            print("Selected option: " + str(option))
            delete_item()
    except ValueError:
        print("You entered a string. Please select a valid option. (1, 2, 3, 4)")





'''def display_menu(option):
    not_valid = True
    while not_valid:
        print('1,2,3,4')
        option = int(input('12,,3,4)'))
        if valid_option():
            not_valid = False
        else:
            print('only select between 1 to 4 incl')
    if option == 1:
        do 1'''


# ADD - Add to inventory
# 1. Scan barcode
# 2. If new, information required:
#       - item (string)
#       - category (multi-select)
#       - quantity
#       - unit (multi-select)
#       - expiry_date (YYYY-MM-DD format)
#       Add to database
# 3. If existing, information required:
#       -
#

def new_item():
    barcode = input("Please scan the item's barcode. ")

    # check that barcode is valid - must be a number.
    while not barcode.isnumeric():
        print("Barcode must be numeric.")
        barcode = input("Please scan the item's barcode. ")

    else :
        pass


'''If barcode exists in the database, user can update or delete.'''


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






