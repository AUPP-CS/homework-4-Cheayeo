# def caesar(text, shift, operation):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     try:
#         # Check if shift is an integer and within the range 0 to 25
#         if not isinstance(shift, int) or shift < 0 or shift > 25:
#             raise ValueError('Invalid shift value. Shift must be an integer between 0 and 25.')

#         # Check if operation is either 'e' or 'd'
#         if operation not in ['e', 'd']:
#             raise ValueError('Invalid operation. Operation must be "e" for encryption or "d" for decryption.')

#         encrypt_text = ''
#         decrypt_text = ''

#         if operation == 'e':
#             for n in text:
#                 if n.isalpha():
#                     shift_index = (alphabet.index(n) + shift) % 26
#                     encrypt_text += alphabet[shift_index]
#                 else:
#                     encrypt_text += n
#             return encrypt_text
#         elif operation == 'd':
#             for n in text:
#                 if n.isalpha():
#                     shift_index = (alphabet.index(n) - shift) % 26
#                     decrypt_text += alphabet[shift_index]
#                 else:
#                     decrypt_text += n
#             return decrypt_text
    
#     except ValueError as e:
#         return str(e)  # Return the error message
