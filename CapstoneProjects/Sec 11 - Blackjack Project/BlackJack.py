# BlackJack game capstone project - Udemy Bootcamp
# Made by Artem Brandt
# 2025-02-03

# IMPORTS
import os
import random
from colorama import Fore, Back, Style

# STARTUP SCREEN
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

print("\nWelcome to Blackjack!\nPlay against the dealer and get as close to 21 as possible without going over. Good luck!")
input("[Press 'Enter' to begin.]\n")

# SETUP
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [(rank, suit) for suit in suits for rank in ranks]  # Creating a deck of 52 cards
random.shuffle(deck)  # Shuffle the deck

player_hand = []
dealer_hand = []

# HELPER METHODS

# 1) clear() - Clears the terminal screen/console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 2) initial_deal() - Deals 2 cards to the player and dealer
def initial_deal():
    global player_hand, dealer_hand
    print("Let's begin the round!\nBoth player and dealer draw 2 cards.")
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

# 3) print_hand(person) - Prints the hand of a player or dealer
def print_hand(person):
    if person == "player":
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "Your hand:" + Style.RESET_ALL)
        for card in player_hand:
            print(f"{card[0]} of {card[1]}")
    elif person == "dealer":
        print(Back.WHITE + Fore.BLACK + "Dealer's hand:" + Style.RESET_ALL)
        for i, card in enumerate(dealer_hand):
            if i == 0:
                print(f"{card[0]} of {card[1]}")
            else:
                print("[Hidden Card]")

# 4) calculate_score(hand) - Calculates the score of a given hand
def calculate_score(hand):
    score = 0
    ace_count = 0
    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(rank)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

# 5) print_board() - Displays hands and scores
def print_board():
    global player_score, dealer_score
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n------------------------------------------------------------------")
    print_hand("player")
    print(Back.LIGHTRED_EX + Style.BRIGHT + f"Your score: {player_score}" + Style.RESET_ALL)
    print("\n------------------------------------------------------------------")
    print_hand("dealer")
    print(Back.LIGHTRED_EX + Style.BRIGHT + "Dealer's score: ???" + Style.RESET_ALL)
    print("------------------------------------------------------------------\n")

# 6) isInitialBlackjack() - Checks for an initial Blackjack
def isInitialBlackjack():
    global player_score, dealer_score
    if player_score == 21 and dealer_score == 21:
        print("Both you and the dealer hit 21 right away!")
        return "tie"
    elif player_score == 21:
        print("You got Blackjack from the get-go!\nYou win this round!")
        return "player wins"
    return "neither"

# 7) announce_winner(winner) - Announces round result
def announce_winner(winner):
    if winner == "player":
        print("You win this round!")
    elif winner == "dealer":
        print("Dealer wins this round.")
    elif winner == "tie":
        print("It's a tie!")

# 8) player_turn() - Manages player's turn
def player_turn():
    global player_score
    while True:
        clear()
        print_board()
        choice = input("Your turn! Would you like to:\n[1] Hit\n[2] Stand\nInput your choice (number): ")

        if choice == "1":
            card = deck.pop()
            player_hand.append(card)
            print(f"You drew: {card[0]} of {card[1]}")
            input("[Press 'Enter' to continue...]")
            player_score = calculate_score(player_hand)

            if player_score > 21:
                return "busted"
            elif player_score == 21:
                return "stands"
        elif choice == "2":
            print("You decide to stand.")
            input("[Press 'Enter' to continue...]")
            return "stands"
        else:
            print("Invalid input. Try again.")
            input("[Press 'Enter' to continue...]")

# 9) dealer_turn() - Dealer automatically plays
def dealer_turn():
    global dealer_score
    wants_to_draw = True

    #simulating dealer's decision taking
    score_limit = random.choice([16,17,18])
    if score_limit == 16 and dealer_score <= score_limit:
        print("Dealer decides to play this round cautiously.")
    elif score_limit == 17 and dealer_score <= score_limit:
        print("Dealer plays a balanced strategy for this round.")
    elif score_limit == 18 and dealer_score <= score_limit:
        print("Dealer takes a more aggressive approach this round!")
    elif dealer_score > score_limit:
        print("Dealer decided to stand.")
        input("[Press 'Enter' to continue...]")
        wants_to_draw = False

    while wants_to_draw:
        print("Dealer draws.")
        card = deck.pop()
        dealer_hand.append(card)
        dealer_score = calculate_score(dealer_hand)

        # Post-draw checks
        if dealer_score > 21:
            print("Dealer regrets drawing... they busted!")
            wants_to_draw = False
        elif dealer_score == 21:
            print("Dealer smiles confidently... Blackjack!")
            wants_to_draw = False
        elif dealer_score < score_limit:
            print("Dealer wants to draw again.")
        else:
            print("Dealer decides to stand.")
            wants_to_draw = False
        
        input("[Press 'Enter' to continue...]")

# 10)
def dealers_final_hand():
    print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "Dealer's secret hand revealed:" + Style.RESET_ALL)
    for card in dealer_hand:
        print(f"{card[0]} of {card[1]}")

# MAIN GAME LOOP
while True:
    clear()
    initial_deal()
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print_board()
    first_check = isInitialBlackjack()
    if first_check in ["player wins", "tie"]:
        announce_winner(first_check)
        break

    print("Nobody got a blackjack!\nThe game goes on...")
    input("[Press 'Enter' to continue...]")

    post_turn = player_turn()
    if post_turn == "busted":
        print("\nYou bust! You went over 21.")
        announce_winner("dealer")
        break

    print("\nDealer's turn...")
    dealer_turn()

    # Final results
    print_board()
    if dealer_score > 21:
        print("Dealer busts! You win!")
        announce_winner("player")
    elif dealer_score > player_score:
        announce_winner("dealer")
    elif dealer_score < player_score:
        announce_winner("player")
    else:
        announce_winner("tie")
    
    break  # Ends after one round (can be modified for replayability)
