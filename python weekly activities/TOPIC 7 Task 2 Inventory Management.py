# Inventory Management
# This program manages product quantities using a dictionary.

# Create inventory dictionary
inventory = {
    "Sugar": 20,
    "Rice": 35,
    "Milk": 15,
    "Bread": 25,
    "Flour": 30
}

# Display quantity of a specified product
print("Quantity of Rice:", inventory["Rice"])

# Add a new product
inventory["Cooking Oil"] = 18

# Update quantity of an existing product
inventory["Sugar"] = 25

# Remove one product
del inventory["Milk"]

# Display final inventory
print("\nFinal Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")
