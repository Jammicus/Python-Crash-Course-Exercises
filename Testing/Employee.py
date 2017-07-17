'''
Write a class called Employee. 
The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. 
Write a method called give_raise() that adds $5000 to the annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_ default_raise() and test_give_custom_raise(). 
Use the setUp() method so you don’t have to create a new employee instance in each test method. Run your test case, and make sure both tests pass
'''


class Employee() :
    def __init__(self, firstName, lastName, annualSalary):
        self.firstName = firstName
        self.lastName = lastName
        self.annualSalary = annualSalary


    def giveRaise(self, amount=''):
        if (amount== ''):
             self.annualSalary+= 5000
        else:
            self.annualSalary += amount