# Employee Salary Records
# This program stores employee salaries using a dictionary.

# Create employee salary dictionary
employees = {
    "John": 45000,
    "Mary": 55000,
    "Peter": 50000,
    "Ann": 60000,
    "David": 48000
}

# Display all employee names and salaries
print("--- Employee Salaries ---")

for name, salary in employees.items():
    print(f"{name}: KSh {salary:.2f}")

# Update the salary of one employee
employees["John"] = 50000

# Add a new employee
employees["James"] = 52000

# Calculate total salary
total_salary = sum(employees.values())

# Display updated records
print("\n--- Updated Employee Salaries ---")

for name, salary in employees.items():
    print(f"{name}: KSh {salary:.2f}")

print(f"\nTotal Salary Payable: KSh {total_salary:.2f}")
