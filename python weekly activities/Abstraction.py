from abc import ABC, abstractmethod

# a) Abstract class Employee
class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name      # private - encapsulation
        self.__salary = salary  # private - encapsulation

    # Getters - the SAFE way to access private attributes
    # from the child classes
    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def display_info(self):
        print("Employee Name:", self.__name)

    @abstractmethod
    def calculate_salary(self):
        pass

# b) Two child classes
class FullTimeEmployee(Employee):
    # c) Polymorphism - same method, different behaviour
    def calculate_salary(self):
        return self.get_salary()  # full salary

class PartTimeEmployee(Employee):
    # c) Polymorphism - same method, different behaviour
    def calculate_salary(self):
        return self.get_salary() / 2  # half salary

# d) Main program
full = FullTimeEmployee("James", 60000)
part = PartTimeEmployee("Mary", 60000)

employees = [full, part]

for emp in employees:
    emp.display_info()
    print("Calculated Salary:", emp.calculate_salary())
    print("--------------------")
