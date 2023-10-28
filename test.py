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