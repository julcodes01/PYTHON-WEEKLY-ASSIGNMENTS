# Electricity Bill Calculator
# This program calculates an electricity bill using a function.

# Define the function
def calculate_bill(units_consumed, cost_per_unit):
    bill = units_consumed * cost_per_unit
    return bill


# Get input from the user
units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit: "))

# Call the function
total_bill = calculate_bill(units, cost)

# Display the bill
print(f"Electricity Bill: KSh {total_bill:.2f}")
