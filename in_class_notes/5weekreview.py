#in-class review
import os
os.getcwd()
# what if a function gives me an answer, 
# but its seems to be the wrong answer?
# strategy: try something simpler to verify 

"test string".count("t")

word_from_user = "spam"
file_contents = "song about SPAM that says the word spam a lot, spam spam." #should come from with open function reading contents

print(file_contents) #to make sure the right variable is assigned to the right string

file_contents.lower().count(word_from_user)

# working directories
import os 
os.getcwd()
os.listdir("text2_folder")
os.chdir("word_search")

filename = "text2_folder/spam_song.txt"

with open (filename) as file_connection:
    contents = file_connection.read()

folder_to_check = "songs"

os.path.exists(folder_to_check)

for counter in range(1000):
    counter = 782 # works when 781, raises error when at 782
    if counter == 782:
        raise ValueError # forces error to happen

print(counter)

# if statements

x = 7
if x < 5:
    print("x was pretty small") 
elif x > 10:
    print("x was pretty big")
else: 
    print("x was pretty mid")

print("outside the if") # skips the print inside the function and moves on beause its false
# when there isn't an else/elif in the function

#try catch

# Errors (aka exceptions) STOP your program

new_price = 100

if new_price > 20:
    raise ValueError("there's no way that could be so expensive, check your data")

test_string = "heres an actual string with an actual value"
# or 
test_string = None 

try:
    word_count = test_string.count("an")
except AttributeError:
    print("that pesky None value problem popped up, setting word_count to 0")
    word_count = 0
except  ValueError:
    print("this was a Value Error instead")
except FileNotFoundError:
    print("I have no idea how you even got this error")
except TypeError:
    print(" I need to change this to a string")


word_count = test_string.count("an")
print(word_count)

