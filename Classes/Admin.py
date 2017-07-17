'''
An administrator is a special kind of user  
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171)  
Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", 
and so on  Write a method called show_privileges() that lists the administrator’s set of privileges  Create an instance of Admin, and call your method 
'''

from Classes import Users, Priviledges



class Admin (Users):


    def __init__(self, firstName, lastName, age, location, gender):
        super().__init__(firstName, lastName, age, location, gender)
        self.privileges = Priviledges()

admin = Admin("James", "Walter222" , 111, "London", "Unknown")
admin.describe_user()
admin.privileges.show_privileges()