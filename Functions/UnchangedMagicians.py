'''
Start with your work from Exercise 8-10  Call the function make_great() with a copy of the list of magicians’ names  
Because the original list will be unchanged, return the new list and store it in a separate list  
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great 
added to each magician’s name 
'''

magicians = ['abc', 'def', 'ghi' ,'jkm']

def show_magicians(list):
    for item in list:
        print(item)


def make_great(list):
    for magician in list:
        magician = "Great " + magician
        list.pop(0)
        list.append(magician)
    return list


magiciansNames = magicians[:]
greatCopy =  make_great(magicians)
show_magicians(magiciansNames)
show_magicians(greatCopy)
show_magicians(magicians)