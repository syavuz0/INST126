#assignment 4 extension 

import os


wd = os.getcwd()
visible_wd = os.listdir()

os.getcwd()
os.chdir("/Users/nuryavuz/Desktop/INST126/word_search/")
os.getcwd()

path_to_file = input("Input a path from your working directory.")

count_word_message = input("What word do you want to count?")

with open(path_to_file) as textfile:
   read = textfile.read()

count_word = read.lower().count(count_word_message.lower)
print("The textfile {} has the word {} times".format(path_to_file, count_word))

#new tests and issues 

if path_to_file != "/Users/nuryavuz/Desktop/INST126/word_search/text1_folder" | "/Users/nuryavuz/Desktop/INST126/word_search/text2_folder":
    raise NameError("The path you chose is not an option, please choose a different one.")


path_to_file = input("Input a path from your working directory.")

try: 
    path_to_file = input()
except:
    path_to_file = "/Users/nuryavuz/Desktop/INST126/word_search/text2_folder"
    print("That is an incorrect value. You have been directed to text2_folder.")


#a way to make the user interface better is if we can input specific subjects for the files instead of having to describe the specific path
# the goal is to have options for the user to pick from instead of a free format answer 

File1 = "/Users/nuryavuz/Desktop/INST126/word_search/text1_folder"
File2 = "/Users/nuryavuz/Desktop/INST126/word_search/text2_folder"

path_to_file = input("Would you like to choose text from foler 1 or folder 2?")
os.chdir(path_to_file)

count_word_message = input("Pick a word you'd like me to count the occurences of.")

count_word = read.lower().count(count_word_message.lower)
print("{} has the word {} times".format(path_to_file, count_word))


