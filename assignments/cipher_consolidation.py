# Cipher Assignment 

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input("How many letters would you like the alphabet to shift by?: "))
text = input('Enter the text to cipher: ')


def cipher(text, key):
    ciphertext = ""
    for letter in text:
        letter = letter.lower()
        if not letter == "":
            index = letter.find(letter)
            if index == -1:
                cipher += letter
            else:
                new_index = index + key 
     



# user input for shift use masking 

import string 

def cipher(string_to_mask, cipher_shift = alphabet):
    mask = cipher_shift  
    return mask 

phrase_to_cipher= input("Type in a phrase you want to cipher: ")
masking_char = input("How many letters would you like the alphabet to shift by?")

for character in phrase_to_cipher:
    if character in alphabet:
    position = alphabet.find(character) % 26 
    new_position = (position + cipher_shift)
    new_character = alphabet 

#########

#map 

#create variables and key while adding space for input

#successfuly create a function with working arguments

#try and except to catch an error

#if condition for error

#raise error and helpful message 