'''
 Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times  
 Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
 and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders  
 Make sure no pastrami sandwiches end up in finished_sandwiches 
'''

sandwich_orders = ['Tuna', 'Pastrami', 'Chicken', 'pastrami', 'BLT', 'pastrami', 'Ham and Cheese']

finished_sandwiches = []


def makeSandwich(orders):
    for sandwich in sandwich_orders:
        if (sandwich.lower() == 'pastrami'):
            print("Sorry, we have ran out of pastrami")
            continue
        else:
            print("We are making " + sandwich + " right now!")
            finished_sandwiches.append(sandwich)

    print("The following sandwiches have been made:" + str(finished_sandwiches))


makeSandwich(sandwich_orders)
