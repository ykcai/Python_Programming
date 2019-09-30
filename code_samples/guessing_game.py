# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
import random

target = random.randint(1, 100)

guesses = [0]
# Keep track of all your guesses

print("Input your guess below...")

while True:
    try:
        guess = int(input("What is your guess? "))
    except ValueError:
        print("Sorry, I don't understand that.")
        continue
    else:
        print(guess)
        
        if guess < 1 or guess > 100:
            print("OUT OF BOUNDS!!! Please try again: ")
            continue

        # here we compare the player's guess to our number
        if guess == target:
            print(f'CONGRATZ, you guessed it in {len(guesses)} tries')
            break

        # if guess is incorrect, add guess to the list
        guesses.append(guess)

        # when testing our first guess, guesses[-2] == 0
        # this brings us to the first guess

        # for cases after first guess
        if guesses[-2]:
            if abs(target-guess) < abs(target-guesses[-2]):
                print('WARMER!')
            else:
                print('COLDER!')

        # for first guess case
        else:
            if abs(target-guess) <= 10:
                print('WARM!')
            else:
                print('COLD!')
