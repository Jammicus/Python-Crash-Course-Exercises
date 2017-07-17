'''
Start with your program from Exercise 8-7  Write a while loop that allows users to enter an album’s artist and title  
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created  
Be sure to include a quit value in the while loop 
'''


def make_album(artist, title, numberOfTracks=0):

    if numberOfTracks != 0:

        return {'artist':artist,'title':title,'numberOfTracks' : numberOfTracks}

    else:
        return {'artist': artist, 'title': title}



artist = 'not null'

while (artist != ""):
    artist = input("Who is the albums artist? (Leave this blank to exit)")
    title = input("What is the title of the album")
    numberOfTracks = input("How many tracks are there? (Leave blank if you do not know)")

    if numberOfTracks != '':
        print(make_album(artist, title,numberOfTracks))
    else:
        print(make_album(artist, title))
