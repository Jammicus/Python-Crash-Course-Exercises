'''
Make a dictionary called cities  Use the names of three cities as keys in your dictionary  
Create a dictionary of information about each city and include the country that the city is in, its approximate population,
 and one fact about that city  The keys for each city’s dictionary should be something like country, 
population, and fact  Print the name of each city and all of the information you have stored about it 
'''

londonInformation = {'country': 'London', 'population': 1000000, 'fact': 'It often rains here'}

tokyoInformation = {'country': 'Japan', 'Population': 2000000, 'fact': 'It is very compact'}

sydneyInformation = {'country': 'Australia', 'Population': 500000, 'fact': 'It is very hot here'}

cities = {'London': londonInformation, 'Tokyo': tokyoInformation, 'Sydney': sydneyInformation}


def printCityInformation(cities):
    for key, value in cities.items():
        print(key + " Has the following information")

        for key, values in value.items():
            if (key.lower() == 'country'):
                print("The country this city is in is: " + values)

            if (key.lower() == 'population'):
                print("The population of this city is: " + str(values))

            if (key.lower() == 'fact'):
                print("A fact about this city is that: " + values)

        print('\n')


printCityInformation(cities)
