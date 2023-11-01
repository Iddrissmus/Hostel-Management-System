# import sys
# import time
# def loading_bar_animation():
#     total_progress = 100  # Total progress value (e.g., 100%)
#     bar_width = 50  # Width of the loading bar in characters

#     for progress in range(total_progress + 1):
#         completed_width = bar_width * progress // total_progress

#         sys.stdout.write("\r[")
#         for i in range(bar_width):
#             if i < completed_width:
#                 sys.stdout.write("=")
#             else:
#                 sys.stdout.write(" ")
#         sys.stdout.write("] {}%".format(progress))
#         sys.stdout.flush()

#         # Add a small delay to control the speed of the animation
#         time.sleep(0.05)

#     print()  # Move to the next line after the loading bar is complete

# # loading_bar_animation()

              
#                 # | |  | |  / __ \   / ____| |__   __| |  ____| | |     
#                 # | |__| | | |  | | | (___      | |    | |__    | |     
#                 # |  __  | | |  | |  \___ \     | |    |  __|   | |     
#                 # | |  | | | |__| |  ____) |    | |    | |____  | |____ 
#                 # |_|  |_|  \____/  |_____/     |_|    |______| |______|

# print('''  

                                  
                                  
#     ,---,.                 ,---,. 
#   ,'  .'  \       ,---,  ,'  .' | 
# ,---.' .' |      /_ ./|,---.'   | 
# |   |  |: |,---, |  ' :|   |   .' 
# :   :  :  /___/ \.  : |:   :  |-, 
# :   |    ; .  \  \ ,' ':   |  ;/| 
# |   :     \ \  ;  `  ,'|   :   .' 
# |   |   . |  \  \    ' |   |  |-, 
# '   :  '; |   '  \   | '   :  ;/| 
# |   |  | ;     \  ;  ; |   |    \ 
# |   :   /       :  \  \|   :   .' 
# |   | ,'         \  ' ;|   | ,'   
# `----'            `--` `----'     
                                  



# ''')




# # import pyfiglet
  
# # result = pyfiglet.figlet_format("CodeSnail")
# # print(result)
import csv

def add_room():
        room_id = (input("Enter Room ID: "))
        room_type = input("Enter Room Type: ")
        occupancy = int(input("Enter Occupancy: "))
        price = int(input("Enter Price: "))
        status = input("Enter Status: ")

        if check_room_id(room_id):
             print(f"Error: Room ID {room_id} already exists. Please enter a unique Room ID.")
             return add_room()

        try:
            with open('data/testroom.csv', 'a', newline='') as file:
                csv_writer = csv.writer(file) 
                csv_writer.writerow([room_id, room_type, price, occupancy, status])
            print(f"Room {room_id} added successfully.")
        except FileNotFoundError:
            print("Error: Room CSV file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

def check_room_id(room_id):
    try:
          with open('data/testroom.csv', 'r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    existing_room_id = (row[0])
                    if existing_room_id == room_id:
                        return True
    except FileNotFoundError:
        print("Error: Room CSV file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False

add_room()