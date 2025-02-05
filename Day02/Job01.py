class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width
    
    def set_length(self, new_length):
        self.__length = new_length
        return self.__length
        
    def set_width(self, new_width):
        self.__width = new_width
        return self.__width
    
    def __str__(self):
        return f"Rectangle(length={self.__length}, width={self.__width})"
    
rect_01 = Rectangle(10,5)

print(rect_01.get_length())
rect_01.set_length(18)
rect_01.set_width(32)

print(rect_01)