class Rectangle:
    def __init__(self,length, width):
        self.__length = length
        self.__width = width
        
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width
    
    def set_length(self, new_length):
        self.__length = new_length
        
    def set_width(self, new_width):
        self.__width = new_width
    
    def perimeter(self):
        perimeter = 2 * (self.get_length() + self.get_width())
        return perimeter
    
    def aire(self):
        aire = self.get_length() * self.get_width()
        return aire
        
class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.__height = height
        
    def get_height(self):
        return self.__height
    
    def calculate_volume(self):
        volume = self.get_length() * self.get_width() * self.__height
        return volume
        
        
rect_01 = Rectangle(3,8)
print(f"the perimeter of this rectangle is: {rect_01.perimeter()}")
print(f"the aire of this rectangle is: {rect_01.aire()}")
        
cuboid_01 = Parallelepiped(20, 10, 50)
print(f"the height of this parallelepiped is: {cuboid_01.get_height()}")
print(f"the volume of this parallelepiped is: {cuboid_01.calculate_volume()}")