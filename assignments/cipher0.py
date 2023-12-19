# Cipher Assignment 

import os

os.getcwd()
os.chdir("/Users/nuryavuz/Desktop/INST126/assignments")
os.getcwd()

#map 

#create variables and key while adding space for input
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#successfuly create a function with working arguments
def cipher(text,shift):
    text= text.lower()
    altered_text = ""
    for char in text:
        if char.islower():
            altered_text += chr((ord(char) + shift - 97) % 26 + 97) #shift by 3 here 
        else:
            altered_text += char
        return altered_text
    print(altered_text)

text = input('Enter a phrase to cipher: ')
n = int(input("How many letters should the cipher shift by?: "))

cipher(text,n)


