#Hangman Game final code by Artem Brandt

#Part 1 - Imports
import random
import hangman_words
import hangman_art
import os

#Part 2 - Setup
word_list = hangman_words.words_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
endgame = False
lives = 6
wrong_letter = []

display = [] #creating a display to see which letters have been guessed
for _ in range(word_length):
    display += "_"

#Part 3 - Beginning
print(hangman_art.logo)
print("Welcome to the Hangman Game! Have fun!")
input("Press anything to begin\n")
os.system("cls" if os.name == "nt" else "clear")
print(f"The word is: {' '.join(display)}")

#Part 4 - Main game loop
while not endgame:
    print(f"Wrong letters so far: {' '.join(wrong_letter)}")
    guess = input("Guess a letter: ") #getting an input letter
    guess.lower()
    os.system("cls" if os.name == "nt" else "clear")
    if guess in display:
        print("This letter is already guessed")

    for position in range(word_length): #Check guessed letter
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:  #Check if user is wrong.
        print(f"Letter '{guess}' is not in the word")
        wrong_letter.append(guess)
        lives -= 1
        print(f"Lives left: {lives}")
        if lives == 0:
            endgame = True
            print("You lose! Better luck next time.")
            print(f"The word was: {chosen_word}")


    print(f"{' '.join(display)}") #Join all the elements in the list and turn it into a String.

    if "_" not in display:  #Check if user has got all letters.
        endgame = True
        print("You win! Congratulations.")

    print(hangman_art.stages[lives])
input("Press anything to exit the program.\n")