def create_mask(string_to_mask, masking_char = "x"):
    mask = len(string_to_mask) * masking_char
    return mask

#keeps running "syntax error" although return is inside of the function 

#strings

"here's a string".capitalize()
"another string".count("t")

new_list = [1, 2, 3, 4, 10]
another_list = [10, 4, 2, 3, 1]

another_list.sort()
print(another_list)

yet_another_list = [6, 3, 67, 1]
sorted(yet_another_list)
print(yet_another_list)

yet_another_list.sort()
print(yet_another_list)

#.sort forever changes the list

print(yet_another_list)
