class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def se_presenter(self):
        return f"Je suis {self.first_name} {self.last_name}"
        
member1 = Person("John", "Doe")
print(member1.se_presenter())

member2 = Person("Marie", "Combs")
print(member2.se_presenter())