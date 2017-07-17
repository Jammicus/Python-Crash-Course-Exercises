'''
Make a class called Restaurant  The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type  
Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indi- cating that the restaurant is open 
Make an instance called restaurant from your class  Print the two attri- butes individually, and then call both methods 
----------
Start with your class from Exercise 9-1  Create three different instances from the class, and call describe_restaurant() for each instance 

---------

Start with your program from Exercise 9-1 (page 166)  Add an attribute called number_served with a default value of 0  
Create an instance called restaurant from this class  Print the number of customers the restaurant has served, and then change this value and print it again 
Add a method called set_number_served() that lets you set the number of customers that have been served  Call this method with a new number and print the value again 
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served  
Call this method with any num- ber you like that could represent how many customers were served in, say, a day of business 

'''


class Restaurant () :

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numberServed = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, number):
        self.numberServed = number

    def increment_numer_served(self):
        self.numberServed += 1


restaurant =  Restaurant("KFC", "Fried Food")
restaurantTwo = Restaurant("Hong Kong City", "Chinese")
restaurantThree = Restaurant("Pizza Hut", "Italian")


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurantTwo.describe_restaurant()
restaurantThree.describe_restaurant()

print("Number Served: " + str(restaurantThree.numberServed))
restaurantThree.set_number_served(10)
print("Number Served: " + str(restaurantThree.numberServed))
restaurantThree.increment_numer_served()
print("Number Served: " + str(restaurantThree.numberServed))
