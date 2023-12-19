#iteration and iterators

counter = 0 
while counter < 10:
    print("We're in a loop!")
    print(counter)
    counter += 1 

while True:   #runs forever, stop with control c 
    print(counter)
    counter += 1


counter = 0
while True:
    print(counter)
    counter += 1
    if counter > 1000:
        break


counter = 1 
while counter < 10:
    print("here's loop number {}".format(counter))
   

numlist[1, 2, 3, 4, 5]
for number in numlist:
    print(number)

    
char_list = ["a", "b", "c", "d", "e"] #print all values in the list 
for char in char_list:
    print(char)

for idx in range(10):  #prints 10 different values but doesnt get up to ten and starts at 0
    print(idx)

#range and lists are iterators

#list indexing lst[2] = ["a", "b", "c"] would take value c 

#slice lst[0:3] = ["a", "b", "c" , "d"] takes a b and c because its only taking three values 
# lst[2:3] = ["a", "b", "c" , "d"] takes c 

char_list = ["a", "b", "c", "d", "e"]
char_list[3] #after the third position is d 
char_list[3:5] #works bc it looks at the space between the numebrs, not after
char_list[5] #error, no number past 5th spot 

for idx in range(5):
    print(char_list[idx])

###############
fruits = ["apple", "pear", "banana", "peach"]
prices = [3.49, 4.19, 1.79, 5.99]

for index in range(len(fruits)):
    print("The price of {} today is ${} per lb.".format(fruits[index], prices[index]))

############
#list methods

example_string = "Here's a STRING"
print(example_string)
print(example_string.lower()) #doesnt change the original value 

#most list methods change the original value

fruits = ["apple", "pear", "banana", "peach"]
print(fruits)
fruits.append("grapes") #adds grapes to string
print(fruits) 

fruits.pop() #gives back value it pops off the last item 
print(fruits) 

while len(fruits) > 0:
    this_fruit = fruits.pop()
    print("We just removed {} from the list of fruits".format(this_fruit))
print(fruits)

