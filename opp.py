# OBJECT ORIENTATED PROGRAMING
# University system
class Human:
  def _init_(self, name, age):
    self.name = name
    self.age = age

  def _str_(self):
    return f"Name: {self.name}, Age: {self.age}"


class Teacher(Human):
  def _init_(self, name, age, subject):
    super()._init_(name, age)
    self.subject = subject

  def _str_(self):
    return f"Teacher: {self.name}, Subject: {self.subject}"


class Student(Human):
  def _init_(self, name, age, student_id):
    super()._init_(name, age)
    self.student_id = student_id

  def _str_(self):
    return f"Student: {self.name}, ID: {self.student_id}"


class Section:
  def _init_(self, section_name, teacher, students, timing):
    self.section_name = section_name
    self.teacher = teacher
    self.students = students
    self.timing = timing

  def _str_(self):
    student_list = ', '.join([student.name for student in self.students])
    return f"Section: {self.section_name}, Teacher: {self.teacher.name}, Students: {student_list}, Timing: {self.timing}"


class University:
  def _init_(self):
    self.sections = []
    self.total_sections = 0

  def add_section(self, section):
    self.sections.append(section)
    self.total_sections += 1

  def get_section_details(self):
    for section in self.sections:
      print(section)


# Example Usage
university = University()

teacher1 = Teacher("John Smith", 40, "Mathematics")
teacher2 = Teacher("Jane Doe", 35, "Science")


student1 = Student("Alice", 18, "101")
student2 = Student("Bob", 19, "102")
student3 = Student("Charlie", 17, "103")
student4 = Student("David", 18, "104")

section1 = Section("Math 101", teacher1, [student1, student2], "9:00 AM - 10:00 AM")
section2 = Section("Science 101", teacher2, [student3, student4], "10:00 AM - 11:00 AM")

university.add_section(section1)
university.add_section(section2)

university.get_section_details()