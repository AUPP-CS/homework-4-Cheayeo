# '''
# The caesar function will be used to encrypt or decrypt user input.

# @parameters:
#     text = string provided as encrypt or decrypt text.
#     shift = number that is use to perform an alphabetically position shift in the list.
#     operation = string letter "e" for encrypt and "d" for decrypt.

# @return:
#     if operation is "e" then the function will return the encrypted text.
#     if operation is "d" then the function will return the decrypted text.
# '''
# num_letters = True
# def caesar(text, shift, operation):    
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
#     # Your code goes here
#     result = ''
#     if operation == 'e':
#         shift = shift
            
#         for character in text:
#             character = character.lower()
#             if not character == "":
#                 index = character.find(character)
#                 if index == -1:
#                     result += character
#                 else:
#                     new_index = index + shift
#                     if new_index >= num_letters:
#                         new_index -= num_letters
#                     elif new_index < 0:
#                         new_index += num_letters
#                     result += character[new_index]
#     elif operation == 'd':
#         shift = shift
#         for character in text:
#             character = character.lower()
#             if not character == "":
#                 index = character.find(character)
#                 if index == -1:
#                     result += character
#                 else:
#                     new_index = index + shift
#                     if new_index >= num_letters:
#                         new_index -= num_letters
#                     elif new_index < 0:
#                         new_index += num_letters
#                     result += character[new_index]
#     else:
#         return 'invalid option'



#try_again#  
# if try_again.lower() != 'yes':
#         print("Thank you for using our tool!")
#         break