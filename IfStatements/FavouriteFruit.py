'''
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list 
• Make a list of your three favorite fruits and call it favorite_fruits 
• Write  five if statements  Each should check whether a certain kind of fruit is in your list  If the fruit is in your list,
 the if block should print a statement, such as You really like bananas!
'''


favourite_fruits = ['Kiwis', 'Bananas', 'Grapes', 'Rasins']



def checkFavouriteFruits(listOfFruits):

    if ("Kiwis" in listOfFruits):
        print("You like kiwis!")
    if ("Bananas" in listOfFruits):
        print("You like bananas")
    if ("Oranges" in listOfFruits):
        print("You like oranges!")
    if ("Pears" in listOfFruits):
        print("You like pears!")
    if ("Grapes" in listOfFruits):
        print('You like grapes!')

checkFavouriteFruits(favourite_fruits)