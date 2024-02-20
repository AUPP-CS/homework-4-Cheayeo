# from asciitryfunction import caesar
# import os
# import platform

# # Your code goes here
# def welcoming_screen():
#     print('''
#                                                         🌹🌷🌻 %៛#===========================================================
# \t\t\t\t\t _  _  _       _                             
# \t\t\t\t\t| || || |     | |                          _         
# \t\t\t\t\t| || || | ____| | ____ ___  ____   ____   | |_  ___                                                               ||
# \t\t\t\t\t| ||_|| |/ _  ) |/ ___) _ \|    \ / _  )  |  _)/ _ \                                                              ||
# \t\t\t\t\t| |___| ( (/ /| ( (__| |_| | | | ( (/ /   | |_| |_| |                                                             ||
# \t\t\t\t\t \______|\____)_|\____)___/|_|_|_|\____)   \___)___/ \n                                                           ||
# \t\t\t    _   _   _ ____  ____    _____                           _____    ___     ____                           _____     ||
# \t\t\t   / \ | | | |  _ \|  _ \  | ____|_ __   ___ _ __ _   _ _ _|_   _|  ( _ )   |  _ \  ___  ___ _ __ _   _ _ _|_   _| 
# \t\t\t  / _ \| | | | |_) | |_) | |  _| | '_ \ / __| '__| | | | '_ \| |    / _ \/\ | | | |/ _ \/ __| '__| | | | '_ \| |   
# \t\t\t / ___ \ |_| |  __/|  __/  | |___| | | | (__| |  | |_| | |_) | |   | (_>  < | |_| |  __/ (__| |  | |_| | |_) | |   
# \t\t\t/_/   \_\___/|_|   |_|     |_____|_| |_|\___|_|   \__, | .__/|_|    \___/\/ |____/ \___|\___|_|   \__, | .__/|_|    
# \t\t\t                                                  |___/|_|                                        |___/|_|                                                                                                            
# \t\t\t\t\t\t\t\t\t\t\t\t __  __            _     _            
# \t\t\t\t\t\t\t\t\t\t\t\t|  \/  | __ _  ___| |__ (_)_ __   ___  
# \t\t\t\t\t\t\t\t\t\t\t\t| |\/| |/ _` |/ __| '_ \| | '_ \ / _ '
# \t\t\t\t\t\t\t\t\t\t\t\t| |  | | (_| | (__| | | | | | | |  __/
# \t\t\t\t\t\t\t\t\t\t\t\t|_|  |_|\__,_|\___|_| |_|_|_| |_|\___|    
# ||
# ================================================================%$# 🌹🌷🌻   
                                                          
# \n\n                 

#      🌻 Instruction 🌼
# =============================
# ~ Our App Made Just For You ~
# =============================

# 🌷 There are 2 main functions of our app:
#     e : Encript your text message 🔐 
#     d : Decript your text message 🗝️
    
#  ''')
    
# # function to clear screen after finish 1 round of the game
# def clear_screen():
#     # ref to get this function: https://www.geeksforgeeks.org/clear-screen-python/
#     # Get the operating system
#     operating_system = platform.system()
#     # Clear screen based on the operating system
#     if operating_system == 'Linux':
#         os.system('clear')  # For Linux
#     elif operating_system == 'Windows':
#         os.system('cls')   # For Windows
#     else:
#         print("Unsupported operating system: {}".format(operating_system))


# def get_user_input():
#     # Function to get user input
#     print("\nSelect an option:")
#     print("\tE. Encrypt")
#     print("\tD. Decrypt")
#     user_option = input("Enter your choice (E/D): ").lower()

#     user_data = input("Enter data: ")
#     user_shift_count = str.isdigit(input("Enter shift count: "))

#     if user_shift_count > 25 or user_shift_count < 0:
#         raise ValueError("Data length must be between 1 and 25 characters.")

#     return user_option, user_data, user_shift_count


# def perform_cryptography(user_option, user_data, user_shift_count):
#     # Function to perform encryption or decryption based on user's option
#     result = caesar(user_data.lower(), user_shift_count, user_option)
#     return result


# def main():
#     while True:
#         welcoming_screen()

#         try:
#             user_option, user_data, user_shift_count = get_user_input()

#             if user_option == 'e':
#                 result = perform_cryptography(
#                     user_option, user_data, user_shift_count)
#                 print("Encrypted Result:", result)
#             elif user_option == 'd':
#                 decrypted_result = perform_cryptography(
#                     user_option, user_data, user_shift_count)
#                 print("Decrypted Result:", decrypted_result)
#             else:
#                 print("Invalid option. Please choose 'E' for encrypt or 'D' for decrypt.")

#         except ValueError as ve:
#             print(f"Error: {ve}")
#         except Exception as e:
#             print(f"Unexpected error: {e}")

#         continue_option = input("Do you want to continue? (y/n): ")
#         if continue_option.lower() != 'y':
#             print("Exiting the program. Goodbye!")
#             break
#         clear_screen()


# # This line mean if the current file name main, then run the main() function
# if __name__ == "__main__":
#     main()
        

    

