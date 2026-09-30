# Student Grade Function
# This program uses a function to calculate a student's grade.

# Define the grading function
def calculate_grade(mark):

    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


# Get student's mark
mark = int(input("Enter student's mark: "))

# Call the function
grade = calculate_grade(mark)

# Display the result
print(f"Grade: {grade}")
