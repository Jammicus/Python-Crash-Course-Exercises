'''
Make a class called User  Create two attributes called first_name and last_name,
 and then create several other attributes that are typically stored in a user pro le  Make a method called describe_user() that prints a summary of the user’s information  
 Make another method called greet_user() that prints a personalized greeting to the user 
Create several instances representing different users, and call both methods for each user 

--------

 Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166)  Write a method called increment_ login_attempts() that increments the value of login_attempts by 1  
 Write another method called reset_login_attempts() that resets the value of login_ attempts to 0 
Make an instance of the User class and call increment_login_attempts() several times  
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts()  
Print login_attempts again to make sure it was reset to 0ma
'''



class Users():
    def __init__(self, firstName, lastName, age, location, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.location = location
        self.gender = gender
        self.loginAttempts = 0

    def describe_user(self):
        print("Their name is " + self.firstName + " " + self.lastName)
        print("Their age is " + str(self.age))
        print("Their location is " + self.location)
        print("Their gender is " + self.gender)


    def greet_user(self):
        print("Welcome back " + self.firstName)

    def reset_login_attempts(self):
        self.loginAttempts = 0

    def increment_login_attempts(self):
        self.loginAttempts += 1

user1 = Users("James", "Walter", 20, "London", "Male")
user2 = Users("Bob" , "Bobbingham", 66, "NewYork", "Male")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

print(user2.loginAttempts)
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
print(user2.loginAttempts)
user2.reset_login_attempts()
print(user2.loginAttempts)
