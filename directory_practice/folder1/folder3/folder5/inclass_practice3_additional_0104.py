# In-class practice for 09-18-2023
# 1. File reading and writing
# 2. More directory practice
#    getcwd()
#    chdir()
#    listdir() 
#
# 3. User input with input()
# 4. Format strings

# what module do you need for working with directories, and how do you load it?

# reminder of how to open a file, read the contents, and either:
#   - print the contents, or
#   - assign the contents to a variable



# download directory_practice.zip, unzip it
# figure out how to get your working directory to "folder5"
# try reading and printing the contents of each file in each folder (1 through 10),
# with folder 5 as your starting place, aka working directory.

import os
os.getcwd()

with open("file5.txt","r") as file5connection:
    print(file5connection.read())
    file5 = file5connection.read()

# new string method: join()
# usage:  "joining string".join(["list", "to", "join"])
# make a new string using join() to separate each with a new line

" ".join(["here", "is", "a", "longer", "string"]) #better solution
"something".join(["here", "is", "a", "longer", "string"]) #run to see why we leave the space empty

"here " + "is " + "another " + "string" #old version, have to manually put all spaces there for readability

# write your joined string out to a new file
# same as reading, but with the "w" mode in the open() function (for "write")

write_output = " ".join(["here", "is", "a", "really", "dumb", "string"])
print(write_output) #checking work

# make a new string, and write that to the same file
# what happened?

with open("dumb_string.txt", "w") as writeout: #writeout is the name of the connection object
    writeout.write(write_output)
    writeout.write(" this did not over-write!")

# "w" deletes the old text and replaces it
# "a" adds on to the preexisting code

#writeout.write("another thing") #error because its after the with block 

########################

#directory practice
# read the contents of file 8 

os.getcwd()

with open("folder8/file8.txt", "r") as readnew:
    print(readnew.read())
    file8 = readnew.read()


with open("folder7/folder10/file10.txt") as readagain: 
    print(readagain.read())
    fil10 = readagain.read()

#can use the folder/7/blah because they are within folder five and python can see it

# make another new string, use "a" to "append" to the same file
# what happened?





