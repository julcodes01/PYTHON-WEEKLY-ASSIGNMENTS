# Student Marks Using a List
# This program stores and processes five subject marks.

# Create a list containing five subject marks
marks = [75, 68, 82, 55, 90]

# Display all marks
print("Student Marks:", marks)

# Calculate total marks
total_marks = sum(marks)
print("Total Marks:", total_marks)

# Calculate average mark
average_mark = total_marks / len(marks)
print("Average Mark:", average_mark)

# Display highest mark
highest_mark = max(marks)
print("Highest Mark:", highest_mark)

# Display lowest mark
lowest_mark = min(marks)
print("Lowest Mark:", lowest_mark)

# Modify the third subject mark
marks[2] = 88

# Display updated list
print("Updated Marks:", marks)
