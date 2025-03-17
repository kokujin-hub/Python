"""This program will print"""

try:
    while True:
        num = input('Enter a number: ')

        if num == '-':
            break

        num1 = int(num)

        if num1.isdecimal:
            print('boop') 
        for i in num:
            print('beep')
except ValueError:
    print('not robot')



