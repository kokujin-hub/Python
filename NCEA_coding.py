'''This program will see look if there is an unsafe speed'''

#variables and list
safe_speed = 10 
speedrecord = []
end_code = 'end' #a word that will end the inf loop
not_safe_speed = 0
 
 #infinite loop until a certain word or number is meet
while True:
    try:
        speed = input("Input descent speed in m/s: ") #asking for the speed

        if speed == end_code:
            break #if input is 'end' the code stops

        if int(speed) <= 0: 
            print("Error, invalid input.")  #if 0 or negative number is put it prints out "invalid input".

        speed = float(speed) #converting int speed to float speed
        speedrecord.append(speed) # putting the inputs onto the list
    except ValueError: 
        print('Error, invalid input.') #if a non number is input it prints this 

speed = float(speed)
for speed in speedrecord:
    if speed > safe_speed:
        not_safe_speed += 1

print(f"There were {not_safe_speed} rockets faster than the safe speed")
     
 







