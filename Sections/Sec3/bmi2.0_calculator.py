# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height ** 2)

if bmi >= 35:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
elif bmi >= 30:
    print(f"Your BMI is {round(bmi)}, you are obese.")
elif bmi >= 25:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
else:
    print(f"Your BMI is {round(bmi)}, you are underweight.")

input("Press anything to exit the program.\n")