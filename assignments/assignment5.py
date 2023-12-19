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

count_word_message = input("Pick a word you'd like me to count the occurrences of.")

count_word = read.lower().count(count_word_message.lower)
print("{} has the word {} times".format(path_to_file, count_word))


#wants program to continue asking for a foler name until a good path is entered
#after three incorrect tries, wants program to tell me a string that i can type to wuit the program
#wants to keep trying to enter a path if chosen

import os
os.getcwd()
os.chdir("/Users/nuryavuz/Desktop/INST126/word_search/word_search_expanded")
os.getcwd()


#use while and for loops #assignment 5 section

keep_searching = True
failure_count = 0

while keep_searching:

    try:
        path_to_file = input("Please input a file to read.")
        os.listdir(print("these are your options"))
        count_word_message = input("Pick a word you'd like me to count the occurrences of.")
        failure_count = 0
        print("{} has the word {} times".format(path_to_file, count_word))
    except:
        path_to_file = input("Please pick a different value, I don't know what you're looking for. ")
        failure_count += 1
        if failure_count > 3:
            raise NameError("You are out of tries, exiting the program.")
            keep_searching = False 
        



