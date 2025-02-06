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
    def __init__(self, school_subject):
        self.__subject_taught = school_subject
        
    def teaching(self):
        print("The class is about to begin, folks!")
        
person_01 = Person()

student_01 = Student()
student_01.show_age()