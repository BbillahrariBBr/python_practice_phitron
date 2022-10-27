import time

class School:
    def __init__(self,name,address,principal = '') -> None:
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []
    
    def add_grade(self,name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)
    
    def remove_grade(self,name):
        idx = 0
        for i, grade in enumerate(self.grades):
            if grade.name == name:
                idx = i
        del self.grades[idx]
class Grade:
    # constructor
    def __init__(self,name,teacher) -> None:
        self.students = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'class of {self.name} with teacher {self.teacher}'
    

    def __del__(self):
        print(f'Deleting {self.name} with teacher {self.teacher}')
    

oxford = School('Oxford Kid Academy','Mirpur','Obayed Alam')
oxford.add_grade('Class 3','Osman Gani')
oxford.add_grade('Class 2','Nazma mam')
oxford.add_grade('Class 8','Razib Sir')
print(oxford.grades)

oxford.remove_grade('Class 2')
print(oxford.grades)
print('My code running is done')
time.sleep(10)