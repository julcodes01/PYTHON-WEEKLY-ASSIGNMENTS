# Unique Product Categories Using a Set
# This program demonstrates how sets maintain unique values.

# Create a set containing product categories
# Duplicate categories are automatically removed.
categories = {
    "Electronics",
    "Clothing",
    "Food",
    "Furniture",
    "Electronics",
    "Books",
    "Clothing"
}

# Display the set
print("Original Categories:", categories)

# Add a new category
categories.add("Shoes")

# Remove one category
categories.remove("Furniture")

# Display the final set
print("Final Categories:", categories)
