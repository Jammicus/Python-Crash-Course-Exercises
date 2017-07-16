# If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner  Then use your list to print a message to each person, inviting them to dinner

guests = ['Roger Federer', 'Albert Einstein', 'Elon Musk ']



def invitePeopleToDinner(guests):
    for people in guests:
        print (people + ", please come for dinner at mine")

invitePeopleToDinner(guests)