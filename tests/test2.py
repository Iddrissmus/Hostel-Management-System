# import csv

# import classes_functions


# class Admin:
#     def __init__(self):
#         pass


#     def guest_login(self, guest_name, ID):
#         try:
#             with open('data/testguest.csv', mode='r') as file:
#                 reader = csv.reader(file)
#                 for row in reader:
#                     if row[1] == guest_name and row[0] == ID:
#                         print(f"Welcome {guest_name}")
#                         return True
#         except FileNotFoundError:
#             print("Error: Guest's data file not found.")
#         except Exception as e:
#             print(f"An error occured : {e}")

#         print("Name or ID invalid!!")
#         return False

# guest_verifier = classes_functions.Guest()
# guest_name = input("Enter guest name: ")
# ID = input("Enter guest ID: ")
# guest_verifier.guest_login(guest_name, ID)
# #
# #     def check_room_availability(self, room_id):
# #         try:
# #             with open(self.room_csv, 'r') as file:
# #                 rooms = list(csv.reader(file))
# #             for room in rooms:
# #                 if room[0] == room_id:
# #                     if room[4] == 'Available':
# #                         return True
# #                     else:
# #                         print(f"Room {room_id} is not available.")
# #                         return False
# #             print(f"Room {room_id} not found.")
# #             return False
# #         except FileNotFoundError:
# #             print("Error: Room CSV file not found.")
# #             return False
# #         except Exception as e:
# #             print(f"An error occurred: {e}")
# #             return False
# #
# #     def add_guest(self, guest_name, room_id):
# #         try:
# #             if self.check_room_availability(room_id):
# #                 with open(self.guest_csv, 'a', newline='') as file:
# #                     csv_writer = csv.writer(file)
# #                     csv_writer.writerow([guest_name, room_id])
# #                 print(f"Guest {guest_name} added successfully to Room {room_id}.")
# #                 with open(self.room_csv, 'r') as file:
# #                     rooms = list(csv.reader(file))
# #                 with open(self.room_csv, 'w', newline='') as file:
# #                     csv_writer = csv.writer(file)
# #                     for room in rooms:
# #                         if room[0] == room_id:
# #                             room[4] = 'Unavailable'
# #                         csv_writer.writerow(room)
# #             else:
# #                 print("Failed to add guest.")
# #         except FileNotFoundError:
# #             print("Error: Guest or Room CSV file not found.")
# #         except Exception as e:
# #             print(f"An error occurred: {e}")
# #
# # # Example usage:
# # if __name__ == "__main__":
# #     admin = Admin('data/testroom.csv', "data/testguest.csv")
# #     guest_name = input("Enter guest name: ")
# #     room_id = input("Enter room ID: ")
# #     admin.add_guest(guest_name, room_id)

# #     def search_for_guest(self, guest_name):
# #         try:
# #             with open('data/testguest.csv', mode='r') as file:
# #                 reader = csv.reader(file)
# #                 # headers = next(reader) skip header row
# #                 for row in reader:
# #                     if (row[1]) == guest_name:
# #                         # if row[4] == 'Available':
# #                         print("Guest ID: ", row[0])
# #                         print("Guest name: ", row[1])
# #                         print("Phone no: ", row[2])
# #                         print("room ID: ", row[3])
# #                         print("Date: ", row[4])
# #                         return
# #                 print("Guest not found.")
# #         except FileNotFoundError:
# #             print("Error: Guest CSV file not found.")
# #         except Exception as e:
# #             print(f"Error: {e}")




# # admin2 = Admin()
# # guest_name = input("Enter guest name: ")
# # admin2.search_for_guest(guest_name)