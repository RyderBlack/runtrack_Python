import math

class Circle():
    def __init__(self, rayon):
        self.rayon = rayon
    
    def change_rayon(self, new_rayon):
         self.rayon = new_rayon
         return new_rayon
     
    def display_infos(self):
        print("Informations du cercle:")
        print(f"  Rayon: {self.rayon}")
        print(f"  Diamètre: {self.diametre()}")
        print(f"  Circonférence: {self.circonference()}")
        print(f"  Aire: {self.aire()}")
        
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon**2
    
    def diametre(self):
        return 2 * self.rayon
    
circle1 = Circle(4)
circle2 = Circle(7)

circle1.display_infos()

circle2.change_rayon(32)
circle2.display_infos()