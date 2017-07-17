'''
Write a program that asks the user how many people are in their dinner group  
If the answer is more than eight, print a message say- ing they’ll have to wait for a table  Otherwise, report that their table is ready 
'''


def seating():
    numberOfPeople = input("How many people are there?")

    if str(numberOfPeople) > '8':
        print("Please have a seat and wait for a table to become free")
    else:
        print("Please follow me to your table")


seating()
