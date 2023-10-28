
import classes_functions
is_program_running = True
admin_menu = False
guest_menu = False

while is_program_running:
    admin_menu = True
    guest_menu = True
    # Display an introduction
    classes_functions.intro()
    print("\nHOTEL MANAGEMENT APPLICATION")
    print("---------------------------------")
    print("ADMIN LOGIN - Press 'a'")
    print("GUEST LOGIN - Press 'g'")
    print("EXIT PROGRAM - Press 'e'")
    print()
    option = input("Enter your choice: ")
    guest1 = classes_functions.Guest()
    admin1 = classes_functions.Admin()

    if option == 'a':
        if __name__ == "__main__":
            filename = 'data/Admin_data.csv'
            admin_verifier = classes_functions.Admin()
            search1 = classes_functions.Admin()
            admin_name = input("Enter admin name: ")
            password = input("Enter admin password: ")

            if admin_verifier.admin_login(admin_name, password):
                print()
                while admin_menu:
                    print("\nPlease enter an option")
                    print("---------------------------------")
                    print("1. Show all rooms")
                    print("2. Search for a particular room")
                    print("3. Search for available rooms")
                    print("4. Add room")
                    print("5. Remove a room")
                    print("6. Show all guests")
                    print("7. Search for Guest")
                    print("8. Add Guest")
                    print("9. Remove Guest")
                    print("b. Back to main menu")
                    print("e. Exit")

                    choice = input("> ")

                    if choice == '1':
                        classes_functions.loading_bar_animation()
                        admin1.show_all_rooms()
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True
                        else:
                            #correct infinite loop
                            print("Invalid Option, try again")

                    elif choice == '2':
                        room_id = input("Enter room ID: ")
                        search1.search_for_room(room_id)
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '3':
                        admin1.search_available_rooms()
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '4':
                        admin1.add_room()
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '5':
                        room_id = input("Enter Room ID to remove: ")
                        admin1.remove_room(room_id)
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '6':
                        admin1.show_all_guests()
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '7':
                        guest_name = input("Enter guest name: ")
                        admin1.search_for_guest(guest_name)
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '8':
                        admin1.add_guest()
                        print()
                        print("Enter Room details")
                        admin1.add_room()
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == '9':
                        guest_name = input("Please input guest name: ")
                        admin1.remove_guest(guest_name)
                        choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
                        if choice == 'n':
                            admin_menu = False
                        elif choice == 'y':
                            admin_menu = True

                    elif choice == 'b':
                        admin_menu = False
                        is_program_running = True

                    elif choice == 'e':
                        admin_menu = False
                        is_program_running = False

                    else:
                        print("\nYou entered an invalid option, please try again.")
                        admin_menu = True

    elif option == 'g':
            choice = None
            if admin1.search_for_guest(guest_name, ID):
                print()
                while guest_menu:
                    print("\nPlease enter an option")
                    print("----------------------------------")
                    print("1. Search for available rooms")
                    print("2. Check for personal details")
                    print("3. Leave room")
                    print("4. Back to Main Menu\n")
                    print("5. Exit\n")
                    name, f_name, l_name, ID = "", "", "", ""
                    login_success = False
                    choice = input("> ")

                    if choice == '1':
                        print("These are the rooms available:")
                        print("---------------------------------------")
                        admin1.search_available_rooms()
                        choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")
                        if choice == 'n':
                            is_program_running = True
                        elif choice == 'y':
                            guest_menu = True

                    elif choice == '2':
                        guest_name = input("Enter your full name: ")
                        ID = input("Enter your ID: ")
                        login_success = guest1.guest_login(guest_name,ID)
                        if login_success:
                            admin1.search_for_guest(guest_name, ID)
                            choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")
                            if choice == 'n':
                                is_program_running = True
                            elif choice == 'y':
                                guest_menu = True
                        else:
                            guest_menu = True

                    elif choice == '3':
                        f_name = input("Enter your first name: ")
                        l_name = input("Enter your last name: ")
                        name = l_name + " " + f_name
                        ID = input("Enter your ID: ")
                        login_success = guest1.guest_login(name, ID)
                        if login_success:
                            admin1.remove_guest(name, ID)
                            choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")
                            if choice == 'n':
                                is_program_running = True
                            elif choice == 'y':
                                guest_menu = True
                        else:
                            guest_menu = True

                    elif choice == '4':
                        is_program_running = True

                    elif choice == '5':
                        guest_menu = False

                    elif choice == 'y':
                        guest_menu = True

                    elif choice == 'n':
                        is_program_running = True

                    else:
                        print("\nYou entered an invalid option, please try again.\n")
                        guest_menu = True
    elif option == 'e':
        is_program_running = False

classes_functions.outro()

# if __name__ == '__main__':
#     print('PyCharm')
