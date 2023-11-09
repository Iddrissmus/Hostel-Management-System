# import csv
# # #
# # # class HotelManager:
# # #     def __init__(self, csv_file):
# # #         self.csv_file = csv_file
# # #
# # #     def search_available_rooms(self):
# # #         try:
# # #             with open(self.csv_file, 'r') as file:
# # #                 csv_reader = csv.reader(file)
# # #                 next(csv_reader)  # Skip header row if exists
# # #                 available_rooms = []
# # #                 for row in csv_reader:
# # #                     room_id, room_type, occupancy, price, availability = row
# # #                     if availability.lower() == 'available':
# # #                         available_rooms.append({
# # #                             'Room ID': room_id,
# # #                             'Room Type': room_type,
# # #                             'Occupancy': occupancy,
# # #                             'Price': price,
# # #                             'Availability': availability
# # #                         })
# # #
# # #                 if available_rooms:
# # #                     print("\nAvailable Rooms:")
# # #                     for room in available_rooms:
# # #                         print(room)
# # #                 else:
# # #                     print("\nNo available rooms.")
# # #         except FileNotFoundError:
# # #             print("Error: Room CSV file not found.")
# # #         except Exception as e:
# # #             print(f"An error occurred: {e}")
# # #
# # # # Example usage
# # # if __name__ == "__main__":
# # #     csv_file = 'data/Room_data.csv'  # Replace 'rooms.csv' with your actual CSV file name
# # #     hotel_manager = HotelManager(csv_file)
# # #     hotel_manager.search_available_rooms()
# #
# #
# # import csv
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
# #                 print("\nAvailable Rooms:")
# #                 for row in csv_reader:
# #                     room_id, room_type, occupancy, price, availability = row
# #                     if availability.lower() == 'available':
# #                         print(f"{room_id}, {room_type}, {occupancy}, {price}, {availability}")
# #                 print()  # Add a newline for better formatting
# #         except FileNotFoundError:
# #             print("Error: Room CSV file not found.")
# #         except Exception as e:
# #             print(f"An error occurred: {e}")
# #
# # # Example usage
# # # if __name__ == "__main__":
# # csv_file = 'data/Room_data.csv'  # Replace 'rooms.csv' with your actual CSV file name
# # hotel_manager = HotelManager(csv_file)
# # hotel_manager.search_available_rooms()
# #

# #
# # if __name__ == "__main__":
# #             filename = 'data/Admin_data.csv'
# #             admin_verifier = classes_functions.Admin()
# #             search1 = classes_functions.Admin()
# #             admin_name = input("Enter admin name: ")
# #             password = input("Enter admin password: ")
# #
# #             if admin_verifier.admin_login(admin_name, password):
# #                 print()
# #                 while admin_menu:
# #                     print("\nPlease enter an option")
# #                     print("---------------------------------")
# #                     print("1. Show all rooms")
# #                     print("2. Search for a particular room")
# #                     print("3. Search for available rooms")
# #                     print("4. Add room")
# #                     print("5. Remove a room")
# #                     print("6. Show all guests")
# #                     print("7. Search for Guest")
# #                     print("8. Add Guest")
# #                     print("9. Remove Guest")
# #                     print("b. Back to main menu")
# #                     print("e. Exit")
# #
# #                     choice = input("> ")
# #
# #                     if choice == '1':
# #                         classes_functions.loading_bar_animation()
# #                         admin1.show_all_rooms()
# #                         choice = input("\nPerform another task? (y/n[Back to main menu])\n> ")
# #                         if choice == 'n':
# #                             admin_menu = False
# #                         elif choice == 'y':
# #                             admin_menu = True
# #                         else:
# #                             #correct infinite loop
# #                             print("Invalid Option, try again")
# # option = input()
# elif option == 'g':
#     print("\nPlease enter an option")
#     print("----------------------------------")
#     print("1. Search for available rooms")
#     print("2. Check for personal details")
#     print("3. Leave room")
#     print("4. Back to Main Menu\n")
#     print("e. Exit\n")

#     choice = input("> ")

#     if choice == '1':

#         print("These are the rooms available:")

#         print("---------------------------------------")

#         admin1.search_available_rooms()

#         choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

#         if choice == 'n':

#             guest_menu = False

#         elif choice == 'y':

#             guest_menu = True

#         else:

#             print("Invalid option, try again")

#     elif choice == '2':
#         if __name__ == "__main__":

#             filename1 = 'data/Guest_data.csv'

#             search2 = classes_functions.Admin()

#             # choice = None

#             guest_verifier = classes_functions.Guest()

#             guest_name = input("Enter guest name: ")

#             ID = input("Enter guest ID: ")

#             print()

#             if guest_verifier.guest_login(guest_name, ID):

#                 print()

#                 while guest_menu:
#                     login_success = False
#                     guest_name = input("Enter your full name: ")

#                     ID = input("Enter your ID: ")

#                     login_success = guest1.guest_login(guest_name, ID)

#                     if login_success:

#                         admin1.search_for_guest(guest_name, ID)

#                         choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

#                         if choice == 'n':

#                             guest_menu = False

#                         elif choice == 'y':

#                             guest_menu = True

#                     else:

#                         guest_menu = True
#     elif choice == '3':
#         if __name__ == "__main__":

#             filename1 = 'data/Guest_data.csv'

#             search2 = classes_functions.Admin()

#             # choice = None

#             guest_verifier = classes_functions.Guest()

#             guest_name = input("Enter guest name: ")

#             ID = input("Enter guest ID: ")

#             print()

#             if guest_verifier.guest_login(guest_name, ID):

#                 print()

#                 while guest_menu:
#                     login_success = False
#                     name = input("Enter full name")

#                     ID = input("Enter your ID: ")

#                     login_success = guest1.guest_login(name, ID)

#                     if login_success:

#                         admin1.remove_guest(name)

#                         choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

#                         if choice == 'n':

#                             is_program_running = True

#                         elif choice == 'y':

#                             guest_menu = True

#                     else:

#                         guest_menu = True

#     elif choice == '4':

#         guest_menu = False

#         is_program_running = True


#     elif choice == 'e':

#         guest_menu = False

#         is_program_running = False

#     else:

#         print("\nYou entered an invalid option, please try again.\n")

#         guest_menu = True




#     if __name__ == "__main__":

#         filename1 = 'data/Guest_data.csv'

#         search2 = classes_functions.Admin()

#         # choice = None

#         guest_verifier = classes_functions.Guest()

#         guest_name = input("Enter guest name: ")

#         ID = input("Enter guest ID: ")

#         print()

#         if guest_verifier.guest_login(guest_name, ID):

#             print()

#             while guest_menu:

#                 print("\nPlease enter an option")

#                 print("----------------------------------")

#                 print("1. Search for available rooms")

#                 print("2. Check for personal details")

#                 print("3. Leave room")

#                 print("4. Back to Main Menu\n")

#                 print("e. Exit\n")

#                 login_success = False

#                 choice = input("> ")

#                 if choice == '1':

#                     print("These are the rooms available:")

#                     print("---------------------------------------")

#                     admin1.search_available_rooms()

#                     choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

#                     if choice == 'n':

#                         guest_menu = False

#                     elif choice == 'y':

#                         guest_menu = True

#                     else:

#                         print("Invalid option, try again")



#                 elif choice == '2':

#                     guest_name = input("Enter your full name: ")

#                     ID = input("Enter your ID: ")

#                     login_success = guest1.guest_login(guest_name, ID)

#                     if login_success:

#                         admin1.search_for_guest(guest_name, ID)

#                         choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

#                         if choice == 'n':

#                             guest_menu = False

#                         elif choice == 'y':

#                             guest_menu = True

#                     else:

#                         guest_menu = True


#                 elif choice == '3':

#                     name = input("Enter full name")

#                     ID = input("Enter your ID: ")

#                     login_success = guest1.guest_login(name, ID)

#                     if login_success:

#                         admin1.remove_guest(name)

#                         choice = input("\nPerform another action?(y/n [Back to main menu])\n > >")

#                         if choice == 'n':

#                             is_program_running = True

#                         elif choice == 'y':

#                             guest_menu = True

#                     else:

#                         guest_menu = True


#                 elif choice == '4':

#                     guest_menu = False

#                     is_program_running = True


#                 elif choice == 'e':

#                     guest_menu = False

#                     is_program_running = False


#                 # elif choice == 'y':

#                 #     guest_menu = True

#                 # elif choice == 'n':

#                 #     is_program_running = True

#                 else:

#                     print("\nYou entered an invalid option, please try again.\n")

#                     guest_menu = True

# def set_visitorsName():
#         while True:
#             name = input("Enter Guest Name: ")
#             visName = name.title()
#             if visName.replace(" ","").isalpha():
#                 __visitorsName = visName
#                 break
#             else:
#                 print("Name should include only letters! ")



# set_visitorsName()




# import csv

# room_type_max_occupancy = {
#     '2 in 1': 2,
#     '3 in 1': 3,
#     '4 in 1': 4,
#     '1 in 1': 1
# }

# def add_guest_to_room(room_id):
#     # rooms = []
#     updated = False

#     with open('data/testroom.csv', 'r') as file:
#         rooms = list(csv.DictReader(file))
#         for room in rooms:
#             if room['ID'] == room_id:
#                 max_occupancy = room_type_max_occupancy.get(room['Room Type'], 0)
#                 if int(room['Occupancy']) < max_occupancy and room['Availability'] == 'Available':
#                     room['Occupancy'] = str(int(room['Occupancy']) + 1)  # Increase occupancy
#                     if int(room['Occupancy']) == max_occupancy:
#                         room['Availability'] = 'Uavailable'
#                     # room['Availability'] = 'Unavailable'  # Mark room as unavailable
#                     updated = True
#             # rooms.append(room)

#     if updated:
#         fieldnames = ['ID', 'Room Type', 'Price', 'Occupancy', 'Availability']
#         with open('data/testroom.csv', 'w', newline='') as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(rooms)
#         print(f"Guest added to Room {room_id}.")
#     else:
#         print(f"No available room with ID {room_id} or Room {room_id} is full.")

# Example usage
# room_id = input("Enter Room ID to add guest: ")
# add_guest_to_room(room_id)


# import csv

# def read_room_data(file_path):
#     rooms = []
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip the header row
#         for row in csv_reader:
#             room_id, room_type, price, occupancy, availability = row
#             rooms.append({
#                 'id': room_id,
#                 'type': room_type,
#                 'price': int(price),
#                 'occupancy': int(occupancy),
#                 'availability': availability.strip().lower() == 'available'
#             })
#     return rooms

# def update_room_data(file_path, rooms):
#     with open(file_path, 'w', newline='') as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow(['ID', 'Room Type', 'Price', 'Occupancy', 'Availability'])
#         for room in rooms:
#             csv_writer.writerow([room['id'], room['type'], room['price'], room['occupancy'], 'Available' if room['availability'] else 'Unavailable'])

# def add_guests_to_rooms(rooms):
#     for room in rooms:
#         if room['availability'] and room['occupancy'] < room_type_max_occupancy[room['type']]:
#             room['occupancy'] += 1
#             print(f"Guest added to Room {room['id']} (Room Type: {room['type']}). Current occupancy: {room['occupancy']}")

# # Define the maximum occupancy for each room type
# room_type_max_occupancy = {
#     '2 in 1': 2,
#     '3 in 1': 3,
#     '4 in 1': 4,
#     '1 in 1': 1
# }

# # Path to the room CSV file
# room_file_path = 'data/testroom.csv'

# # Read room data from the CSV file
# rooms = read_room_data(room_file_path)

# # Add guests to rooms until they reach their maximum occupancy
# add_guests_to_rooms(rooms)

# # Update the room data in the CSV file
# update_room_data(room_file_path, rooms)


import csv

class YourClass:
    def __init__(self):
        self.visitorsName = ""

    def set_visitorsName(self):
        while True:
            name = input("Name: ")
            visName = name.title()
            if visName.replace(" ", "").isalpha():
                self.visitorsName = visName
                self.write_to_csv()
                break
            else:
                print("Invalid Name! Please enter a valid name with letters and spaces.")

    def write_to_csv(self):
        with open('data/testguest.csv', 'a', newline='') as csvfile:
            fieldnames = ['Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'Name': self.visitorsName})
            print("Name added to CSV file successfully!")

# Example usage
your_object = YourClass()
your_object.set_visitorsName()
