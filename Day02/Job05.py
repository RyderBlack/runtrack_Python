class Car():
    def __init__(self, brand, model, year, kms):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kms = kms
        self.__is_on = False
        self.__fuel_tank = 50
        
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_kms(self):
        return self.__kms
    
    def get_is_on(self):
        return self.__is_on
    
    
    def set_brand(self, brand):
        self.__brand = brand
        
    def set_model(self, model):
        self.__model = model
        
    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            raise ValueError("Year must be a positive integer")
        
    def set_kms(self, kms):
        if isinstance(kms, int) and kms >= 0:
            self.__kms = kms
        else:
            raise ValueError("Kilometers must be a non-negative integer")
        
    def set_is_on(self, is_on):
        if isinstance(is_on, bool):
            self.__is_on = is_on
        else:
            raise ValueError("Is on must be a boolean value")
    
    def turn_on(self):
        if self.__check_fuel_level() > 5:
            self.__is_on = True
            print("The car is turned on")
        else:
            print("Not enough fuel in the tank to start the car.")
    
    def turn_off(self):
        self.__is_on = False
        return "The car is turned off"
    
    def __check_fuel_level(self):
        return self.__fuel_tank
    
car_01 = Car("Toyota", "Rav4", 2020, 25000)

print(car_01.get_brand()) 
car_01.set_brand("Lexus")
print(car_01.get_brand())  

car_01.turn_on()
print(car_01.turn_off())