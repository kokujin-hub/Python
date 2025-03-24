'''This program will record the unsafe speed'''

#Variables and lists
safe_speed = 10
speedrecord = []

#infinite loop until a certain word or number is meet
while True: 
    try: #if error occurs it prints something
        speed = int(input("Input descent speed in m/s: "))
        if speed == 'end':
            break
        

