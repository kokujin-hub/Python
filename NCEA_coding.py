'''This program will record the unsafe speed'''

#Variables and lists
safe_speed = 10
speedrecord = []
end_code = 'end'
not_safe_speed = 0

#infinite loop until a certain word or number is meet
speed = input("Input descent speed in m/s: ")

while speed != end_code: 
    try: #if error occurs it prints something
        
        speed = float(speed) #converting int speed to float speed
        speedrecord.append(speed) # putting the inputs onto the list        

        if int(speed) <= 0: 
            print("Error, invalid input.")  #if 0 or negative number is put it prints out "invalid input".
        
    except ValueError: 
        print('Error, invalid input.') #if a non number is input it prints this 









