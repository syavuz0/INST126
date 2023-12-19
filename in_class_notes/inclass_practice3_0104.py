# In-class practice for 09-15-2023
# 1. Import
import os

# 2. Working directory
os.getcwd() #gets the working directory tells you where you are 
os.chdir("desktop") #changes directory 
os.chdir("..") #moves up a folder back to base
########
os.mkdir("embedded_directory") #makes a directory 
os.chdir("embedded_directory")
os.getcwd()
os.chdir("..")
os.getcwd()

# 3. Read text file
with #creates a block that can clean up things for you and the cleaning
with open("sample_text_file2.txt", "r") as textfile:
    sample_text = textfile .read()

print(sample_text) 

type(sample_text) #tells you if its a string or number 
small_i = sample_text.count("i") #character sensitive 
big_i = sample_text.count("i")
small_i + big_i

sample_text.lower().count("i") #converts everything to lowercase and then counts
#lower is a string method 
type(sample_text.lower()) #string
type(sample_text.lower().count("i")) #integer

#format strings 
x = 35
y = 89
z = 95
"The first value is {}, and the second value is {}".format(x,y)
"the age of my middle daughter is {}, and the age of my grandmother is {}".format(x,z)

# 4. Some text methods


# 5. readlines() and sort()
# 5. Install lorem

import os
import lorem 

lorem.paragraph()
lorem.sentence()

#lorem download not working installation failure 


# 6. Write lorem

# for more on strings and .format(), see:
# https://docs.python.org/3/library/string.html


os.getcwd() #gets the working directory tells you where you are 
#os.chdir("") changes directory 
#os.chdir("..") move up a folder

