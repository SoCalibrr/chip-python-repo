import random
secret_number = random.randint(1, 100)
print('I am thinking of a number between 1 and 100..')

for guesses_taken in range(1,7):
    print('Take a guess :)')
    guess = int(input())

    if guess > secret_number:
        print('Sorry, too high.')
    elif guess < secret_number:
        print('Sorry, too low.')
    else:
        break # this means that the secret number was guessed correctly

if guess == secret_number:
    print('Look at you...smart ass ;)')
else:
    print('A lil slow, are we?')