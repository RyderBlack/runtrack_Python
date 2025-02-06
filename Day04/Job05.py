from math import pi

class Form:
    
    def aire(self):
        return 0
  
class Rectangle(Form):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def aire(self):
        aire = self.length * self.width
        return f"The rectangle's aire is {aire:.2f}"
       
class Circle(Form):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        aire = pi * self.radius ** 2
        return f"The circle's aire is {aire:.2f}"
    
rect_01 = Rectangle(300,200)
print(rect_01.aire())    
    
circle_01 = Circle(10)
print(circle_01.aire())