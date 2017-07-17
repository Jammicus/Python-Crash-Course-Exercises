'''
Start with a copy of your program from Exercise 8-9  Write a function called make_great() that modi es the list of magicians
 by adding the phrase the Great to each magician’s name  Call show_magicians() to see that the list has actually been modified 
'''

magicians = ['abc', 'def', 'ghi' ,'jkm']

def show_magicians():
    global  magicians
    for magician in magicians:
        print(magician)


def make_great():
    global magicians
    for magician in magicians:
        magician = "Great " + magician
        magicians.pop(0)
        magicians.append(magician)



make_great()
show_magicians()