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


student1 = Student("Marian", 5052, 19, "A")    
student1.display_info()    

student2 = Student("Isha", 2025, 17, "B")
student2.display_info()