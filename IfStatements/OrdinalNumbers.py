'''
Ordinal numbers indicate their position in a list,
 such as 1st or 2nd  Most ordinal numbers end in th, except 1, 2, and 3 
• Store the numbers 1 through 9 in a list 
• Loop through the list 
• Use an if-elif-else chain inside the loop to print the proper ordinal end- ing for each number  
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line 
'''

numbers = [number for number in range(1,11)]

def printOrdinal(numbers):

    for number in numbers:

        if (number == 1):
            print (str(number) + "st")
        elif (number == 2):
            print(str(number) + "nd")
        elif (number == 3):
            print(str(number) + "rd")
        else:
            print(str(number) + 'th')

printOrdinal(numbers)