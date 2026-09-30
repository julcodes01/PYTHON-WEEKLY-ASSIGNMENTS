# Supermarket Purchase System

# Get customer information
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity purchased: "))
price = float(input("Enter price per item: "))

# Calculate total cost
total_cost = quantity * price

# Display purchase information
print("\n--- Purchase Information ---")
print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price: KSh {price:.3f}")
print(f"Total Cost: KSh {total_cost:.3f}")
