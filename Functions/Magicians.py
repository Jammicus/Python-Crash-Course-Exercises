'''
Make a list of magician’s names  Pass the list to a function called show_magicians(), which prints the name of each magician in the list 
'''


magicians = ['abc', 'def', 'ghi' ,'jkm']

def show_magicians():
    global  magicians
    for magician in magicians:
        print(magician)

show_magicians()
