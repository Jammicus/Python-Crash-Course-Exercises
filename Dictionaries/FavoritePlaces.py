'''
Make a dictionary called favorite_places  Think of three names to use as keys in the dictionary, and store one to three 
favorite places for each person  To make this exercise a bit more interesting, 
ask some friends to name a few of their favorite places  Loop through the dictionary, and print each person’s name and their favorite places 
'''

favorite_places = {'James': ['London', 'Tokyo'], 'Bob': ['McDonalds', 'KFC'], 'Jennie': ['Stockholm', 'London']}


def printFavoritePlaces(places):
    for key, value in places.items():
        print(key + " has chosen the following as his or hers favorite places" + str(value))


printFavoritePlaces(favorite_places)
