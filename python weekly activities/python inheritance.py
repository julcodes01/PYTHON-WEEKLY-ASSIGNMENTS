# 1. Base class Person
class Person:
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    # 2. display_details in base class
    def display_details(self):
        print(f"Person ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# 3. Derived class Student
class Student(Person):
    def __init__(self, person_id, name, age, course, marks):
        super().__init__(person_id, name, age)  # call base constructor
        self.course = course
        self.marks = marks

    # 4. calculate_grade
    def calculate_grade(self):
        if self.marks >= 70:
            return "Grade A"
        elif self.marks >= 60:
            return "Grade B"
        elif self.marks >= 50:
            return "Grade C"
        else:
            return "Grade D"

    # 5. Override display_details - use super()
    def display_details(self):
        super().display_details()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

# 6. Derived class Lecturer
class Lecturer(Person):
    def __init__(self, person_id, name, age, department, monthly_salary):
        super().__init__(person_id, name, age)
        self.department = department
        self.monthly_salary = monthly_salary

    # 7. calculate_annual_salary
    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    # 8. Override display_details - use super()
    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        print(f"Monthly Salary: {self.monthly_salary}")

# 9. Create one Student and one Lecturer object
student1 = Student(1, "Juliet", 22, "Computer Science", 75)
lecturer1 = Lecturer(101, "Tevin", 35, "ICT", 60000)

# 10. Display details and call respective methods
print("--- Student Details ---")
student1.display_details()
print(f"Grade: {student1.calculate_grade()}")

print("\n--- Lecturer Details ---")
lecturer1.display_details()
print(f"Annual Salary: {lecturer1.calculate_annual_salary()}")
