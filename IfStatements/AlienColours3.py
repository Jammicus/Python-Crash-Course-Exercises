'''
Turn your if-else chain from Exercise 5-4 into an if-elif- else chain 
• If the alien is green, print a message that the player earned 5 points 
• If the alien is yellow, print a message that the player earned 10 points 
• If the alien is red, print a message that the player earned 15 points 
• Write three versions of this program, making sure each message is printed for the appropriate color alien 
'''


def checkColour(colour):
    colour = colour.lower()
    if (colour == 'green'):
        print("You have earned 5 points")
    elif (colour == 'yellow'):
        print("You have earned 10 points")
    else:
        print('You have earned 15 points')

checkColour('Green')
checkColour('yellow')
checkColour('Red')