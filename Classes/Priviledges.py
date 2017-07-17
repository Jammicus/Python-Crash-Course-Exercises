'''
Write a separate Privileges class  
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7  
Move the show_privileges() method to this class  
Make a Privileges instance as an attribute in the Admin class  
Create a new instance of Admin and use your method to show its privileges 
'''


class Privileges() :
    def __init__(self):
        self.privileges = ["Can add post", "Can delete post", "Can ban user", "Can delete user"]

    def show_privileges(self):
        print("Your privileges are" + str(self.privileges))



