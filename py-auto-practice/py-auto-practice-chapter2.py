# def great(num1, num2):
#    if num1 > num2:
#        return str(num1) + ' is greater than ' + str(num2)
#    else:
#        return str(num2) + ' is greater than ' + str(num1)
#    
# print(great(25, 100))



# print('What is your name Daddy?')
# name = input()
# if name == 'Chip':
#    print('Hello Chip Daddy. What is your password again?')
#    password = input ()
#    if password == 'swordfish':
#        print('Access Granted')
#    else:
#        print('Nice try chump. Wrong password.')



# while True:
#    print('Who are you?')
#    name = input()
#    if name != 'Joe':
#        continue
#    print('Hello, Joe. What is the password? (It is a fish.)')
#    password = input()
#    if password == 'swordfish':
#        break
# print('Access granted.')



# print('My name is')
# for i in range(5):
#    print('Chipper five times (' + str(i) + ')')



# total = 0 
# for num in range(101):
#    total = total + num
# print (total)



# import random
# for i in range(10):
#    print(random.randint(1, 25))



# import sys

# while True:
#    print('Type exit to exit')
#    response = input()
#    if response == 'exit':
#        sys.exit()
#    print('You typed ' + response + '.')
#    print()



# This is a guess the number game.
#import random
#secret_number = random.randint(1, 50)
#print('I am thinking of a number between 1 and 50')

# Ask the player to guess 6 times.
#for guesses_taken in range(1,7):
#    print('Take a guess.')
#    guess = int(input())

#    if guess < secret_number:
#        print('Your guess is too low homie.')
#    elif guess > secret_number:
#        print('Your guess is too high bro.')
#    else: 
#        break # This condition is the correct guess

# if guess == secret_number:
#    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
# else:
#    print('Nope. The number I was thinking of was ' + str(guess) + '. Sorry :).')



# import random
# import sys
# print('ROCK, PAPER, SCISSORS')

# # These variables keep track of the number of wins, losses and ties.
# wins = 0
# losses = 0
# ties = 0

# while True: # The main game loop.
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True: # The player input loop.
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         player_move = input()
#         if player_move == 'q':
#             sys.exit() # Quit the program.
#         if player_move == 'r' or player_move == 'p' or player_move == 's':
#             break # Break out of the player input loop.
#         print('type one of r, p, s, or q')

#     # Display what the player chose:
#     if player_move == 'r':
#         print('ROCK versus...')
#     elif player_move == 'p':
#         print('PAPER versus...')
#     elif player_move == 's':
#         print('SCISSORS versus...')

#     # Display what the computer chose:
#     randomNumber = random.randint(1,3)
#     if randomNumber == 1:
#         computer_move = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computer_move = 'p'
#         print('PAPER')
#     if randomNumber == 3:
#         computer_move = 's'
#         print('SCISSORS')

#     # Display and record the win/loss/tie:
#     if player_move == computer_move:
#         print('It is a tie!')
#         ties = ties + 1
#     elif player_move == 'r' and computer_move == 's':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'p' and computer_move == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 's' and computer_move == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif player_move == 'r' and computer_move == 'p':
#         print('You lose...')
#         losses = losses + 1
#     elif player_move == 'p' and computer_move == 's':
#         print('You lose...')
#         losses = losses + 1
#     elif player_move == 's' and computer_move == 'r':
#         print('You lose...')
#         losses = losses + 1

#     # End the game
#     if wins == 3 or losses == 3:
#         print('Game Over!!!')
#         break
#     elif ties == 3:
#         print('Looks like we have both met our match today, huh?')
#         break



# import random
# import sys


# while True:
#     print('Lets see who will get spammed baby!')
#     while True:
#         spam = random.randint(0, 2)
#         if spam == 1:
#             print('Hello')
#             break
#         elif spam == 2:
#             print('Howdy')
#             break
#         else: 
#             print('Greetings!')
#             break
#     break


# for i in range(1,11):
#     print(i)

num = 0
while num < 11:
    print(num)
    num = num + 1
   