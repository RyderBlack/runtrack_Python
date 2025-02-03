class Character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move_up(self):
        self.y += 1
        return self.y
    
    def move_down(self):
        self.y -= 1
        return self.y
    
    def move_right(self):
        self.x += 1
        return self.x
    
    def move_left(self):
        self.x -= 1
        return self.x
    
    def position(self):
        return (self.x, self.y)
    
char01 = Character(22,33)
print(char01.position())
char01.move_down()
print(char01.position())

char01.move_right()
print(char01.position())
