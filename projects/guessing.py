# Import the random module
import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Ask the user to guess the number and store it
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess is correct
if guess == number:
    print("You won!")
else:
    print("You lost!")
    print("The number was", number)