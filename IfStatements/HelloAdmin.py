'''
Make a list of  ve or more usernames, including the name 'admin'  Imagine you are writing code that 
will print a greeting to each user after they log in to a website  Loop through the list, and print a greeting to each user:
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for log- ging in again.
'''



usernames = ['jamesw', 'bobm', 'Admin', 'johnd', 'clarkk']

def greetUser(usernames):
    for user in usernames:
        if (user.lower() == 'admin'):
            print('Hello admin, would you like to see a status report?')
        else:
            print('Welcome '+ user + '. Thanks for logging in')

greetUser(usernames)