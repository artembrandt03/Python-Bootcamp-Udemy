import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    letter_found = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            letter_found = True

    # If the guess is not in the chosen_word, reduce 'lives' by 1.
    if not letter_found:
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has guessed all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Check if 'lives' is 0, and end the game if so.
    if lives == 0:
        end_of_game = True
        print("You lose.")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])