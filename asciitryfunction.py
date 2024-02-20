'''
The caesar function will be used to encrypt or decrypt user input.

@parameters:
    text = string provided as encrypt or decrypt text.
    shift = number that is use to perform an alphabetically position shift in the list.
    operation = string letter "e" for encrypt and "d" for decrypt.

@return:
    if operation is "e" then the function will return the encrypted text.
    if operation is "d" then the function will return the decrypted text.
'''


def caesar(text, shift, direction):
    result_txt = ''
    try:
        if shift > 25 or shift < 0:
            return 'invalid shift'
    except Exception:
        return 'invalid shift'

    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            # Set the starting ASCII value based on case
            start = ord('A') if char.isupper() else ord('a')

            # Determine the shift direction based on user input
            if direction == 'e':
                new_char = chr((ord(char) - start + shift) % 26 + start)
            elif direction == 'd':
                new_char = chr((ord(char) - start - shift) % 26 + start)
            else:
                return "invalid option"

            result_txt += new_char
        else:
            result_txt += char  # If it's not an alphabet letter, keep it unchanged
    return result_txt
