#Calculator App
import art
print(art.logo)
input("Welcome to the calculator app! Press 'Enter' to begin.")
import os


#Defining section
#Add operation
def add(n1, n2):
    return n1 + n2
#Substract operation
def substract(n1, n2):
    return n1 - n2
#Multiply operation
def multiply(n1, n2):
    return n1 * n2
#Divide operation
def divide(n1, n2):
    return n1 / n2
#Clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Main Part
clear()
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
keep_going = True
previous_result = 0

while keep_going:
    if previous_result != 0:
        print(f"Previous result: {previous_result}")
    num1 = float(input("What's the first number?: "))
    for sign in operations:
        print(sign)
    operation_sign = input("Pick an operation from the ones above: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operation_sign](num1, num2)
    previous_result = answer
    clear()
    print(f"{num1} {operation_sign} {num2} = {answer}")

    still_calculating = (input("Do you want to keep calculationg?\nType 'y' for yes or 'n' for no.\n"))
    if still_calculating == 'n':
        keep_going = False
    clear()