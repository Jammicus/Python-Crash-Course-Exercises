'''
You just found a bigger dinner table, so now more space is available  Think of three more guests to invite to dinner 
• Start with your program from Exercise 3-4 or Exercise 3-5  Add a print statement to the end of your program informing people that you found a bigger dinner table 
• Use insert() to add one new guest to the beginning of your list 
• Use insert() to add one new guest to the middle of your list 
• Use append() to add one new guest to the end of your list 
• Print a new set of invitation messages, one for each person in your list 
'''

guests = ['Roger Federer', 'Albert Einstein', 'Elon Musk ']

def invitePeopleToDinner(guests):
    for people in guests:
        print (people + ", please come for dinner at mine")

invitePeopleToDinner(guests)
print("Albert Einstien can not make dinner. He is busy apparently.")

guests[1] = 'Tim Ferris'

invitePeopleToDinner(guests)

print("Due to requests from others, we have found a bigger table and will be invited more people")


guests.insert(0, "Jon Doe")
guests.insert(2, "Tom Hanks")
guests.append("Barack Obama")

invitePeopleToDinner(guests)