'''
 Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python  
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message 
'''

def make_shirt(size, text):

    if (size.lower() == 'large' or size.lower() == 'medium'):
        print("The  size will be " + str(size) + " and the text will say " + "I Love Python")
    else:
        print("The  size will be " + str(size) + " and the text will say " + str(text))


make_shirt('large', 'dank')

make_shirt('medium', 'dank')

make_shirt('small', 101010101)
