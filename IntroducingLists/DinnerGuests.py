'''
Working with one of the programs from Exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner
'''

guests = ['Roger Federer', 'Albert Einstein', 'Elon Musk ']


def invitePeopleToDinner(guests):
    for people in guests:
        print(people + ", please come for dinner at mine")


invitePeopleToDinner(guests)
print("Number of guests are " + str(len(guests)))
