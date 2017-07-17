'''
Add an if test to hello_admin.py to make sure the list of users is not empty 
• If the list is empty, print the message We need to  nd some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed 
'''

usernames = ['jamesw', 'bobm', 'Admin', 'johnd', 'clarkk']

def greetUser(usernames):

    if (len(usernames)==0):
        print('We need some users!')
    else:

        for user in usernames:
            if (user.lower() == 'admin'):
                print('Hello admin, would you like to see a status report?')
            else:
                print('Welcome '+ user + '. Thanks for logging in')

greetUser(usernames)

greetUser([])