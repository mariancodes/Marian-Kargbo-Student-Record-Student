class Student:
    def __init__(self, name, student_id, age, grade):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grade = grade


    def display_info(self):
        print("Student Information")
        print("Name:", self.name)
        print("ID", self.student_id)
        print("Age", self.age)
        print("Grade", self.grade)

    def enroll_course(self, course):
        print(self.name, "is enrolled in", course.course_name)       

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id

    def display_info(self):
        print("Course Information")
        print("Course Name", self.course_name)
        print("Course ID", self.course_id)



student1 = Student("Marian", 5052, 19, "A")    
student1.display_info()    

student2 = Student("Isha", 2025, 17, "B")
student2.display_info()

course1 = Course("OOP", "PROG211")
course1.display_info()
student1.enroll_course(course1)