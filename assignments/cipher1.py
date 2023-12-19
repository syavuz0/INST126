import sys 

first_char = ord('a')
last_char = ord('z')
char_range = last_char - first_char + 1

def cipher(message,shift):
    result = ""
    for char in message.lower():
        if char.isalpha():   # ensures that the function runs only if the inputed values are in the alphabet
            char_code = ord(char)
            new_code = char_code + shift

            if new_code >  last_char:    # makes it so that the loop shifts back to the beginning
                new_code -= char_range   # of the alphabet instead of keep shifting forward 
            if new_code < first_char:
                new_code += char_range

            new_char = chr(new_code)
            result += new_char
        else: 
            result += char #leaves the characters that are not a part of the alphabet like punctuation

    return result 

#test runs 
# cipher("Hello World", 7)
# cipher("Nevermind", 3)
# cipher("Have a good day!", 2)

user_message = input("Message to cipher: ")
shift_input = int(input("Shift Number: "))

def main():
    try:
        user_message = sys.argv[1]
        shift_input = int(sys.argv[2])
        cipher_text = cipher(user_message, shift_input)
        print(f"Cipher Text: {cipher_text}")

    except IndexError:
        print("Error: Please provide a message and a shift number as command-line arguments.")
    except ValueError:
        print("Error: Shift Number must be an integer.")

if __name__ == "__main__":
    main()

