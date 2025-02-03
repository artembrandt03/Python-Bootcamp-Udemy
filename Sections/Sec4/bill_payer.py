# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number = random.randint(0, len(names) -1 )
person_picked = names[number]
print(f"{person_picked} is going to buy the meal today!")

#alternate simple sulution: person_picked = random.choice(names) // picks a random name essentially
input("Press anything to exit the program.\n")