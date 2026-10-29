# Customer Details Using a Tuple
# This program stores customer information in a tuple.

# Create a tuple containing customer information
customer = (
    "John Kamau",
    "C001",
    "0712345678",
    "john@gmail.com"
)

# Display the complete tuple
print("Customer Details:", customer)

# Access the customer's name
print("Customer Name:", customer[0])

# Access the customer's telephone number
print("Telephone Number:", customer[2])

# Display the number of items
print("Number of Items:", len(customer))

# Attempt to modify the telephone number
# customer[2] = "0798765432"
