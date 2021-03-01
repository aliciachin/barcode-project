def display_menu():
    option = input("Select an integer between 1 and 4 inclusive.\n")
    try:
        int_option = int(option)
        if not 1 <= int_option <= 4:
            print("1 to 4. There are only four options. How did you go wrong there?")
        if int_option == 1:
            print("Yay")
        if int_option == 2:
            print("Yay")
        if int_option == 3:
            print("Yay")
        if int_option == 4:
            print("Yay")
    except ValueError:
        print("I said an integer. You entered a string, bitch.")


display_menu()


