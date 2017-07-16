'''
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests 
• Start with your program from Exercise 3-6  Add a new line that prints a message saying that you can invite only two people for dinner 
• Use pop() to remove guests from your list one at a time until only two names remain in your list  Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner 
• Print a message to each of the two people still on your list, letting them know they’re still invited 
• Use del to remove the last two names from your list, so you have an empty list  Print your list to make sure you actually have an empty list at the end of your program 

'''

newLineRegex = "\n"
guests = ['Roger Federer', 'Albert Einstein', 'Elon Musk ']


def invitePeopleToDinner(guests):
    for people in guests:
        print(people + ", please come for dinner at mine")


invitePeopleToDinner(guests)
print(newLineRegex)
print("Albert Einstien can not make dinner. He is busy apparently.")

guests[1] = 'Tim Ferris'

invitePeopleToDinner(guests)
print(newLineRegex)

print("Due to requests from others, we have found a bigger table and will be invited more people")

guests.insert(0, "Jon Doe")
guests.insert(2, "Tom Hanks")
guests.append("Barack Obama")

invitePeopleToDinner(guests)

print(newLineRegex)

print("We have now lost that bigger table we claimed to have found earlier, we will be using a 2 person foldable table instead")

while (len(guests) > 2):
    print("Sorry  " + guests[-1] + " You cannot come for dinner")
    guests.pop()

print(newLineRegex)

invitePeopleToDinner(guests)

print(newLineRegex)

print("Change of plans, no one can come to dinner now")

print(newLineRegex)

while (len(guests) > 0):
    del guests[0]

print("We have the following guests on the invitation list: " + str(guests))
