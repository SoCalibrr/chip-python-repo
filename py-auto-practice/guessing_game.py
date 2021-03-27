# This is a guess the number game.
import random
secret_number = random.randint(1, 50)
print('I am thinking of a number between 1 and 50')

# Ask the player to guess 6 times.
for guesses_taken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too LOW my love.')
    elif guess > secret_number:
        print('Your guess is too HIGH my flower.')
    else: 
        break # This condition is the correct guess

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses! I guess you are smart my baby ;)')
else:
    print('Dangggg. I thought you were smart. The number I was thinking of was ' + str(secret_number) + '.')