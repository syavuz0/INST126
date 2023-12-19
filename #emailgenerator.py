#email greeting generator 

greeting = "Hello "
message = "Unfortunately we cannot offer you a position at..." 
format = ",\n\n"

#new with variables
print(greeting + "Mahmoud" + format + message)
print(greeting + "Maria" + format + message)
print(greeting + "Mark" + format + message)

#with a function
def write_email(newgreeting, name, newmessage): 
    print(newgreeting + name + ",\n" + newmessage)

write_email("Hey ", "Amanda", "How are you?")

    


#original 
print("Dear " + "Mahmoud" + ",\n" + "We regret to inform you...")
print("Dear " + "Maria" + ",\n" + "We regret to inform you...")
print("Dear " + "Mark" + ",\n" + "We regret to inform you...")

