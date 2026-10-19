# Build a number guessing game — computer picks a random number, user keeps guessing until correct.

import random

n = int(input("Enter the first number of range: "))
m = int(input("Enter the second number of range: "))

com = random.randint(n,m)
tries = 0

while True:
    tries += 1
    hum = int(input("Guess the Number: "))

    if hum == com:
        print(f"Congratulations! you have won the game in {tries} tries.")
        break
    elif hum > com:
        print("Sorry! Wrong Guess, Guess a lower number.")
    elif hum < com:
        print("Sorry! Wrong Guess, Guess a higher number.")

