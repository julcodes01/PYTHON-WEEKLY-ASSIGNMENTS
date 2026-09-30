"""
Employee Status Program

This program stores basic employee information,
including whether the employee is currently active.
"""

# Employee information
employee_name = "Mary Wanjiku"
employee_age = 30
employee_salary = 55000.00
employee_active = True

# Display employee information
print(f"Employee Name: {employee_name}")
print(f"Employee Age: {employee_age}")
print(f"Employee Salary: KSh {employee_salary:.2f}")
print(f"Employee Active: {employee_active}")

# Convert a number to a string before concatenating
age_message = "Employee age is " + str(employee_age)
print(age_message)
