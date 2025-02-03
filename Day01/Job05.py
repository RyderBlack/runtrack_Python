class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display_points(self):
        return f"x is {self.x} and y is {self.y}"
    
    def display_x(self):
        return self.x
    
    def display_y(self):
        return self.y
    
    def change_x(self):
        self.x = int(input("enter a new value for x :"))
        return self.x
    
    def change_y(self):
        self.y = int(input("enter a new value for x :"))
        return self.y
    
    
coord1 = Point(322,45)
print(coord1.display_points())

coord1.change_x()
print(coord1.display_points())