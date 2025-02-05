class City:
    def __init__(self, city_name, nb_people):
        self.__city_name = city_name
        self.__nb_people = nb_people
    
    def get_city_name(self):
        return self.__city_name

    def get_population(self):
        return self.__nb_people
    
    def set_population(self, new_population):
        self.__nb_people = new_population
    
    def add_population(self):
        self.__nb_people += 1

    def __str__(self):
        return f"For the city of {self.__city_name}, there are about {self.__nb_people} habitants."
        

class Netizen:
    def __init__(self, netizen_name, netizen_age, netizen_city):
        self.__netizen_name = netizen_name
        self.__netizen_age = netizen_age
        self.__netizen_city = netizen_city
        self.__netizen_city.add_population()
        
    def add_population(self):
        current_population = self.__netizen_city.get_population()
        self.__netizen_city.set_population(current_population + 1)
    
    def __str__(self):
        return f"{self.__netizen_name}, {self.__netizen_age}, is living in {self.__netizen_city.get_city_name()}."
    

    
city_01 = City("Paris", 1000000)
print(city_01)

city_02 = City("Marseille", 861635)
print(city_02)

netizien_01 = Netizen("John", 45, city_01)
netizien_02 = Netizen("Myrtille", 8, city_01)
netizien_03 = Netizen("Chloe", 18, city_02)
print(netizien_01,netizien_02, netizien_03)

print(city_01)
print(city_02)