# Student Record Using a Dictionary
# This program stores and updates student information.

# Create the student dictionary
student = {
    "registration_number": "BIT/001/2026",
    "student_name": "Juliet Wambui",
    "course": "Information Technology",
    "year_of_study": 4
}

# Display student name and course
print("Student Name:", student["student_name"])
print("Course:", student["course"])

# Change the year of study
student["year_of_study"] = 5

# Add an email address
student["email"] = "juliet@gmail.com"

# Display the complete updated dictionary
print("\nUpdated Student Record:")
print(student)
