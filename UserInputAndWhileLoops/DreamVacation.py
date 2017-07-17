'''
Write a program that polls users about their dream vacation  
Write a prompt similar to If you could visit one place in the world, where would you go? 
Include a block of code that prints the results of the poll 
'''


def topThreeVactions():
    locations = []

    while len(locations) <3:
        locations.append(input("Select your number " + str(len(locations)+1) + " holiday location"))

    print("Your holiday choices are ranked from best to worst: " + str(locations))

topThreeVactions()