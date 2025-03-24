'''This program will record the unsafe speed'''

#Variables and lists
safe_speed = 10
speedrecord = []
end_code = 'end'

#infinite loop until a certain word or number is meet
while True: 
    try: #if error occurs it prints something
        speed = input("Input descent speed in m/s: ") #ask for the speed

        if speed == end_code:
            break #if input is 'end' the code stops
        speed = int(speed)
        elif speed <= 0:
            print("Error, invalid input.")
        speed = float(speed) #converting int speed to float speed
        speedrecord.append(speed) # putting the inputs onto the list

    except ValueError: 
        print('Error, invalid input.') #if a non number is input it prints this 



