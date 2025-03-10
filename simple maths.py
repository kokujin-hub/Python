"""This program will ask the user for their name and favourite numbers
and then perform some simple maths on the numbers"""

# Ask the user for their name and favourite number
q = input('What is your name? ')
num1 = int(input('What is your favourite number? '))
num2 = int(input('What is your second favourite number '))

#do the math
addition = num1 + num2
multiply = num1 * num2

#printing result
print(f'Hello my friend{q}')
print(f'here is the calculation of your favourite numbers')
print(f'{num1} + {num2} = {addition}')
print(f'{num1} * {num2} = {multiply}')
