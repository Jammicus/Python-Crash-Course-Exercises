'''
Make a dictionary containing three major rivers and the country each river runs through  One key-value pair might be 'nile': 'egypt' 
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt 
• Use a loop to print the name of each river included in the dictionary 
• Use a loop to print the name of each country included in the dictionary 
'''


majorRivers = {'nile' : 'Egypt', 'thames' : 'England'}


def printRivers (rivers):

    for key,value in rivers.items():
        print("The river " + key + " runs through " + value)

printRivers(majorRivers)
