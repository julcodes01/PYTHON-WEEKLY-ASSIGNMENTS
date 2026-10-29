# Employee Salary Calculation

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
deduction = float(input("Enter monthly deduction: "))

# Calculate housing allowance
housing_allowance = 0.10 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + housing_allowance

# Calculate net salary
net_salary = gross_salary - deduction

# Display results
print("\n--- Salary Details ---")
print(f"Employee Name: {employee_name}")
print(f"Basic Salary: KSh {basic_salary:.2f}")
print(f"Housing Allowance: KSh {housing_allowance:.2f}")
print(f"Gross Salary: KSh {gross_salary:.2f}")
print(f"Deduction: KSh {deduction:.2f}")
print(f"Net Salary: KSh {net_salary:.2f}")
