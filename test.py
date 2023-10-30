import csv
# #
# # class HotelManager:
# #     def __init__(self, csv_file):
# #         self.csv_file = csv_file
# #
# #     def search_available_rooms(self):
# #         try:
# #             with open(self.csv_file, 'r') as file:
# #                 csv_reader = csv.reader(file)
# #                 next(csv_reader)  # Skip header row if exists
# #                 available_rooms = []
# #                 for row in csv_reader:
# #                     room_id, room_type, occupancy, price, availability = row
# #                     if availability.lower() == 'available':
# #                         available_rooms.append({
# #                             'Room ID': room_id,
# #                             'Room Type': room_type,
# #                             'Occupancy': occupancy,
# #                             'Price': price,
# #                             'Availability': availability
# #                         })
# #
# #                 if available_rooms:
# #                     print("\nAvailable Rooms:")
# #                     for room in available_rooms:
# #                         print(room)
# #                 else:
# #                     print("\nNo available rooms.")
# #         except FileNotFoundError:
# #             print("Error: Room CSV file not found.")
# #         except Exception as e:
# #             print(f"An error occurred: {e}")
# #
# # # Example usage
# # if __name__ == "__main__":
# #     csv_file = 'data/Room_data.csv'  # Replace 'rooms.csv' with your actual CSV file name
# #     hotel_manager = HotelManager(csv_file)
# #     hotel_manager.search_available_rooms()
#
#
# import csv
#
# class HotelManager:
#     def __init__(self, csv_file):
#         self.csv_file = csv_file
#
#     def search_available_rooms(self):
#         try:
#             with open(self.csv_file, 'r') as file:
#                 csv_reader = csv.reader(file)
#                 next(csv_reader)  # Skip header row if exists
#                 print("\nAvailable Rooms:")
#                 for row in csv_reader:
#                     room_id, room_type, occupancy, price, availability = row
#                     if availability.lower() == 'available':
#                         print(f"{room_id}, {room_type}, {occupancy}, {price}, {availability}")
#                 print()  # Add a newline for better formatting
#         except FileNotFoundError:
#             print("Error: Room CSV file not found.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#
# # Example usage
# # if __name__ == "__main__":
# csv_file = 'data/Room_data.csv'  # Replace 'rooms.csv' with your actual CSV file name
# hotel_manager = HotelManager(csv_file)
# hotel_manager.search_available_rooms()
#

#
# if __name__ == "__main__":
#             filename = 'data/Admin_data.csv'
#             admin_verifier = classes_functions.Admin()
#             search1 = classes_functions.Admin()
#             admin_name = input("Enter admin name: ")
#             password = input("Enter admin password: ")
#
#             if admin_verifier.admin_login(admin_name, password):
#                 print()
#                 while admin_menu:
#                     print("\nPlease enter an option")
#                     print("---------------------------------")
#                     print("1. Show all rooms")
#                     print("2. Search for a particular room")
#                     print("3. Search for available rooms")
#                     print("4. Add room")
#                     print("5. Remove a room")
#                     print("6. Show all guests")
#                     print("7. Search for Guest")
#                     print("8. Add Guest")
#                     print("9. Remove Guest")
#                     print("b. Back to main menu")
#                     print("e. Exit")
#
#                     choice = input("> ")
#
#                     if choice == '1':
#                         classes_functions.loading_bar_animation()
#                         admin1.show_all_rooms()
#                         choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
#                         if choice == 'n':
#                             admin_menu = False
#                         elif choice == 'y':
#                             admin_menu = True
#                         else:
#                             #correct infinite loop
#                             print("Invalid Option, try again")
# option = input()
elif option == 'g':
    print("\nPlease enter an option")
    print("----------------------------------")
    print("1. Search for available rooms")
    print("2. Check for personal details")
    print("3. Leave room")
    print("4. Back to Main Menu\n")
    print("e. Exit\n")

    choice = input("> ")

    if choice == '1':

        print("These are the rooms available:")

        print("---------------------------------------")

        admin1.search_available_rooms()

        choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

        if choice == 'n':

            guest_menu = False

        elif choice == 'y':

            guest_menu = True

        else:

            print("Invalid option, try again")

    elif choice == '2':
        if __name__ == "__main__":

            filename1 = 'data/Guest_data.csv'

            search2 = classes_functions.Admin()

            # choice = None

            guest_verifier = classes_functions.Guest()

            guest_name = input("Enter guest name: ")

            ID = input("Enter guest ID: ")

            print()

            if guest_verifier.guest_login(guest_name, ID):

                print()

                while guest_menu:
                    login_success = False
                    guest_name = input("Enter your full name: ")

                    ID = input("Enter your ID: ")

                    login_success = guest1.guest_login(guest_name, ID)

                    if login_success:

                        admin1.search_for_guest(guest_name, ID)

                        choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

                        if choice == 'n':

                            guest_menu = False

                        elif choice == 'y':

                            guest_menu = True

                    else:

                        guest_menu = True
    elif choice == '3':
        if __name__ == "__main__":

            filename1 = 'data/Guest_data.csv'

            search2 = classes_functions.Admin()

            # choice = None

            guest_verifier = classes_functions.Guest()

            guest_name = input("Enter guest name: ")

            ID = input("Enter guest ID: ")

            print()

            if guest_verifier.guest_login(guest_name, ID):

                print()

                while guest_menu:
                    login_success = False
                    name = input("Enter full name")

                    ID = input("Enter your ID: ")

                    login_success = guest1.guest_login(name, ID)

                    if login_success:

                        admin1.remove_guest(name)

                        choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

                        if choice == 'n':

                            is_program_running = True

                        elif choice == 'y':

                            guest_menu = True

                    else:

                        guest_menu = True

    elif choice == '4':

        guest_menu = False

        is_program_running = True


    elif choice == 'e':

        guest_menu = False

        is_program_running = False

    else:

        print("\nYou entered an invalid option, please try again.\n")

        guest_menu = True




    if __name__ == "__main__":

        filename1 = 'data/Guest_data.csv'

        search2 = classes_functions.Admin()

        # choice = None

        guest_verifier = classes_functions.Guest()

        guest_name = input("Enter guest name: ")

        ID = input("Enter guest ID: ")

        print()

        if guest_verifier.guest_login(guest_name, ID):

            print()

            while guest_menu:

                print("\nPlease enter an option")

                print("----------------------------------")

                print("1. Search for available rooms")

                print("2. Check for personal details")

                print("3. Leave room")

                print("4. Back to Main Menu\n")

                print("e. Exit\n")

                login_success = False

                choice = input("> ")

                if choice == '1':

                    print("These are the rooms available:")

                    print("---------------------------------------")

                    admin1.search_available_rooms()

                    choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

                    if choice == 'n':

                        guest_menu = False

                    elif choice == 'y':

                        guest_menu = True

                    else:

                        print("Invalid option, try again")



                elif choice == '2':

                    guest_name = input("Enter your full name: ")

                    ID = input("Enter your ID: ")

                    login_success = guest1.guest_login(guest_name, ID)

                    if login_success:

                        admin1.search_for_guest(guest_name, ID)

                        choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

                        if choice == 'n':

                            guest_menu = False

                        elif choice == 'y':

                            guest_menu = True

                    else:

                        guest_menu = True


                elif choice == '3':

                    name = input("Enter full name")

                    ID = input("Enter your ID: ")

                    login_success = guest1.guest_login(name, ID)

                    if login_success:

                        admin1.remove_guest(name)

                        choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

                        if choice == 'n':

                            is_program_running = True

                        elif choice == 'y':

                            guest_menu = True

                    else:

                        guest_menu = True


                elif choice == '4':

                    guest_menu = False

                    is_program_running = True


                elif choice == 'e':

                    guest_menu = False

                    is_program_running = False


                # elif choice == 'y':

                #     guest_menu = True

                # elif choice == 'n':

                #     is_program_running = True

                else:

                    print("\nYou entered an invalid option, please try again.\n")

                    guest_menu = True