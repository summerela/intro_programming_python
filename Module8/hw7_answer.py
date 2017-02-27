from sortedcontainers import SortedDict

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a User')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    menu_choice = int(input("Type in a number (1-5): "))
    
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("Username: ")
        usernames[name] = username
        
    # remove an entry
    elif menu_choice == 3:
        # what do i do here? 
        print("Remove User")
        # get the name of the user they want to delete
        input_name = input("Name: ")
        # check if input name in dictionary
        if input_name in usernames:
            del usernames[input_name]

    # view user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name or username: ")
        if name in usernames:
            print(usernames[name])
        else:
            print("User not found.")

    #  # view user name      
    # elif menu_choice == 4:
    #     print("Lookup User")
    #     name = input("Name or username: ")
    #     for key, value in usernames.items():
    #         if (name == key):
    #             print(usernames[name])
    #         if (name == value):
    #             print([item[0] for item in usernames.items() if item[1] == name])
    #         else:
    #             print("User not found.")
    
    # is user enters something strange, show them the menu
    else:
        print_menu()