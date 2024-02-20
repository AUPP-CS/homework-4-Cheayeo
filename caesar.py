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
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            start = ord('A') if char.isupper() else ord('a')  # Set the starting ASCII value based on case
            result_txt += chr((ord(char) - start + shift * direction) % 26 + start)
        else:
            result_txt += char  # If it's not an alphabet letter, keep it unchanged
    return result_txt
def caesar_decrypt(text, shift):
    return caesar(text, shift, -1)
