'''
 Favorite Numbers: Use a dictionary to store people’s favorite numbers  Think of  five names, and use them as keys in your dictionary  Think of a favorite number for each person, and store each as a value in your dictionary 
  Print each person’s name and their favorite number  For even more fun, poll a few friends and get some actual data for your program 
'''

peoplesFavoriteNumbers = {'James' : 7 , 'Dan' : 22, 'Bob' : 17, 'Ringo' : 1 , 'Homer' : 987}



def printPeoplesFavouriteNumbers(peopleInformation):

    for key,value in peoplesFavoriteNumbers.items():
        print (key + " has chosen " + str(value) + " as their favorite number")


printPeoplesFavouriteNumbers(peoplesFavoriteNumbers)