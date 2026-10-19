# Create a rock, papers and scissors game

import random
tries = 0 

while True:
    choices = ["rock", "paper", "scissors"]
    com = random.choice(choices)
    tries += 1
    hum = input("Enter between Rock, Paper and Scissors: ").lower()

    if hum not in choices:
        print("Invalid Choice!")
    elif hum == com:
        print("It's a tie!")
        print("computer choosed =",com)
        print("tries =",tries)
    elif (hum == "rock" and com == "scissors") or (hum == "paper" and com == "rock") or (hum == "scissors" and com == "paper"):
        print("You win!")
        print("computer choosed =",com)
        print("tries =",tries)
        break
    else:
        print("Computer wins!")
        print("computer choosed =",com)
        print("tries =",tries)
