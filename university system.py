class Subject:
    def __init__(self, subject_name, teacher_name):
        self.subject_name = subject_name
        self.teacher_name = teacher_name
        self.registered_students = {}

    def register_student(self, student_name, student_grade = 0):
        self.registered_students[student_name] = int(student_grade)

class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number
    
    @property
    def get_info(self):
        return f"{self.name} (ID Number: {self.id_number}) is {self.age} years old."

class Student(Person):
    def __init__(self, name, id_number, age, major, gpa):
        super().__init__(name, id_number, age)
        self.major = major
        self.gpa = gpa
        self.courses = []
    
    @property    
    def get_info(self):
        return f"{self.name} (ID Number: {self.id_number}) is {self.age} years old, and is doing a {self.major} major, with a {self.gpa} GPA."

    def enroll_in_course(self, subject):
        if subject not in self.courses: # If student doesn't have this subject
            self.courses.append(subject) # Add subject to courses list
            subject.register_student(self.name) # Register the student's name to the subject
            print(f"{self.name} successfully enrolled in {subject.subject_name}.")
        else:
            print(f"{self.name} is already enrolled in {subject.subject_name}.")
        

class Professor(Person):
    def __init__(self, name, age, id_number, department, courses_teaching):
        super().__init__(name, age, id_number)
        self.department = department
        self.courses_teaching = courses_teaching

    @property
    def get_info(self):
        course_names = "" # Create a string of subjects in courses_teaching. It used to print memory address of courses_teaching before adding this.

        for i in range(len(self.courses_teaching)):
            course_names += self.courses_teaching[i].subject_name
            if i != len(self.courses_teaching) - 1: # Checks if i is at the last item, and if not, adds a comma between items.
                course_names += ", "

        return (f"{self.name} (ID Number: {self.id_number}) is {self.age} years old, and is in the {self.department} department, teaching {course_names}.")

    def assign_grade(self, subject, student_name, grade):
        if subject in self.courses_teaching: # Checks if professor teaches this subject
            if student_name in subject.registered_students: # Checks if professor teaches this student
                subject.registered_students[student_name] = int(grade) # Updates the dictionary in class Subject
                print(f"A grade ({grade}) was assigned to {student_name} in {subject.subject_name}.")
            else:
                print(f"{student_name} is not enrolled in {subject.subject_name}.")
        else:
            print(f"{self.name} does not teach {subject.subject_name}.")

# MAIN

math = Subject("Mathematics", "Dr. Smith")
stats = Subject("Statistics", "Dr. Smith")

student1 = Student("Alice", 20, "S123", "Computer Science", 3.8)
prof = Professor("Dr. Smith", 45, "P001", "Mathematics", [math, stats])

print(student1.get_info)
print(prof.get_info)
student1.enroll_in_course(math)
prof.assign_grade(math, "Alice", 95)

print(math.registered_students)