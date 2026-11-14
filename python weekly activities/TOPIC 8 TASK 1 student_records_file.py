# Student Records File
# This program writes student information to students.txt.

# Open the file in write mode
f = open("students.txt", "w")

# Write student records to the file
print("Student Name: John Kamau", file=f)
print("Registration Number: BIT/001/2026", file=f)
print("Course: Information Technology", file=f)
print("Mark: 75", file=f)

print("\nStudent Name: Mary Wanjiku", file=f)
print("Registration Number: BIT/002/2026", file=f)
print("Course: Computer Science", file=f)
print("Mark: 82", file=f)

print("\nStudent Name: Peter Mwangi", file=f)
print("Registration Number: BIT/003/2026", file=f)
print("Course: Information Technology", file=f)
print("Mark: 68", file=f)

# Close the file
f.close()

print("Student records saved successfully.")
