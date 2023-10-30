#modules imported
import sys
import os
import time
from datetime import datetime
import csv

#ASCII codes for letters used in program
# A = 97
# G = 103
# ESC = 27


#displays at start of program
def intro():
    print('''


      ___           ___           ___                       ___                   
     /__/\         /  /\         /  /\          ___        /  /\                  
     \  \:\       /  /::\       /  /:/_        /  /\      /  /:/_                 
      \__\:\     /  /:/\:\     /  /:/ /\      /  /:/     /  /:/ /\    ___     ___ 
  ___ /  /::\   /  /:/  \:\   /  /:/ /::\    /  /:/     /  /:/ /:/_  /__/\   /  /|
 /__/\  /:/\:\ /__/:/ \__\:\ /__/:/ /:/\:\  /  /::\    /__/:/ /:/ /\ \  \:\ /  /:/
 \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:/~/:/ /__/:/\:\   \  \:\/:/ /:/  \  \:\  /:/ 
  \  \::/       \  \:\  /:/   \  \::/ /:/  \__\/  \:\   \  \::/ /:/    \  \:\/:/  
   \  \:\        \  \:\/:/     \__\/ /:/        \  \:\   \  \:\/:/      \  \::/   
    \  \:\        \  \::/        /__/:/          \__\/    \  \::/        \__\/    
     \__\/         \__\/         \__\/                     \__\/                  
                                    
                                                       
    ''')
#function call to see the output
# intro()


def outro():
    print('''

                                  
                                  
    ,---,.                 ,---,. 
  ,'  .'  \       ,---,  ,'  .' | 
,---.' .' |      /_ ./|,---.'   | 
|   |  |: |,---, |  ' :|   |   .' 
:   :  :  /___/ \.  : |:   :  |-, 
:   |    ; .  \  \ ,' ':   |  ;/| 
|   :     \ \  ;  `  ,'|   :   .' 
|   |   . |  \  \    ' |   |  |-, 
'   :  '; |   '  \   | '   :  ;/| 
|   |  | ;     \  ;  ; |   |    \ 
|   :   /       :  \  \|   :   .' 
|   | ,'         \  ' ;|   | ,'   
`----'            `--` `----'     
                                  

    ''')

#function call to see the output
#outro()

# def split(text, delimiter):
#     # List to store the individual data
#     tokens = []
#     token = ''
#     i = 0
#     while i < len(text):
#         if text[i] == delimiter:
#             # Add the token to the tokens list when a delimiter is found
#             tokens.append(token)
#             token = ''  # Reset the token to an empty string
#         else:
#             token += text[i]  # If no delimiter is found, add character to the token
#         i += 1
#     # When we reach the end of a row, add the last value to the list
#     if token:
#         tokens.append(token)
#     return tokens

# Example usage
# text = "Hello,World,Python"
# delimiter = ','
# result = split(text, delimiter)
# print(result)  # Output: ['Hello', 'World', 'Python']

def get_csv_data(csv_filename):
    data = []
    with open(csv_filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            formatted_row = ' '.join(row)
            formatted_row = formatted_row.replace('\t', ' ')
            data.append(formatted_row)  # Join the CSV row into a single string with spaces instead of tabs
    return data

# Example usage
# csv_filename = 'data/Guest_data.csv'  # Replace this with the actual CSV file name
# csv_data = get_csv_data(csv_filename)
# print(csv_data)


def delete_row(row, search_item):
    row_copy = row.copy()  # Create a copy of the input list to avoid modifying it while iterating
    for item in row_copy:
        if search_item in item:
            row.remove(item)  # Remove the item from the list if it contains the search item


# Example usage
# row = ["apple", "banana", "orange", "apple pie", "grape"]
# search_item = "apple"
# delete_row(row, search_item)
# print(row)  # Output: ['banana', 'orange', 'grape']

def get_current_date():
    # Get the current date and time
    now = datetime.now()
    # Format the current date as a string with the desired format
    formatted_date = now.strftime("%d-%m-%Y")
    return formatted_date

# Example usage
# current_date = get_current_date()
# print(current_date)  # Output: current date in the format "dd-mm-yyyy"

#creates a loading bar animation
def loading_bar_animation():
    total_progress = 100  # Total progress value (e.g., 100%)
    bar_width = 50  # Width of the loading bar in characters

    for progress in range(total_progress + 1):
        completed_width = bar_width * progress // total_progress

        sys.stdout.write("\r[")
        for i in range(bar_width):
            if i < completed_width:
                sys.stdout.write("=")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("] {}%".format(progress))
        sys.stdout.flush()

        # Add a small delay to control the speed of the animation
        time.sleep(0.05)

    print()  # Move to the next line after the loading bar is complete

# Example usage
# loading_bar_animation()

#FILE PATH FOR ROOM DATA CSV FILE
ROOM_DATA = "data/Room_data.csv"
#FILE PATH FOR GUEST DATA CSV FILE
GUEST_DATA = "data/Guest_data.csv"
#FILE PATH FOR ADMIN DATA CSV FILE
ADMIN_DATA = "data/Admin_data.csv"


#ROOM CLASS, constructor to create a Room object that the admin can use, Display Room data
class Room:
    def __init__(self, room_data):
        self.id = room_data[0]
        self.type = room_data[1]
        self.price = room_data[2] + " night"
        self.occupant_count = room_data[3]
        self.status = room_data[4]

    #displays a list of all the rooms
    def show_all_rooms(self):
        try:
            with open('data/Room_data.csv', mode='r') as file:
                reader = csv.reader(file)
                header = next(reader)
                print("Room Data:")
                print("ID\tRoom Type\tOccupancy\tPrice\tAvailability")
                print("-" * 50)
                for row in reader:
                    room_id, room_type, price, occupancy, availability = row
                    print(f"{room_id}\t{room_type}\t\t{occupancy}\t\t{price}\t\t{availability}")
        except FileNotFoundError:
            print("Error: Room data file not found.")
        except Exception as e:
            print(f"An error occurred : {e}")

    # def display_room_data(self):
    #     border = "+--------------+-----------------------------------+"
    #     time.sleep(0.9)
    #     print(border)
    #     print("| Room Id      | {:<34} |".format(self.id))
    #     # Set the console text color based on the room type
    #     if self.type == "Single":
    #         print(border)
    #         print("| Room Type    | {:<34} |".format(self.type))
    #     elif self.type == "Double":
    #         print(border)
    #         print("| Room Type    | {:<34} |".format(self.type))
    #     elif self.type == "Triple":
    #         print(border)
    #         print("| Room Type    | {:<34} |".format(self.type))
    #     else:
    #         print(border)
    #         print("| Room Type    | {:<34} |".format(self.type))
    #     print(border)
    #     print("| Price        | {:<34} |".format(self.price))
    #     print(border)
    #     print("| Occupant No. | {:<34} |".format(self.occupant_count))
    #     print(border)
    #     # Set the console text color based on the status
    #     if self.status == "Unavailable":
    #         print(border)
    #         print("| Status       | {:<34} |".format(self.status))
    #     elif self.status == "Available":
    #         print(border)
    #         print("| Status       | {:<34} |".format(self.status))
    #     print(border)
    #     print()
    #     time.sleep(0.9)


# ADMIN CLASS, constructor to create an admin object that the admin can use, Display Admin data
#inherits contents from Room class
class Admin(Room):
    def __init__(self):
        pass
        # self.name = ""
        # self.password = ""

    # import csv
    #a method that authentics an admin to display admin menu
    def admin_login(self, admin_name, password):
        try:
            with open('data/Admin_data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == admin_name and row[1] == password: #iterates through file to confirm deatils
                        print(f"Welcome {admin_name}")
                        return True
        except FileNotFoundError: #exception handle
            print("Error: Admins data file not found.")
        except Exception as e:
            print(f"An error occured : {e}")

        print("Username or Password invalid!!")
        return False
    
    #a method to search for all rooms and display it
    def search_for_room(self, room_id):
        try:
            with open('data/Room_data.csv', mode='r') as file:
                reader = csv.reader(file)
                # headers = next(reader) skip header row
                for row in reader:
                    if (row[0]) == room_id:
                        # if row[4] == 'Available':
                        print("Room ID:", row[0])
                        print("Room Type:", row[1])
                        print("Occupancy:", row[2])
                        print("Price:", row[3])
                        print("Availability:", row[4])
                        return
                print("Room not found.")
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"Error: {e}")

    # Example usage
# if __name__ == "__main__":
#     filename = 'data/Admin_data.csv'
#     admin_verifier = Admin(filename)
#     admin_name = input("Enter admin name: ")
#     password = input("Enter admin password: ")
#
#     if admin_verifier.admin_login(admin_name, password):
#         print("Admin verified. Access granted.")
#     else:
#         print("Invalid admin credentials. Access denied.")

    # def admin_login(self):
    #     login_status = False
    #     print("\nEnter Admin ID (For testing, Enter Adminho): ")
    #     admin_id = input()
    #     print("\nEnter password (For testing, Enter xy4567): ")
    #     admin_password = input()
    #     admin_database = get_csv_data(ADMIN_DATA)
    #     for admin_data in admin_database:
    #         admin_info = admin_data.split(',')
    #         if admin_info[0] == admin_id and admin_info[1] == admin_password:
    #             login_status = True
    #             break
    #     if not login_status:
    #         print("Invalid Login! Please try again\n")
    #     return login_status

    # def show_all_rooms(self):
    #     rows = get_csv_data(ROOM_DATA)
    #     print("\nDisplaying all Rooms...")
    #     loading_bar_animation()
    #     for row in rows:
    #         room = Room(row.split(','))
    #         room.display_room_data()

    # def show_all_rooms(self):
    #     try:
    #         with open('data/Room_data.csv', mode='r') as file:
    #             reader = csv.reader(file)
    #             header = next(reader)
    #             print("Room Data:")
    #             print("ID\tRoom Type\tOccupancy\tPrice\tAvailability")
    #             print("-" * 50)
    #             for row in reader:
    #                 room_id, room_type, price, occupancy, availability = row
    #                 print(f"{room_id}\t{room_type}\t\t{occupancy}\t\t{price}\t\t{availability}")
    #     except FileNotFoundError:
    #         print("Error: Room data file not found.")
    #     except Exception as e:
    #         print(f"An error occurred : {e}")




    # def search_for_room(self):
    #     success = False
    #     while not success:
    #         room_id = input("\nEnter Room ID: ")
    #         rows = get_csv_data(ROOM_DATA)
    #         is_room_found = False
    #         print("\nSearching for Room " + room_id + " ...")
    #         loading_bar_animation()
    #         for row in rows:
    #             if row.split(',')[0] == room_id:
    #                 is_room_found = True
    #                 room = Room(row.split(','))
    #                 room.show_all_rooms()
    #                 success = True
    #                 break
    #         if not is_room_found:
    #             print("\nRoom not found. Please try again\n")


    # def search_available_rooms(self):
    #     rows = get_csv_data(ROOM_DATA)
    #     are_rooms_found = False
    #     for row in rows:
    #         data = row.split(',')
    #         if data[4] == "Available":
    #             are_rooms_found = True
    #             room = Room(data)
    #             room.display_room_data()
    #     if not are_rooms_found:
    #         print("\nNo available Rooms. Check again later\n")
    
    #a method to search for available rooms in csv file
    def search_available_rooms(self):
        try:
            with open('data/Room_data.csv', mode='r') as file:
                reader = csv.reader(file)
                headers = next(reader) #skip header row
                print("\nAvailable Rooms:")
                for row in reader:
                    room_id, room_type, occupancy, price, availability = row
                    if availability.lower() == 'available':
                        print(f"{room_id}, {room_type}, {occupancy}, {price}, {availability}")
                print()  # Add a newline for better formatting
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"Error: {e}")

    #a method to add a room into csv file
    def add_room(self):
        room_id = input("Enter Room ID: ")
        room_type = input("Enter Room Type(Single,Double,Triple,Quadruple): ")
        occupancy = int(input("Enter Occupancy: "))
        price = int(input("Enter Price: "))
        status = input("Enter Status: ")

        try:
            with open('data/Room_data.csv', 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([room_id, room_type, price, occupancy, status])
            print(f"Room {room_id} added successfully.")
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # def get_room_by_type(self):
    #     success = False
    #     while not success:
    #         print("\nSelect preferred Room Type: \n1 - Single\n2 - Double\n3 - Triple\n4 - Quadruple")
    #         choice = int(input("Your Choice: "))
    #         room_types = ["Single", "Double", "Triple", "Quadruple"]
    #         if 1 <= choice <= 4:
    #             room_type = room_types[choice - 1]
    #             rows = get_csv_data(ROOM_DATA)
    #             are_rooms_found = False
    #             print("\nSearching for Available Rooms...")
    #             loading_bar_animation()
    #             for row in rows:
    #                 data = row.split(',')
    #                 if data[1] == room_type and data[4] == "Available":
    #                     are_rooms_found = True
    #                     room = Room(data)
    #                     room.display_room_data()
    #             if not are_rooms_found:
    #                 print("\nNo available rooms of this type. Check again later\n")
    #             else:
    #                 success = True
    #         else:
    #             print("\nInvalid Option. Please try again\n")

    #a method to remove a room from csv file
    def remove_room(self, room_id):
        try:
            with open('data/Room_data.csv', 'r') as file:
                rooms = list(csv.reader(file))
            with open('data/Room_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                room_found = False
                for room in rooms:
                    if room[0] == room_id:
                        room_found = True
                        print(f"Room {room_id} removed successfully.")
                    else:
                        writer.writerow(room)
                if not room_found:
                    print(f"Room {room_id} not found.")
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    #a method to show all guests and details in csv file
    def show_all_guests(self):
        try:
            with open('data/Guest_data.csv', mode='r') as file:
                reader = csv.reader(file)
                header = next(reader)
                print("Guest Data:")
                print("Guest ID\tGuest Name\tPhone Number\troom_id\tDate Arrived")
                print("-" * 70)
                for row in reader:
                    guest_id, guest_name, phone_no, room_id, date = row
                    print(f"{guest_id}\t{guest_name}\t\t{phone_no}\t\t{phone_no}\t\t{date}")
        except FileNotFoundError:
            print("Error: Room data file not found.")
        except Exception as e:
            print(f"An error occurred : {e}")

    #a method to search for a particular guest
    def search_for_guest(self, guest_name):
        try:
            with open('data/Guest_data.csv', mode='r') as file:
                reader = csv.reader(file)
                # headers = next(reader) skip header row
                for row in reader:
                    if (row[1]) == guest_name:
                        print("Guest ID: ", row[0])
                        print("Guest name: ", row[1])
                        print("Phone no: ", row[2])
                        print("room ID: ", row[3])
                        print("Date: ", row[4])
                        return
                print("Guest not found.")
        except FileNotFoundError:
            print("Error: Guest CSV file not found.")
        except Exception as e:
            print(f"Error: {e}")

    #a method to add a guest to csv file
    def add_guest(self):
        guest_id = input("Enter Guest ID: ")
        guest_name = input("Enter Guest name: ")
        phone_no = input("Enter Phone no: ")
        room_id = input("Enter room ID: ")
        date = input("Enter date in format (DD-MM-YY): ")

        try:
            with open('data/Guest_data.csv', 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([guest_id, guest_name, phone_no, room_id, date])
            print(f"{guest_name} added successfully.")
        except FileNotFoundError:
            print("Error: Guest CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    #a method to remove guest from csv file
    def remove_guest(self, guest_name):
        try:
            with open('data/Guest_data.csv', 'r') as file:
                guests = list(csv.reader(file))
            with open('data/Guest_data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                guest_found = False
                for guest in guests:
                    if guest[1] == guest_name:
                        guest_found = True
                        print(f"Guest {guest_name} removed successfully.")
                    else:
                        writer.writerow(guest)
                if not guest_found:
                    print(f"Guest, {guest_name} not found.")
        except FileNotFoundError:
            print("Error: Guest CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


# GUEST CLASS, constructor to create an guest object that the guest can use
class Guest:
    def __init__(self, guest_data=None):
        self.id = guest_data[0] if guest_data else ""
        self.name = guest_data[1] if guest_data else ""
        self.contact_info = guest_data[2] if guest_data else ""
        self.room_id = guest_data[3] if guest_data else ""
        self.arrival_date = guest_data[4] if guest_data else ""

    # def get_details(self):
    #     time.sleep(0.9)
    #     print("+---------------+-----------------------------------+")
    #     print("| Guest Id      | {:<34} |".format(self.id))
    #     print("+---------------+-----------------------------------+")
    #     print("| Guest Name    | {:<34} |".format(self.name))
    #     print("+---------------+-----------------------------------+")
    #     print("| Contact Info  | {:<34} |".format(self.contact_info))
    #     print("+---------------+-----------------------------------+")
    #     print("| Room Id       | {:<34} |".format(self.room_id))
    #     print("+---------------+-----------------------------------+")
    #     print("| Arrival Date  | {:<34} |".format(self.arrival_date))
    #     print("+---------------+-----------------------------------+\n")

    # @staticmethod
    # def guest_login(name=None, ID=None):
    #     login_status = False
    #     if name is None or ID is None:
    #         print("\nEnter First name (For testing, Enter \"Vince\"): ")
    #         f_name = input()
    #         print("\nEnter Last name(For testing, Enter \"Churchill\"): ")
    #         l_name = input()
    #         print("\nEnter ID(For testing, Enter \"Y678\"): ")
    #         guest_id = input()
    #         guest_name = l_name + " " + f_name
    #     else:
    #         guest_id = ID
    #         guest_name = name
    #
    #     guest_database = get_csv_data(GUEST_DATA)
    #     for guest_data in guest_database:
    #         guest_info = guest_data.split(',')
    #         if guest_info[0] == guest_id and guest_info[1] == guest_name:
    #             print("Welcome " + guest_name)
    #             login_status = True
    #             break
    #
    #     if not login_status:
    #         print("\x1b[31m" + "Invalid Login! Please try again\n" + "\x1b[0m")
    #
    #     return login_status

    #a method to authenticate guest into the system
    def guest_login(self, guest_name, ID):
        try:
            with open('data/Guest_data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == guest_name and row[0] == ID:
                        # print(f"Welcome {guest_name}")
                        return True
        except FileNotFoundError:
            print("Error: Guest's data file not found.")
        except Exception as e:
            print(f"An error occured : {e}")

        print("Name or ID invalid!!")
        return False

    # @staticmethod
    # def guest_login_by_input():
    #     return Guest.guest_login()

    

#FILE PATH FOR ROOM DATA CSV FILE
# ROOM_DATA = "data/Room_Details.csv"
# FILE PATH FOR GUEST DATA CSV FILE
# GUEST_DATA = "data/Guest_Data.csv"
# FILE PATH FOR ADMIN DATA CSV FILE
# ADMIN_DATA = "data/Admin_data.csv"
