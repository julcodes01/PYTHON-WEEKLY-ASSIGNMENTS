# Student Examination Results

student_name = input("Enter student name: ")
coursework_mark = float(input("Enter coursework mark out of 30: "))
examination_mark = float(input("Enter examination mark out of 70: "))

# Calculate total mark
total_mark = coursework_mark + examination_mark

# Determine whether the student passed
passed = total_mark >= 40

# Display results
print("\n--- Examination Results ---")
print(f"Student Name: {student_name}")
print(f"Coursework Mark: {coursework_mark}")
print(f"Examination Mark: {examination_mark}")
print(f"Total Mark: {total_mark}")
print(f"Passed: {passed}")
