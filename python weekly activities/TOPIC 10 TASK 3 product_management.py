# Product Management System
# This program manages products using a Python class.

class Product:

    # Method to assign product details
    def setProductDetails(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    # Method to calculate stock value
    def calculateStockValue(self):
        return self.price * self.quantity

    # Method to display product information
    def displayProductDetails(self):
        print("Product Name:", self.name)
        print("Product Code:", self.code)
        print(f"Price: KSh {self.price:.2f}")
        print("Quantity:", self.quantity)
        print(
            f"Stock Value: KSh {self.calculateStockValue():.2f}"
        )


# Main section
product = Product()

# Set product details
product.setProductDetails(
    "Laptop",
    "P001",
    65000,
    5
)

# Display product information
print("--- Product Details ---")
product.displayProductDetails()
