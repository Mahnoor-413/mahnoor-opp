#OBJECT ORIENTATED PROGRAMING
# University System 
#Q NO 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Q NO 2
class Student(Person):
    def __init__(self, student_id, name, age, department=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.department = department
        self.courses = []

    def assign_department(self, department):
        self.department = department
        department.add_student(self)

    def enroll_in_course(self, course):
        self.courses.append(course)

    def __str__(self):
        course_list = ', '.join([course.name for course in self.courses])
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Department: {self.department.name if self.department else 'None'}, Courses: {course_list}"
#Q NO 3
class Teacher(Person):
    def __init__(self, teacher_id, name, age, department=None):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.department = department
        self.courses = []

    def assign_department(self, department):
        self.department = department

    def assign_course(self, course):
        self.courses.append(course)

    def __str__(self):
        course_list = ', '.join([course.name for course in self.courses])
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Age: {self.age}, Department: {self.department.name if self.department else 'None'}, Courses: {course_list}"
#Q NO 4
class Course:
    def __init__(self, course_id, name, department):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Department: {self.department.name}"

#Q NO 5
class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        course_list = ', '.join([course.name for course in self.courses])
        student_list = ', '.join([student.name for student in self.students])
        return f"Department ID: {self.department_id}, Name: {self.name}, Courses: {course_list}, Students: {student_list}"

#Q NO 6
class Section:
    def __init__(self, section_id, course, teacher, timing, room):
        self.section_id = section_id
        self.course = course
        self.teacher = teacher
        self.timing = timing
        self.room = room
        self.students = []
        course.add_section(self)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        student_list = ', '.join([student.name for student in self.students])
        return f"Section ID: {self.section_id}, Course: {self.course.name}, Teacher: {self.teacher.name}, Timing: {self.timing}, Room: {self.room}, Students: {student_list}"

#Q NO 7
class University:
    def __init__(self):
        self.departments = []
        self.students = []
        self.teachers = []
        self.courses = []
        self.sections = []

    def add_department(self, department):
        self.departments.append(department)

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def add_section(self, section):
        self.sections.append(section)

    def get_department_details(self):
        for department in self.departments:
            print(department)

    def get_student_details(self):
        for student in self.students:
            print(student)

    def get_teacher_details(self):
        for teacher in self.teachers:
            print(teacher)

    def get_course_details(self):
        for course in self.courses:
            print(course)

    def get_section_details(self):
        for section in self.sections:
            print(section)


# Example Usage
university = University()

# Departments
department_cs = Department("CS101", "Computer Science")
department_math = Department("MA101", "Mathematics")
university.add_department(department_cs)
university.add_department(department_math)

# Courses
course1 = Course("CS101", "Introduction to Programming", department_cs)
course2 = Course("CS102", "Data Structures and Algorithms", department_cs)
course3 = Course("MA101", "Calculus I", department_math)
university.add_course(course1)
university.add_course(course2)
university.add_course(course3)
department_cs.add_course(course1)
department_cs.add_course(course2)
department_math.add_course(course3)

# Students
student1 = Student("STU101", "Alice", 18)
student2 = Student("STU102", "Bob", 19)
student3 = Student("STU103", "Charlie", 17)
student1.assign_department(department_cs)
student2.assign_department(department_cs)
student3.assign_department(department_math)
student1.enroll_in_course(course1)
student1.enroll_in_course(course2)
student2.enroll_in_course(course1)
student3.enroll_in_course(course3)
university.add_student(student1)
university.add_student(student2)
university.add_student(student3)

# Teachers
teacher1 = Teacher("TEA101", "John Smith", 40)
teacher2 = Teacher("TEA102", "Jane Doe", 35)
teacher1.assign_department(department_cs)
teacher2.assign_department(department_math)
teacher1.assign_course(course1)
teacher2.assign_course(course3)
university.add_teacher(teacher1)
university.add_teacher(teacher2)

# Sections
section1 = Section("SEC101", course1, teacher1, "9:00 AM - 10:00 AM", "Room A101")
section2 = Section("SEC102", course1, teacher1, "10:00 AM - 11:00 AM", "Room A102")
section3 = Section("SEC103", course3, teacher2, "11:00 AM - 12:00 PM", "Room B101")
university.add_section(section1)
university.add_section(section2)
university.add_section(section3)
section1.add_student(student1)
section1.add_student(student2)
section3.add_student(student3)

# Print details
print("\nDepartment Details:")
university.get_department_details()
print("\nStudent Details:")
university.get_student_details()
print("\nTeacher Details:")
university.get_teacher_details()
print("\nCourse Details:")
university.get_course_details()
print("\nSection Details:")
university.get_section_details()