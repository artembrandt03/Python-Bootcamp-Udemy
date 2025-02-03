#Write your code below this line 👇
# def prime_checker(number):
#     if (not number%2==0) and (not number%3==0) and (not number%5==0) and (not number%7==0) and (not number%9==0):
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

#teacher solution
def prime_checker(number):
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#is the better approach for checking prime numbers because it covers all possible divisors within a specified range and is a more reliable method for prime number determination.

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

input("Press anything to exit the program.\n")