"""This program will check to see if the user has entered a valid integer
in a specific range of values"""

# Use constants for the low nad high values
LOW = 1
HIGH = 100


# ask user to type in a number
num = input('Please enter an integer: ')

# check to see if the number is valid
if num.lstrip('-').isnumeric(): 
    num = int(num)
    if num < LOW:
        print(f'number {num} is lower than {LOW}')
    elif num > HIGH:
        print(f' number {num} higher than {HIGH}')
    else:
        print(f'Your number is {num}')
else:
    print(f'{num} is not a integer')
    
