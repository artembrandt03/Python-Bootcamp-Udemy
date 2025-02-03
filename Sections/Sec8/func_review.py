# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("Hi!")
#   print("How are you?")
#   print("Hope everything is fine!")

# greet()

#function that allows input
# def greet_with_name(name):
#   print(f"Hi {name}!")
#   print(f"How are you {name}?")
#   print(f"Hope everything is fine {name}!")

# greet_with_name("Artem")

#function that allows more than 1 input
def greet_with(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

greet_with("Artem", "Montreal") 
greet_with("Montreal", "Artem")
#positional arguments vs assigning them
greet_with(name="Artem", location="Montreal")
greet_with(location="Montreal", name="Artem")

input("Press anything to exit the program.\n")