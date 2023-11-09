#modules imported
import sys
import time
from datetime import datetime
import csv
import string

current_date = datetime.now().strftime("%d-%m-%y")

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
        time.sleep(0.01)
        
    print()  # Move to the next line after the loading bar is complete

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
        self.price = room_data[2]
        self.occupant_count = room_data[3]
        self.status = room_data[4]

    #displays a list of all the rooms
    def show_all_rooms(self):
        try:
            with open('data/Room_data.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                print("Room Data: ")
                print("ID\tRoom Type\tOccupancy\tPrice  \tAvailability")
                print("-" * 65)
                for row in reader:
                    room_id, room_type, price, occupancy, availability = row
                    print(f"{room_id}\t{room_type}\t\t{occupancy}\t\t{price}\t{availability}")
        except FileNotFoundError:
            print("Error: Room data file not found.")
        except Exception as e:
            print(f"An error occurred : {e}")

# ADMIN CLASS, constructor to create an admin object that the admin can use, Display Admin data
#inherits contents from Room class
class Admin(Room):
    def __init__(self):
        self.room_type_max_occupancy = {
            '2 in 1': 2,
            '3 in 1': 3,
            '4 in 1': 4,
            '1 in 1': 1 
        }

    #a method that authentics an admin to display admin menu
    def admin_login(self, admin_name, password):
        try:
            with open('data/Admin_data.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader)
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
                next(reader) #skip header row
                for row in reader:
                    if (row[0]) == room_id:
                        print("Room ID: ", row[0])
                        print("Room Type: ", row[1])
                        print("Price: ", row[2])
                        print("Occupancy: ", row[3])
                        print("Availability: ", row[4])
                        return
                print("Room not found.")
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"Error: {e}")
    
    #a method to search for available rooms in csv file
    def search_available_rooms(self):
        try:
            with open('data/Room_data.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader) #skip header row
                print("\nAvailable Rooms: ")
                print("ID\tRoom Type\tOccupancy\tPrice\tAvailability")
                print("-" * 63)
                for row in reader:
                    room_id, room_type, price, occupancy,  availability = row
                    if availability.lower() == 'available':
                        print(f"{room_id}\t{room_type}\t\t{occupancy}\t\t{price}\t{availability}")
                print()  # Add a newline for better formatting
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"Error: {e}")

    #a method to add a room into csv file
    # def add_room(self):
    #     while True:
    #         try:
    #             room_id = int((input("Enter Room ID: ")))
    #             room_type = input("Enter Room Type: ")
    #             price = int(input("Enter Price: "))
    #             occupancy = int(input("Enter Occupancy: "))
    #             status = input("Enter Status: ")
    #             break
    #         except ValueError:
    #             print("Invalid Option Entered. Try again")
    #             continue

    #     if self.check_room_id(room_id):
    #          print(f"Error: Room ID {room_id} already exists. Please enter a unique Room ID.")
    #          return self.add_room()

    #     try:
    #         with open('data/Room_data.csv', 'a', newline='') as file:
    #             csv_writer = csv.writer(file)
    #             csv_writer.writerow([room_id, room_type, price, occupancy, status])
    #         print(f"Room {room_id} added successfully.")
    #     except FileNotFoundError:
    #         print("Error: Room CSV file not found.")
    #     except Exception as e:
    #         print(f"An error occurred: {e}")

    # room_type_max_occupancy = {
    # '2 in 1': 2,
    # '3 in 1': 3,
    # '4 in 1': 4,
    # '1 in 1': 1 }


    def add_guest_to_room(self, room_id):
        # rooms = []
        updated = False

        with open('data/Room_data.csv', 'r') as file:
            rooms = list(csv.DictReader(file))
            for room in rooms:
                if room['ID'] == room_id:
                    max_occupancy = self.room_type_max_occupancy.get(room['Room Type'], 0)
                    if int(room['Occupancy']) < max_occupancy and room['Availability'] == 'Available':
                        room['Occupancy'] = str(int(room['Occupancy']) + 1)  # Increase occupancy
                        if int(room['Occupancy']) == max_occupancy:
                            room['Availability'] = 'Uavailable'
                        # room['Availability'] = 'Unavailable'  # Mark room as unavailable
                        updated = True
                # rooms.append(room)

        if updated:
            fieldnames = ['ID', 'Room Type', 'Price', 'Occupancy', 'Availability']
            with open('data/Room_data.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rooms)
            print(f"Guest added to Room {room_id}.")
        else:
            print(f"No available room with ID {room_id} or Room {room_id} is full.")

    def remove_guest_from_room(self, room_id):
        # rooms = []
        updated = False

        with open('data/Room_data.csv', 'r') as file:
            rooms = list(csv.DictReader(file))
            for room in rooms:
                if room['ID'] == room_id:
                    max_occupancy = self.room_type_max_occupancy.get(room['Room Type'], 0)
                    if int(room['Occupancy']) > 0:
                        if int(room['Occupancy']) < max_occupancy or int(room['Occupancy']) == max_occupancy and room['Availability'] == 'Available':
                            room['Occupancy'] = str(int(room['Occupancy']) - 1)  # Decrease occupancy
                            if int(room['Occupancy']) < max_occupancy:
                                room['Availability'] = 'Available'
                            # room['Availability'] = 'Unavailable'  # Mark room as unavailable
                            updated = True
                # rooms.append(room)

        if updated:
            fieldnames = ['ID', 'Room Type', 'Price', 'Occupancy', 'Availability']
            with open('data/Room_data.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rooms)
            print(f"Guest added to Room {room_id}.")
        else:
            print(f"No available room with ID {room_id} or Room {room_id} is full.")

    def check_room_id(self, room_id):
        try:
            with open('data/Room_data.csv', 'r') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader)
                    for row in csv_reader:
                        existing_room_id = (row[0])
                        if existing_room_id == room_id:
                            return True
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return False
    
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
                next(reader)
                print("Guest Data:")
                print("ID\tGuest Name\t\tPhone Number\t\tRoom_id\tDate Arrived")
                print("-" * 80)
                for row in reader:
                    guest_id, guest_name, phone_no, room_id, date = row
                    print(f"{guest_id}\t{guest_name}\t\t{phone_no}\t\t{room_id}\t{date}")
        except FileNotFoundError:
            print("Error: Room data file not found.")
        except Exception as e:
            print(f"An error occurred : {e}")

    #a method to search for a particular guest
    def search_for_guest(self, guest_name):
        try:
            with open('data/Guest_data.csv', mode='r') as file:
                reader = csv.reader(file)
                next(reader) #skip header row
                for row in reader:
                    if (row[1]) == guest_name:
                        print("Guest ID: ", row[0])
                        print("Guest Name: ", row[1])
                        print("Phone Number: ", row[2])
                        print("Room ID: ", row[3])
                        print("Date Arrived: ", row[4])
                        return
                print(f"Guest {guest_name} not found.")
        except FileNotFoundError:
            print("Error: Guest CSV file not found.")
        except Exception as e:
            print(f"Error: {e}")


    def is_valid_name(self, name):
        return all(char.isalpha() or char.isspace() for char in name)


    # def set_userContact(self):
        while True:
                contact = input("Phone Number: ")  
                if contact.isdigit() and len(contact) == 10 and contact[0] == '0':
                    self.__contact = contact
                    break
                else:
                    print("Invalid contact number format")
            

    # def set_visitorsName(self):
        while True:
            name = input("Enter Guest Name: ")
            visName = name.capitalize().replace(" ", "  ")
            if visName.isalpha():
                self.__visitorsName = visName
                break
            else:
                print("Name should include only letters! ")


    #a method to add a guest to csv file
    def add_guest(self):
        while True:
            try:
                guest_id = input("Enter Guest ID: ")
                guest_name = input("Enter Guest Name: ")

                if not self.is_valid_name(guest_name):
                    print("Invalid name! Please enter a valid name with letters and spaces.")
                    continue
                
                phone_no = input("Enter Phone Number: ")

                if len(phone_no) == 10 and phone_no.isdigit() and phone_no[0] == '0':
                    phone_no = int(phone_no)
                else:
                    print("Invalid phone number! Please enter a 10-digit number starting with 0.")
                    continue
                room_id = int(input("Enter Room ID: "))
                date = current_date
                break
            except ValueError:
                print("Invalid Option Entered! Try again")
                continue

        if self.check_guest_id(guest_id):
            print(f"Error: Guest ID {guest_id} already exists. Please enter a unique Guest ID.")
            return self.add_guest()

        try:
            with open('data/Guest_data.csv', 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([guest_id, guest_name, phone_no, room_id, date])
            print(f"{guest_name} added successfully.")
            print()
            room_id = input("Enter Room ID: ")
            self.add_guest_to_room(room_id)
        except FileNotFoundError:
            print("Error: Guest CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def check_guest_id(self, guest_id):
        try:
            with open('data/Guest_data.csv', 'r') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader)
                    for row in csv_reader:
                        existing_guest_id = (row[0])
                        if existing_guest_id == guest_id:
                            return True
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return False
    
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
    def __init__(self):
        pass
        # self.id = guest_data[0] if guest_data else ""
        # self.name = guest_data[1] if guest_data else ""
        # self.contact_info = guest_data[2] if guest_data else ""
        # self.room_id = guest_data[3] if guest_data else ""
        # self.arrival_date = guest_data[4] if guest_data else ""

    #a method to authenticate guest into the system
    def guest_login(self, guest_name, ID):
        try:
            with open('data/Guest_data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == guest_name and row[0] == ID:
                        return True
        except FileNotFoundError:
            print("Error: Guest data file not found.")
        except Exception as e:
            print(f"An error occured : {e}")

        print("Name or ID invalid!!")
        return False

