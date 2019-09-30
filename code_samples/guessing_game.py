# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
import random

target = random.randint(1, 100)

print(target)

guesses = [0]
# Keep track of all your guesses

print("Input your guess below...")

while True:
    guess = int(input("What is your guess? "))
    print(guess)

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS!!! Please try again: ")
        continue

    # here we compare the player's guess to our number
    if guess == target:
        print(f'CONGRATZ, you guessed it in {len(guesses)} tries')
        break
