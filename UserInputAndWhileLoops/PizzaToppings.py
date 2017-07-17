'''
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value  
As they enter each topping, print a message saying you’ll add that topping to their pizza 
'''


def addToppings():
    topping = input("What topping would you like?")

    while topping.lower() != 'quit':
        print("Ok, we will add " + topping + "to the list")
        topping = input("What topping would you like?")


addToppings()
