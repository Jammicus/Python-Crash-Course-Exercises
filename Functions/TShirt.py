'''
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt  
The function should print a sentence summarizing the size of the shirt and the message printed on it 
Call the function once using positional arguments to make a shirt  Call the function a second time using keyword arguments 
'''


def make_shirt(size, text):
    print("The  size will be " + str(size) + " and the text will say " + str(text))


make_shirt('large', 'dank' )

make_shirt('Hello', 101010101)
