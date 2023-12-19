# Assignment 3: word search and counting program

#2
import os 
os.getcwd()
os.chdir("/Users/nuryavuz/Desktop/INST126/word_search/")
os.getcwd()

workingdir = "/Users/nuryavuz/Desktop/INST126/word_search/"
os.listdir(workingdir)

#3

with open("text1_folder/pet_shoppe.txt", "r") as file1:
   file1read = file1.read()


#4

file1num = file1read.lower().count("he") #79 times

#5

with open("text2_folder/spam_song.txt", "r") as file2:
   file2read = file2.read()

file2num = file2read.lower().count("he") #16 times

#6
strfile1 = str(file1num)

print("The word 'he' was found " + strfile1 + " times in this file: pet_shoppe.txt")

#i was having a bit trouble trying to conceptualize how I can plug the file name in the FILE value. 


