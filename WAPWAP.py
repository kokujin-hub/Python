

#create list of pizza types
pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
quantity = []
#Go through list of pizzas om prder
for wap in pizzas:

    #Ask how many of each pizzas do we want
    many = int(input(f"how many {wap} pizzas do we want? "))
    quantity.append(many)
#Loop through all pizzas
for pizza, quantities in zip(pizzas, quantity):
    #check if quatity is greater than 0
    if quantity > 0:
        print(f'{pizza.capitalize()}: {quantity}')
    
