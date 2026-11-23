# Integrated Supermarket Inventory System
# This program demonstrates classes, objects, lists,
# exception handling and file handling.


# Create Product class
class Product:

    # Set product details
    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    # Calculate stock value
    def calculateStockValue(self):
        return self.price * self.quantity

    # Display product information
    def displayProduct(self):
        print(f"Product Name: {self.name}")
        print(f"Product Code: {self.code}")
        print(f"Price: KSh {self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(
            f"Stock Value: KSh "
            f"{self.calculateStockValue():.2f}"
        )
        print()


# Create list for products
products = []

try:

    # Product 1
    product1 = Product()
    product1.setProductDetails(
        "Laptop",
        "P001",
        65000,
        5
    )

    # Product 2
    product2 = Product()
    product2.setProductDetails(
        "Mouse",
        "P002",
        1500,
        10
    )

    # Product 3
    product3 = Product()
    product3.setProductDetails(
        "Keyboard",
        "P003",
        2500,
        8
    )

    # Store products in a list
    products.append(product1)
    products.append(product2)
    products.append(product3)

except ValueError:
    print("Invalid price or quantity entered.")


# Display products
print("--- Inventory ---")

for product in products:
    product.displayProduct()


# Calculate total inventory value
total_value = 0

for product in products:
    total_value += product.calculateStockValue()

print(f"Total Inventory Value: KSh {total_value:.2f}")


# Save inventory to a file
f = open("inventory.txt", "w")

for product in products:
    print(f"Product Name: {product.name}", file=f)
    print(f"Product Code: {product.code}", file=f)
    print(f"Price: KSh {product.price:.2f}", file=f)
    print(f"Quantity: {product.quantity}", file=f)
    print(
        f"Stock Value: KSh "
        f"{product.calculateStockValue():.2f}",
        file=f
    )
    print("-------------------------", file=f)

# Close the file
f.close()

print("Inventory saved to inventory.txt")
