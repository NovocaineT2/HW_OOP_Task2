class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or self.finished_courses) and course in lecturer.courses and (1<=grade<=10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
            
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.grades = {}
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student_2 = Student('Misha', 'Sipl', 'M')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses += ['Java']

best_lecturer = Lecturer('Vasya','Pupkin')
best_lecturer.courses += ['Python']
best_lecturer.courses += ['Java']

best_student.rate_lect(best_lecturer, 'Python', 10)
best_student_2.rate_lect(best_lecturer, 'Java', 9)
print (best_lecturer.grades)
 