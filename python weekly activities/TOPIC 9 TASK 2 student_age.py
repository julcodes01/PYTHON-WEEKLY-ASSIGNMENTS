# Student Age Registration
# This program validates the student's age input.

try:
    age = int(input("Enter your age: "))
    print("Age successfully recorded")

except ValueError:
    print("Invalid age entered")
