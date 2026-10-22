# i. Define a class named Employee
class Employee:
    # ii. Constructor to initialize the four attributes
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    # iii. Method to calculate gross salary
    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    # v. Method to calculate tax - do this before net
    def calculate_tax(self):
        return self.calculate_gross_salary() * 0.10

    # iv. Method to calculate net salary
    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        return gross - (gross * 0.10)

# vi. Create two employee objects
emp1 = Employee("EMP101", "Alice", 50000, 10)
emp2 = Employee("EMP102", "Brian", 65000, 6)

# Display each employee's gross, tax, and net
print(f"Employee: {emp1.employee_id} - {emp1.name}")
print(f"Gross Salary: KSh {emp1.calculate_gross_salary()}")
print(f"Tax (10%): KSh {emp1.calculate_tax()}")
print(f"Net Salary: KSh {emp1.calculate_net_salary()}")

print()

print(f"Employee: {emp2.employee_id} - {emp2.name}")
print(f"Gross Salary: KSh {emp2.calculate_gross_salary()}")
print(f"Tax (10%): KSh {emp2.calculate_tax()}")
print(f"Net Salary: KSh {emp2.calculate_net_salary()}")
