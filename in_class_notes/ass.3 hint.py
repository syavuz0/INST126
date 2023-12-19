#searching for text

pretend_file_input = "Here's\nsome\ntext"
type(pretend_file_input)

pretend_file_input.lower().count("here")

#with open (Path) as somefile:
# path = a full relative directory path
#ex. file.txt # if the file is in your current working directory
# with open ("file.txt") as somefile:
# if its in a lower folder 
# with open ("lower_folder/file.txt")

# if: elsif: else: practice

credit_hours = 15

if credit_hours < 12:
    print("You don't have enough hours to be full time!")
elif credit_hours > 19:
    print("You have too many credits.")
else:
    print("You have a good amount of credits!")


status = "full_time"

if status == "full_time":
    min_hours = 12
else: 
    min_hours = 1

print(min_hours)
#try doing another one where if someone is "overtime" status,
#min_hours is set to 20


#try: catch:
#takes something that normally gives and error and does something else instead
#for any error

credit_hours = "too many"

try: 
    credit_hours < 12
except:
    credit_hours = 0


#different method using isinstance()

credit_hours = "too many"

if not isinstance(credit_hours, int):
    credit_hours = 0
    print("Invalid credit hours data, defaulted to zero")

#slightly specific 
#typeerror is not caught because it is not a nameerror
try: 
    credit_hours < 12
except NameError:
    print("You forgot to assign a value to credit hours.")
    credit_hours = 0

try: 
    credit_hours < 12
except TypeError:
    print("You entered the wrong type of value for credit hours.")
    credit_hours = 0

#example using raise

credit_hours = 100

if credit_hours > 25:
    raise ValueError("The value of credit hours is suspeiciously high... please double check.")

#can use valueerror or exception


#assignment four deals with different inputs 
#handle errors 
#can't read one file, so read the default file 
#goal is to set up an  the error that is informational for useres "try something else" or "exit" 
#use try and except to make that happen
