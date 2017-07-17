'''
Make a list called sandwich_orders and  fill it with the names of various sandwiches  
Then make an empty list called finished_sandwiches  Loop through the list of sandwich orders and 
print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of  finished sandwiches  
After all the sandwiches have been made, print a message listing each sandwich that was made 
'''

sandwich_orders = ['Tuna', 'Chicken', 'BLT', 'Ham and Cheese']

finished_sandwiches = []


def makeSandwich(orders):
    for sandwich in sandwich_orders:
        print("We are making " + sandwich + " right now!")
        finished_sandwiches.append(sandwich)

    print("The following sandwiches have been made:" + str(finished_sandwiches))


makeSandwich(sandwich_orders)
