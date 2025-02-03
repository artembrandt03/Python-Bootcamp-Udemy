# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
score1 = 0
score2 = 0
name1 = name1.lower()
name2 = name2.lower()

score1 += name1.count("t") + name2.count("t") + name1.count("r") + name2.count("r")
score1 += name1.count("u") + name2.count("u") + name1.count("e") + name2.count("e")
score2 += name1.count("l") + name2.count("l") + name1.count("o") + name2.count("o")
score2 += name1.count("v") + name2.count("v") + name1.count("e") + name2.count("e")

result = int(str(score1) + str(score2))

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif 40 <= result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")


input("Press anything to exit the program.\n")