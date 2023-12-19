# checklist review 

# sample: masking function 

def create_mask(string_to_mask, mask_char = "*"):
    mask_length = len(string_to_mask)
    mask = mask_char * mask_length 
    return mask 

# test cases (commented so it doesnt run with the rest of the code)
#print(create_mask("password"))
#print(create_mask("p"))
#print(create_mask("password", "#"))
#print(create_mask("password", 3 )) # does not work, multiples the length of characters times the number (8x3)

def create_mask(string_to_mask, mask_char = "*"):
    """
    This function takes a string and an optimal character, it givses you back 
    a repetition of the character with the same length as the initial string.
    Default character is "*"
    """
    #this ^ docustring shows up every time you use the function
 # look up how to convert to string (commented code doesn't work )
   # if mask_char is int:
   # mask_char = str(mask_char)
    mask_length = len(string_to_mask)
    mask = mask_char * mask_length 
    return mask 



# when you save a function or a py file, in the same working directory, you can import it and use it there. 
# in that file mask_script, the code would look like
# masking.py would be the other file name

# import masking
# from masking import create_mask
# create_mask("pass", "&")

if __name__ == "__main__":
    # test cases
    print(create_mask("password"))
    print(create_mask("p"))
    print(create_mask("password", "#"))
    print(create_mask("password", 3 ))
    
# if you run "python masking.py" at the command line, it prints the test cases


########

# user input 

phrase_to_mask = input("Type in a phrase you want to mask: ")
masking_char = input("Type in the character you rwant to use as a mask:  ")

create_mask(phrase_to_mask, masking_char)

# run file in command line and fill in the answers 

#sysargv is for entering additional arguments at the command line

import sys 

try:
    phrase_to_mask = sys.argv[1] #returns an error if it doesn't get sys.argv[1]
except IndexError:
    phrase_to_mask = input("Type in a phrase you want to mask: ")


try:
    masking_char = sys.argv[2]
except IndexError:
    masking_char = input("Type in the character you rwant to use as a mask:  ")

# run "python mask_script.py \&" at the command line 
# when you enter &&& it keeps asking you for the input 

print(create_mask(phrase_to_mask,masking_char))

import pandas
import numpy
import matplotlib 




