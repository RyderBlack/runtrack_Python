class Operations():
    def __init__(self):
        self.number01 = 12
        self.number02 = 3
    
    def addition(self):
        result = self.number01 + self.number02
        return result
        
operations = Operations()
print(f"Le resultat de {operations.number01} + {operations.number02} est {operations.addition()}")