'''
Make a list of people who should take the favorite languages poll  Include
some names that are already in the dictionary and some that are not 
• Loop through the list of people who should take the poll  If they have already taken the poll, 
print a message thanking them for responding  If they have not yet taken the poll, print a message inviting them to take the poll 
'''

favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

peopleToTakePoll = ['John', 'Phil' ,'bob' , 'James', 'jEn']

def informUserToTakePoll(users):
    global favoriteLanguages
    for user in users:
        if user.lower() in favoriteLanguages.keys():
            print("Thanks for taking the poll, " + user + "!")
        else:
            print("Please take the poll, " +user)

informUserToTakePoll(peopleToTakePoll)