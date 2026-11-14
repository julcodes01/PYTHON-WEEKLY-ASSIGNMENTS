# Sales Records
# This program adds new sales records to sales.txt.

# Get sales information
product_name = input("Enter product name: ")
quantity_sold = int(input("Enter quantity sold: "))
total_sales = float(input("Enter total sales amount: "))

# Open the file in append mode
f = open("sales.txt", "a")

# Write the new sales record
print(
    f"Product: {product_name}, Quantity: {quantity_sold}, "
    f"Total Sales: KSh {total_sales:.2f}",
    file=f
)

# Close the file
f.close()

print("Sales record saved successfully.")
