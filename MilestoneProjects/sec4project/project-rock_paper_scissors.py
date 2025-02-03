rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]

print("Welcome to 'Rock Paper Scissors' game! \nYou're going to be battling againts computer!")
choice = int(input("Choose: \n1 - Rock \n2 - Paper \n3 - Scissors\n"))
import random
computer_choice = int(random.randint(1,3))

print(f"You chose: \n{options[choice - 1]}")
print(f"Computer chose: \n{options[computer_choice - 1]}")
if choice > 3 or choice < 1:
    print("You typed in the wrong choice!")
else:
    if choice == 1 and computer_choice == 1:
        print("It's a draw!")
    elif choice == 1 and computer_choice == 2:
        print("You lost!")
    elif choice == 1 and computer_choice == 3:
        print("You won!")
    elif choice == 2 and computer_choice == 1:
        print("You won!")
    elif choice == 2 and computer_choice == 2:
        print("It's a draw!")
    elif choice == 2 and computer_choice == 3:
        print("You lost!")
    elif choice == 3 and computer_choice == 1:
        print("You lost!")
    elif choice == 3 and computer_choice == 2:
        print("You won!")
    elif choice == 3 and computer_choice == 3:
        print("It's a draw!")

input("Press anything to exit the program.\n")