import unittest
from Testing.Employee import Employee
class testEmployee(unittest.TestCase):


    def setUp(self):
        self.defaultEmployee = Employee("James", "Walter", 50000)


    def test_give_default_raise(self):
        self.defaultEmployee.giveRaise()
        self.assertEqual(self.defaultEmployee.annualSalary,55000)

    def test_give_custom_raise(self):
        self.defaultEmployee.giveRaise(1000)
        self.assertEqual(self.defaultEmployee.annualSalary,51000)