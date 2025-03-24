'''This program will record the unsafe speed'''

#Variables and lists
safe_speed = 10
speedrecord = []
end_code = 'end'
not_safe_speed = 0

#infinite loop until a certain word or number is meet
while True: 
    try: #if error occurs it prints something
        speed = input("Input descent speed in m/s: ") #ask for the speed

        if speed == end_code:
            break #if input is 'end' the code stops
        if int(speed) <= 0: 
            print("Error, invalid input.")  #if 0 or negative number is put it prints out "invalid input".
        
        speed = float(speed) #converting int speed to float speed
        speedrecord.append(speed) # putting the inputs onto the list

    except ValueError: 
        print('Error, invalid input.') #if a non number is input it prints this 

for speeds in speedrecord:
    print(speeds)
    



