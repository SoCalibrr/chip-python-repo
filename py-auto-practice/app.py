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
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[2:])


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # print(matrix[0][1:])
# for row in matrix:      # Selects the first row, or list, in the matrix
#     for item in row:    # For each value in the list
#         print(item ** 2)



# # List Methods/Functions
# numbers = [5, 2, 1, 7, 4]
# numbers.append(20)      # append 20 to the end of the list
# print(numbers)
# numbers.insert(2, 10)   # insert 10 at the 2nd index of list
# print(numbers)
# numbers.remove(5)       # Removes specific objects/value from list
# print(numbers)
# numbers.clear()         # Removes all items from list
# print(numbers)
# numbers = [5, 2, 1, 7, 4]
# numbers.pop()           # Removes last item from a list
# print(numbers)
# print(numbers.index(5)) # Check for the 1st existence of an item in list

# print(2 in numbers)     # Check for the existence of charachers 
# print(50 in numbers)    # or a sequence of characters in a list.
# print(numbers.count(5)) # Count the number of occurences
# numbers.sort()          # Sorts list
# print(numbers)
# numbers.reverse()       # Sorts list in reverse/descending order
# print(numbers)

# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)
# numbers2.append(24)
# print(numbers2)


# chips_list = ['chip', 'josh', 'alycia', 'netta', 'alycia', 'alycia', 'chip', 'alycia']
# uniques = []
# for name in chips_list:
#     if name not in uniques:
#         uniques.append(name)
# print(chips_list)
# print(uniques)


# Tuples (Immutable: Like lists that can't be changed.)
# Defined by parenthesis (), 
# Can only get info about a tuple, can't change it
# You'll mainly use lists, but if you need to create a list 
# that no one can change, use a tuple.
numbers = (1, 2, 3)


# Unpacking
coordinates = [1, 2, 3]
# coordinates[0] * ccordinates[1] * coordinates[2]
# or 
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# Unpaacking is more efficient
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)


# # Random script: Trying to figure out how to create a string of 10 random numbers.
# # NOT QUITE THERE YET :()
# import random
# random_numbers = random.randint(0, 10)
# number_list = []
# # tell_me_your_name = input("Please tell me your name: ")
# for i in str(random_numbers):
#     while len(number_list) < 10:
#         number_list += i
#         continue
# print(number_list)



# Dictionaries
# Can be used to store key:value pairs (defined with {})
# customer = {
#     "name": "Chipper Wilson",
#     "age": 30,
#     "is_verifed": True
# }
# print(customer["name"])
# print(customer.get("birthdate", "Dec 31 1999"))
# customer["name"] = "Alycia Casey"
# print(customer["name"])


# Challenge
# phone = input("Phone: ")
# digits = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }
# output = ""
# for num in phone:
#     output += digits.get(num, "! ") + " "   # print the value of the provided key. 
#                                             # Print "!" if the key/vlaue is unknown.
# print(output)


# # Emoji Converter
# message = input("> ")
# # words = message.split(' ')      # Anywhere in string the space (' ') character is found will be used as boundary
#                                 # to separate string into multiple words and then returns a list.
# emojis = {
#     ":)": "😀",
#     ":(": "🙁",
#     ";)": "😉"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "  # (item that we're seraching our "emojis" dictionary for, 
# print(output)                               # default output if that "word" isn't found) 


# def say_hello():
#     print('Hi there!')
#     print('Welcome aboard!')

#     # Best practice is to put two line breaks after you define function.
# print('Start:')
# say_hello()
# print('Finish:')


# # Functions
# def say_hello(name):
#     print(f"Hi there {name}!")
#     print("Welcome aboard!")
#     # parameter = (name)
#     # arguement = "Calvin"
# say_hello("Calvin")
# say_hello("Alycia")


# # Returns
# def square(number):
#     return number * number


# result = square(3)
# print(result)


# # Putting our emoji converter inside of a function
# def emoji_converter(message):
#     words = message.split(' ')      
#     emojis = {
#         ":)": "😀",
#         ":(": "🙁",
#         ";)": "😉"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input("> ")
# print(emoji_converter(message))


# # Handling Exceptions (Try/Except) 
# # Exception = Kind of error that crashes our program
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('You cant divide a number by zero silly :)')    
# except ValueError:
#     print('Invalid Value')


# Use comments to explain whys an hows, not whats


# Classes are used to define new types
# Simple types in Python (Numbers, strings, booleans)
# A few Complex types in Python (Lists, Dictionaries)
# Classes can define new types to model real concepts

# class Point:     # Pascal Naming Convention (used for naming classes is diff. No underscores. Cap first letter of each word)
#     def move(self):     # You can define your own functions and methods in your class.
#         print("move")
    
#     def draw(self):
#         print("draw")


# # with this class, we've defined a new type
# # with this type we can create new objects
# # An object is an instance of a class
# # A class defines a template for creating objects
# # objects are the actual instances based on that blueprint
# # to create an object:

# point1 = Point()
# point1.draw()
# Point().draw()

# class Point:   
#     def __init__(self, x, y, z):  # This is a constructor and is used to construct, or create, an object.
#         self.x = x
#         self.y = y
#         self.z = z

#     def move(self):     
#         print("move")
    
#     def draw(self):
#         print("draw")


# new_point = Point(5, 10, 20)
# print(new_point.x)
# print(new_point.y)
# print(new_point.z)


# # Project:
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, I am {self.name}.")

# calvin = Person("Calvin")
# # print(calvin.name)
# calvin.talk()

# alycia = Person("Alycia")
# alycia.talk()


# # Inheritance
# # Before:
# class Dog:
#     def walk(self):
#         print("walk")

# class Cat:
#     def walk(self):
#         print("walk")

# # After:
# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):  # The Dog class will inheriate all of the methods defined in the Mammal class.
#     pass            # Pass = there's nothing to see here. This class doesn't have any new info.


# class Cat:
#     pass


# dog1 = Dog()
# dog1.walk()

