'''
Make several dictionaries, where the name of each dictionary is the name of a pet  In each dictionary, 
include the kind of animal and the owner’s name  Store these dictionaries in a list called pets  
Next, loop through your list and as you do print everything you know about each pet 
'''


petsKind = {'bob' : 'tiger', 'john' : 'lion', 'billy' : 'rabit' , 'sally' : 'monkey'}

petsOwner = {'john': 'james', 'sally' : 'Jane' , 'bob' : 'Gandalf' , 'billy' : 'Matt'}

pets = [petsKind, petsOwner]


def printPetInformation(pets):
    for pet in pets:
        for key,value in pet.items():
            print(key + " = " + value)

printPetInformation(pets)