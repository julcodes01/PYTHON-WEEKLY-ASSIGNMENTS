# Student Management System
# This program represents a student using a Python class.

class Student:

    # Method to assign student information
    def setStudentDetails(self, name, registration_number, course, mark):
        self.name = name
        self.registration_number = registration_number
        self.course = course
        self.mark = mark

    # Method to calculate the student's grade
    def calculateGrade(self):

        if self.mark >= 70:
            return "A"
        elif self.mark >= 60:
            return "B"
        elif self.mark >= 50:
            return "C"
        elif self.mark >= 40:
            return "D"
        else:
            return "F"

    # Method to display student information
    def displayStudentDetails(self):
        print("Student Name:", self.name)
        print("Registration Number:", self.registration_number)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.calculateGrade())


# Main section
student = Student()

# Set student details
student.setStudentDetails(
    "Juliet Wambui",
    "BIT/001/2026",
    "Information Technology",
    75
)

# Display student details
print("--- Student Details ---")
student.displayStudentDetails()
