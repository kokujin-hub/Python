#ask for a password

password = input('Enter a password: ').lower()


#see if the password is long enough

while len(password) < 5 :
    print('No, this password is not good enough.')
    password = input('Enter a password: ')
print('Thank you, your password is good enough.')