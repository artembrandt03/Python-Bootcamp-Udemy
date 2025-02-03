#Caesar Cypher Project - final code by Artem Brandt

#Part 1 - Preliminaries
import os

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
previous_shift = None

#Part 2 - Defining function
def loading():
    for number in range (0, 501, 5):
        percentage = round(number*2/10)
        print(f"LOADING {percentage}%")
        os.system("cls" if os.name == "nt" else "clear")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char.isalnum():  # Check if the character is an alphabet letter or a number
            shift = shift_amount
            if cipher_direction == "decode":
                shift *= -1
            if char.isalpha():
                position = alphabet.index(char)
                new_position = (position + shift) % len(alphabet)
                end_text += alphabet[new_position]
            else:  # It's a digit
                position = numbers.index(char)
                new_position = (position + shift) % len(numbers)
                end_text += numbers[new_position]
        else:  # If the character is not an alphabet letter or a number (e.g., a space), no change
                end_text += char
    loading()
    print(f"{cipher_direction}d result: {end_text}")

#Part 3 - Program start
loading()
print(logo)
print("This is a program to encode or decode messages using Caesar Cipher.")
info = input("Would you like to know what a Caesar Cipher is?\nChoose 'yes' or 'no'.\n").lower()
if info == "yes":
    os.system("cls" if os.name == "nt" else "clear")
    print("In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques.") 
    print("It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.")
    print("For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.")
    print("")
    input("Press anything to begin the program.\n")
elif info == "no":
    os.system("cls" if os.name == "nt" else "clear")
    input("Press anything to begin the program.\n")
else:
    os.system("cls" if os.name == "nt" else "clear")
    print("Looks like you miss-typed your choice.")
    input("Regardless, press anything to begin the program.\n")

#Part 4 - Main loop
running = True
while running:
    os.system("cls" if os.name == "nt" else "clear")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction not in ("encode", "decode"):
        print("Invalid option. Please enter 'encode' or 'decode'.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        
    text = input("Type your message:\n").lower()

    if previous_shift is None:
        shift = int(input("Type the shift number:\n"))
    elif previous_shift is not None:
        shift = int(input(f"Type the shift number (Previoulsy used shift number: {previous_shift}):\n"))
    previous_shift = shift

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    print("Do you want to run the program again?")
    decision = input("Type 'yes' or 'no'.\n").lower()
    if decision == "yes":
        input("Press anything to restart the program.\n")
    elif decision == "no":
        running = False
    else: 
        input("Invalid option. Exiting program.\n")
        running = False

input("Thank you for using Caesar Cypher! Press anything to exit.\n")