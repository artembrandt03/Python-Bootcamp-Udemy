#setup
import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

import art 
print(art.logo)
print(f"Welcome to the blind auction program!")
input("Press 'Enter' to start.")
clear()
print(f"Do you want to: \n1.Choose an item for the auction yourself? \n2.Choose the random one?")
choice = input("Type '1' or '2': ")
auction_item = ""
if choice == '1':
    auction_item = input("What is an item for the auction? ")
elif choice == '2':
    auction_item = random.choice(art.auction_items)
clear()


#beginning

bidders = {}
bidding_done = False

while not bidding_done:
    print(f"Today's auction item: {auction_item}")
    name = input(f"What is your name? ")
    bid = int(input(f"What is your bid? $"))
    bidders[name] = bid

    more_bidders = input(f"Are there any other users who want to bid?\nType 'yes' or 'no'. ")
    if more_bidders == "yes":
        clear()
    elif more_bidders == "no":
        bidding_done = True
clear()

highest_bid = 0
highest_bidder = ""
for bidder in bidders:
    bid_amount = bidders[bidder]

    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder

print(f"And {auction_item} goes to...")
input("(Press 'Enter' to continue)")
print(f"{highest_bidder}, who was the highest bidder, with a bid of {highest_bid}! Congratulations. ")
input("Press 'Enter' to exit the program.")