# Employee Bonus System
# This program checks whether an employee qualifies for a bonus.

# Get employee information
employee_name = input("Enter employee name: ")
years_of_service = int(input("Enter years of service: "))
performance_rating = int(input("Enter performance rating: "))

# Check bonus eligibility
if years_of_service >= 3 and performance_rating >= 4:
    result = "Employee qualifies for a bonus"
else:
    result = "Employee does not qualify for a bonus"

# Display employee details
print("\n--- Employee Details ---")
print(f"Employee Name: {employee_name}")
print(f"Years of Service: {years_of_service}")
print(f"Performance Rating: {performance_rating}")
print(f"Result: {result}")
