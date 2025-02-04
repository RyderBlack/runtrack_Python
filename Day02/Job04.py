class Student():
    def __init__(self, first_name, last_name, id_student):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id_student = id_student
        self.__credits_number = 0
        self.__level = self.__student_eval()
        
    def add_credits(self, added_credits):
        if added_credits > 0:
            self.__credits_number += added_credits
            self.__level = self.__student_eval()
            return self.__credits_number
        else:
            raise ValueError("The added credits must be a positive number")
    
    def __student_eval(self):
        if self.__credits_number >= 90:
            return "Excellent!"
        elif self.__credits_number >= 80:
            return "Very Good!"
        elif self.__credits_number >= 70:
            return "Good!"
        elif self.__credits_number >= 60:
            return "At least you tried.."
        elif self.__credits_number < 60:
            return "Not Enough..."
        
    def student_infos(self):
        print(f"Student's last name = {self.__last_name}")
        print(f"Student's first name = {self.__first_name}")
        print(f"Student's ID = {self.__id_student}")
        print(f"Student's level = {self.__level}")
        
    def __str__(self):
        return f"The student {self.__first_name} {self.__last_name} has the ID {self.__id_student} and has {self.__credits_number} credits."
        
        
new_student_01 = Student("John", "Doe", 145)
print(new_student_01)

new_student_01.add_credits(30)
new_student_01.add_credits(20)
new_student_01.add_credits(20)
print(new_student_01)

new_student_01.student_infos()