# Integrated Student Management System
# This program demonstrates classes, objects, lists,
# functions, exception handling and file handling.


# Create Student class
class Student:

    # Set student details
    def setStudentDetails(self, name, registration_number, course, mark):
        self.name = name
        self.registration_number = registration_number
        self.course = course
        self.mark = mark

    # Calculate student's grade
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

    # Display student information
    def displayStudentDetails(self):
        print(f"Name: {self.name}")
        print(f"Registration Number: {self.registration_number}")
        print(f"Course: {self.course}")
        print(f"Mark: {self.mark}")
        print(f"Grade: {self.calculateGrade()}")
        print()


# Create a list to store students
students = []


# Function to display all students
def displayStudents():
    print("--- Student Records ---")

    for student in students:
        student.displayStudentDetails()


# Create student objects
try:

    student1 = Student()
    student1.setStudentDetails(
        "Juliet Wambui",
        "BIT/001/2026",
        "Information Technology",
        75
    )

    student2 = Student()
    student2.setStudentDetails(
        "John Kamau",
        "BIT/002/2026",
        "Computer Science",
        68
    )

    student3 = Student()
    student3.setStudentDetails(
        "Mary Wanjiku",
        "BIT/003/2026",
        "Information Technology",
        82
    )

    # Add students to the list
    students.append(student1)
    students.append(student2)
    students.append(student3)

except ValueError:
    print("Invalid mark entered.")


# Display all students
displayStudents()


# Save student information to a file
f = open("students.txt", "w")

for student in students:
    print(f"Name: {student.name}", file=f)
    print(
        f"Registration Number: {student.registration_number}",
        file=f
    )
    print(f"Course: {student.course}", file=f)
    print(f"Mark: {student.mark}", file=f)
    print(f"Grade: {student.calculateGrade()}", file=f)
    print("-------------------------", file=f)

# Close the file
f.close()

print("Student records saved to students.txt")
