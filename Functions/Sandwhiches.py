'''
Write a function that accepts a list of items a person wants on a sandwich  
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sand- wich that is being ordered  
Call the function three times, using a different num- ber of arguments each time 
'''

def itemsForSandwhiches(*items):
    itemsToUse = []

    for item in items:
        itemsToUse.append(item)

    print("You have ordered the following fillings " + str(itemsToUse))

itemsForSandwhiches("Ham", "pickle", "Mustard")
itemsForSandwhiches("Beef", "Ham", "Chicken", "Turkey" , "Sausage")
itemsForSandwhiches("ham")