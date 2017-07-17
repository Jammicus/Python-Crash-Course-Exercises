'''
Add an attribute called flavors that stores a list of ice cream  flavors  
Write a method that displays these  avors  Create an instance of IceCreamStand, and call this method 
'''


from Classes import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant, type):
        super().__init__(restaurant, type)
        self.flavours = ["Chocolate", "Vanilla", "Lemon", "Cookie Dough"]

    def displayFlavours(self):
        print(str(self.flavours))

iceCreamInstance = IceCreamStand("Ben & Jerries", "Desserts")
iceCreamInstance.describe_restaurant()

iceCreamInstance.displayFlavours()