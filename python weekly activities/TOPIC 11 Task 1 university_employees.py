# University Employee System
# This program demonstrates inheritance.

# Parent class
class Employee:

    def setEmployeeDetails(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def displayEmployee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)


# Child class
class Lecturer(Employee):

    def setTeachingSubject(self, subject):
        self.subject = subject

    def displayLecturer(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Teaching Subject:", self.subject)


# Main section
lecturer = Lecturer()

# Assign employee details
lecturer.setEmployeeDetails("Dr. John Kamau", "EMP001")

# Assign teaching subject
lecturer.setTeachingSubject("Database Management Systems")

# Display information
print("--- Lecturer Details ---")
lecturer.displayLecturer()
