class Vehicle:
    def __init__(self, brand, model, year, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price

    def vehicle_infos(self):
        return (
            "The vehicle's informations are:"
            f"Brand: {self.__brand}"
            f"Model: {self.__model}"
            f"Year: {self.__year}"
            f"Price: {self.__price}"
                )
        
    def turn_engine_on(self):
        return f"Watch out! I'm driving!!"
      
class Car(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.__doors = 4
        
    def vehicle_infos(self):
        return ("The vehicle's informations are:\n"
            f"Brand: {self._Vehicle__brand}\n"
            f"Model: {self._Vehicle__model}\n"
            f"Year: {self._Vehicle__year}\n"
            f"Doors : {self.__doors}\n"
            f"Price: {self._Vehicle__price}"
            )
        
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)  
        self.__wheels = 2
        
    def vehicle_infos(self):
        return ("The vehicle's informations are:\n"
            f"Brand: {self._Vehicle__brand}\n"
            f"Model: {self._Vehicle__model}\n"
            f"Year: {self._Vehicle__year}\n"
            f"Wheels : {self.__wheels}\n"
            f"Price: {self._Vehicle__price}"
            )  
    
    def turn_engine_on(self):
        return f"On my bike, living the dream!"
        
car_01 = Car("Toyota", "Corolla",1995, 20000)   
# print(car_01.vehicle_infos())
print(car_01.turn_engine_on())

moto_01 = Motorcycle("Yamaha", "1200 Vmax", 2025, 75000)
# print(moto_01.vehicle_infos())
print(moto_01.turn_engine_on())