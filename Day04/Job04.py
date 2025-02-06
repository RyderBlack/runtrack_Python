class Form:
    
    def aire(self):
        return 0
    
class Rectangle(Form):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def aire(self):
        aire = self.length * self.width
        return aire
    
rect_01 = Rectangle(300,200)
print(rect_01.aire())