# BlackJack game capstone project - Udemy Bootcamp
# Made by Artem Brandt
# 2025-02-03

#IMPORTS
import os
import random
from colorama import Fore, Back, Style

#STARTUP SCREEN
print(r"""
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
""")

print("\nWelcome to Blackjack!\nPlay againts the dealer and get as close to 21 as possible without going over. Good luck!")
input("[Press 'Enter' to begin.]\n")

#SETUP
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [(rank, suit) for suit in suits for rank in ranks] #Creating a deck of 52 cards using a list comprehension
random.shuffle(deck) #Shuffles the deck in place
player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0

#HELPER METHODS
#1)clear() - clears the terminal screen/console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#initial_deal() - deals 2 cards for player and dealer at the beginning of the round
def initial_deal():
    print("Let's begin!\nBoth Player and Dealer draw 2 cards")
    for i in range(4):
        top_card = deck.pop()
        if i < 2:
            player_hand.append(top_card)
        else:
            dealer_hand.append(top_card)  

#2)print_hand(person) - prints the hand of a player or a dealer. if the person is dealer, only their first card in hand is printed
def print_hand(person):
    if person == "player":
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "Your hand:" + Style.RESET_ALL)
        for card in player_hand:
            rank, suit = card  #Unpack the tuple
            print(f"{rank} of {suit}")
    elif person == "dealer":
        print(Back.WHITE + Fore.BLACK + "Dealer's hand:" + Style.RESET_ALL)
        if len(dealer_hand) > 0:
            print(f"{dealer_hand[0][0]} of {dealer_hand[0][1]}")  #Shows only the first card in dealer's hand
            if len(dealer_hand) > 1:
                print("[Hidden Card]")  #Hide the rest of dealer's cards

#3)calculate_score(hand) - calculate's and returns the score based on cards in hand
def calculate_score(hand):
    score = 0
    ace_count = 0 #keeping track in case the person goes over 21
    for card in hand:
        rank, suit = card
        if rank in ['J', 'Q', 'K']:  #Face cards are worth 10 points
            score += 10
        elif rank == 'A':  #Aces are worth 11 initially
            score += 11
            ace_count += 1
        else:  # Numeric cards (2-10)
            score += int(rank)
    #Adjusting the score if it goes over 21
    while score > 21 and ace_count > 0:
        score -= 10  #Now the ace is worth 1 instead of 11
        ace_count -= 1
    return score

#4)print_board() - print's both dealer's and player's hands with some lines around
def print_board():
    print("------------------------------------------------------------------\n")
    print_hand("player")
    print(Back.LIGHTRED_EX + Style.BRIGHT + "Your score:"+ Style.RESET_ALL + f" {player_score}")
    print("\n------------------------------------------------------------------\n")
    print_hand("dealer")
    print(Back.LIGHTRED_EX + Style.BRIGHT + "Dealer's score:"+ Style.RESET_ALL + " ???")
    print("\n------------------------------------------------------------------")

#5)isBlackjack() - compares initial hands after the first draw
def isBlackjack():
    outcome = ""
    if player_score == 21:
        if dealer_score == 21:
            outcome = "tie"
            print("Both you and the dealer hit 21 right away!")
        else:
            outcome = "player wins"
            print("What luck! You get 21 points right away!")
    else:
        outcome = "neither"
    return outcome

#6)announce_winner(winner) - announcing the outcome of the round
def announce_winner(winner):
    if winner == "player":
        print(f"You win the round with the score: {player_score}")
    elif winner == "dealer":
        print(f"Dealer wins the round with the score: {dealer_score}")
    elif winner == "tie":
        print("It's a tie!")

#7)
def player_turn():
    valid_choice = False
    while not valid_choice:
        clear()
        print_board()
        choice = input("Your turn! Would you like to:\n[1]Hit\n[2]Stand\nInput your choice (number):")
        if choice == "1":
            top_card = deck.pop()
            rank, suit = top_card
            print(f"You draw: {rank} of {suit}")
            input("[Press 'Enter' to continue...]\n")
            player_hand.append(top_card)
            valid_choice = True
        elif choice == "2":
            print("You decide to stand.")
            input("[Press 'Enter' to continue...]\n")
            valid_choice = True
        else:
            print("Invalid input. Try again.")
            input("[Press 'Enter' to continue...]\n")



#MAIN GAME
round_on = True
while round_on:
    clear()
    initial_deal()
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print_board()
    first_check = isBlackjack()
    if first_check == "player wins":
        announce_winner("player")
        round_on = False
        break
    elif first_check == "tie":
        announce_winner("tie")
        round_on = False
        break
    else:
        print("The game goes on...")
        input("[Press 'Enter' to continue...]\n")
    
    player_turn()