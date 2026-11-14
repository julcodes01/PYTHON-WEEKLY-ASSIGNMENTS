# Student Grading System
# This program assigns a grade based on an examination mark.

# Get student information
student_name = input("Enter student name: ")
mark = int(input("Enter examination mark: "))

# Check whether the mark is valid
if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    # Determine the grade
    if mark >= 70:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"

    # Display student information
    print("\n--- Student Results ---")
    print(f"Student Name: {student_name}")
    print(f"Mark: {mark}")
    print(f"Grade: {grade}")
