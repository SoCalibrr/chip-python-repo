# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(type(age))
# print('You are ' + str(age) + ' years old!')

# weight_in_lbs = input('What is your weight in pounds? ')
# weight_in_kilos = int(weight_in_lbs) / 2.2
# print("You weigh " + str(weight_in_kilos) + " kilograms!")

# if weight_in_kilos >= 75:
#     print('Damn girl!!!')
# else:
#     print('Hmmm. Checks out..scrawny ass..')


# first = 'Calvin'
# last = 'Wilson'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# # formatted sting 
# print(msg)
# cert = 'SSCP'
# birthday = 'May 21st'
# year = 2021
# goal = f'I will pass the {cert} exam by {birthday} {year}.'

# print(goal)

# course = 'Python for Beginners'
# print(len(course))
# # with "upper" method
# # "upper" is a method because it belongs to the string type
# # A function, "len" for example, is similar to a method, 
# # but will work with any type of object (string, int, etc.)
# print(course.upper())
# print(course.lower())

# print(course.replace('Beginners', 'Specialists'))
# print(course.replace('n', 'F'))
# print('Python' in course)

# x = 10
# x = x + 5
# x += 5 # augmented assignment variables
# x -= 5 
# print(x)

# import math

# print(math.floor(3.5))

# Google "python 3 ____ module" to see what a module can do once you import
# and what methods it has

# weather = input('Is it hot or cold outside? ')

# if weather == 'hot' or 'Hot':
#     print("It's a hot day.")
#     print("Drink plenty of water!")
# elif weather == 'cold' or 'Cold':
#     print("It's a cold day.")
#     print("Wear warm clothes!")
# else: 
#     print("I don't know, but it's a lovely day. :)")

# house_price = 1000000
# good_credit = False
# # credit_score = input('What is your credit score? ')
# if good_credit:
#     down_payment = house_price * .1
# else:
#     down_payment = house_price * .2
# print(f"Your down payment will be ${down_payment} dollars.")

# logical operators in python = and, or, and not
# has_high_income = True
# has_good_credit = True

# if has_high_income and not has_good_credit:
#     print('Eligible for loan!')
# else: 
#     print('Nopppppeee :(')


# temp = 31
# if temp > 30:
#     print("It's a hot day.")
# elif temp < 10:
#     print("It's a cold day.")
# else:
#     print("It's neither hot, nor cold.")


# name = 'Chi'
# if len(name) < 3:
#     print('Name must be at least 3 characters.')
# elif len(name) > 50:
#     print('Name can be a maximum of 50 characters.')
# else:
#     print('Name looks good baybee! ;)')

# import random
# name = random.randint(1, 100)
# print(name)
# if name < 3:
#     print('Name must be at least 3 characters.')
# elif name > 50:
#     print('Name can be a maximum of 50 characters.')
# else:
#     print('Name looks good baybee! ;)')


# # Project 1: Weight Converter
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted_weight = weight * .45
#     print(f"You are {converted_weight} kilograms.")
# elif unit.upper() == "K":
#     converted_weight = weight / .45
#     print(f"You are {converted_weight} pounds.")
# else:
#     print('Please enter either "L" or "K".')

# i = 1
# while i <= 5:
#     print('+' * i)
#     i += 1
# print('Done')


## Guessing Game
# import random
# random_number = random.randint(1,3)
# guess_count = 0 
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == random_number:
#         print('You win!')
#         break
# else:
#     print(f'You lose. The number I was thinking of was {random_number}.')

# # "Car Game"
# user_input = input('>')
# help = 'help'
# start = 'start'
# stop = 'stop'
# quit = 'quit'


# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print('Car started...Ready to go!')
#     elif command == "stop":
#         if not started:
#             print('Car is already stopped!')
#         else:
#             started = False
#             print('Car stopped.')
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that...")


# prices = [10, 20, 30, 40, 50]
# total = 0
# for num in prices:
#     total += num
# print(f'Total: {total}')


# # Nested Loops:
# (x, y)
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (2, 0)
# for x in range(4): # Outer Loop
#     for y in range (3): # Inner Loop - Explanation 1:50:00
#         print(f'({x}, {y})')

# # Challenge - Print an 'F'
# numbers = [5, 2, 5, 2, 2]
# x = 'x'
# for letter in x:
#     for num in numbers:
#         print(x * num)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = '' # Resets output to an empty string
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# print('')

# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = '' # Resets output to an empty string
#     for count in range(x_count):
#         output += 'x'
#     print(output)


# # Lists
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:])