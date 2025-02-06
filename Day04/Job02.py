class Person:
    def __init__(self):
        self.__age = 14
        
    def show_age(self):
        print(f"Your age is {self.__age}.")
        
    def greeting(self):
        print("Hello!")
        
    def change_age(self, new_age):
        self.__age = new_age
        return self.__age
    
    
class Student(Person):
    
    def going_to_school(self):
        print("I'm going to school!")
        
    def show_age(self):
        print(f"I'm {self._Person__age} years old.")
        
class Professor(Person):
    def __init__(self):
        self.__subject_taught = None
        
    def teaching(self):
        print("The class is about to begin, folks!")
        

student_01 = Student()

student_01.greeting()
student_01.going_to_school()
student_01.change_age(18)
student_01.show_age()

professor_01 = Professor()

professor_01.change_age(40)
professor_01.show_age()
professor_01.greeting()
professor_01.teaching()