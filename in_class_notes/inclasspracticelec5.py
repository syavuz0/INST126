#while

number = 100

while number <= 150:
    print("now we're on a number {}".format(number))
    number += 1 


#for loop start at 100 end at 150
num_list = [100, 101, 102, 103, 104, 105]
for num in num_list:                           #assigns a value from numlist to num every time it loops down every item in the list 
    print("now we're on number {}".format(num))

#with range() if you don't have a list 
for num2 in range(6): #starts counting from zero 
    num_to_print = num2 + 100 
    print("now we're on number {}".format(num_to_print))

for num3 in range(100,106): #counts the range but does not take the last number, is not inclusive 
    print("now we're on number {}".format(num3))



#os.path.exists()
import os
os.getcwd()
files = os.listdir()
type(files)

os.path.exists("holy_grail.txt") #returns true if it finds the path or a file 

#read file

with open("sample_text_file2.txt") as file_connection:
    all_text = file_connection.read()

with open("sample_text_file2.txt") as file_connection: #new way of reading file, dumps line into a list 
    text_as_list = file_connection.readlines() #readline with no s reads one line 

type(text_as_list)
print(text_as_list[0:6]) #grabs all lines between 0 and 6 (gives us 5 lines)

for line in text_as_list[0:1]:               #grabs specific lines and prints them 
    print("this line is: {}".format(line))

with open("sample_text_file2.txt") as file_connection: #runs all the lines, no limitations
    for line in file_connection:
        print("this line is: {}".format(line))

with open("sample_text_file2.txt") as file_connection:
    counter = 0
    while counter < 3:
        line_of_text = file_connection.readline()
        print(line_of_text)
        counter += 1


with open("sample_text_file2.txt") as file_connection:
    while True:
        line_of_text = file_connection.readline()
        print(line_of_text)
        if line_of_text.casefold().count("I") > 0:  #casefold makes it lowercase
            break
        
#loop through holy_grail.txt
# if the line has the word "grail" in it, print the line and the line number



#file connection as iterator 