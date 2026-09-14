class Student:
    def __init__(self, name, admission_number, course_name, course_code):
        self.name = name
        self.admission_number = admission_number
        self.course_name = course_name
        self.course_code = course_code

    def display_student(self):
        print("Student Name:", self.name)
        print("Admission Number:", self.admission_number)
        print("Course Name:", self.course_name)
        print("Course Code:", self.course_code)


# Create a student object
student1 = Student(
    "Beth Waceke",
    "SE001",
    "Software Engineering",
    "SE101"
)

# Display student information
student1.display_student()
