#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = float(input("What % would you like to tip? "))
ppl = int(input("How many people to split the bill? "))

total = bill / ppl * (tip / 100 + 1)
total = "{:.2f}".format(total)
print("Each person should pay: " + str(total))

input("Press anything to exit the program.\n")