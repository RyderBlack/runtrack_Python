class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""
        
    def aging(self):
        self.age += 1
        return f"Your animal's age is now {self.age} year old"
    
    def naming(self):
        self.name = input("Name your pet here: ")
        return f"Your pet's name is now {self.name}!"
        
tiger = Animal()
print(f"Your animal's age is : {tiger.age}")
print(tiger.aging())

print(tiger.naming())
