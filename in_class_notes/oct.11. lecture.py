#see how to use the sys.argv list by running at command line

import sys 

for sysarg in range(len(sys.argv)):
    print(f"sys.argv[{sysarg}]): {sys.argv[sysarg]}")

# dictionaries and tuples
some_value = 23
heres_a_list = [1, 3, 5, "somthing", some_value]
#normal lists have methods, and are mutable

heres_a_list.pop()
print(heres_a_list)

# potential surprise with mutability
first_list = [1, 5, 10, "coffee"]
second_list = first_list # this just gives an extra name to the same list 


second_list[3] = "tea"
first_list # also changed!

first_list = [1, 5, 10, "coffee"]
better_second_list = first_list.copy()
better_second_list[3] = "tea"
print(better_second_list)
print(first_list)

# tuples similar to lists, but immutable

heres_a_tuple = (1, 2,67, "something")
# can grab values but can't change them 
heres_a_tuple[2]

heres_a_list[2] = 87 # can assign it a new value/ change values in the list 
heres_a_list

heres_a_tuple[2] = 87 # error message says object doesnt not support item assignment 

# use a tuple if you ant a function that gives you back two things
def tuple_function(x, y):
    x_plus5 = x + 5 
    new_y = x_plus5 * y 
    return x_plus5, new_y

tuple_result = tuple_function(3,5)
type(tuple_result)
print(tuple_result)

# iteration works for tuples
for number in (2, 59, 87):
    print(number)

# dictionaries are key: value pairs 
fruits = ["apple", "banana", "pear"]
prices = [3.19, 1.79, 4.19]

fruit_prices = {"apple" : 3.19,
                "banana" : 1.79,
                "pear": 4.19}      #curly braces are dictionaries, demonstrates key value pair, can't have duplicates

fruit_prices["apple"]

print(fruit_prices.get("peach")) # if theres a value that isn't in the list and you dont want program to crash, returns NONE

fruit_prices["peach"] = 8.99 # added this value to fruit prices tuple
print(fruit_prices)

fruit_prices.keys()
fruit_prices.values()

# tuple can be a key, but a list cant 

#iterating over dictionaries 
for fruit, price in fruit_prices.items(): # fruit, price is implicitly a tuple, .items iterates both at the same time
    print(f"The price of {fruit} is ${price} today.")


for key, value in fruit_prices.items():
    print(f"The price of {key} is ${value} today.")