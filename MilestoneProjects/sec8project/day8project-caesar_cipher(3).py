alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        plain_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift
                plain_text += alphabet[new_position]
            else:
                plain_text += letter
        print(f"The decoded text is {plain_text}")
    else:
        print("Wrong choice.")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift', and 'direction' values.
caesar(text, shift, direction)
