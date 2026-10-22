# i. Define a class named Book
class Book:
    # ii. Constructor to initialize the four attributes
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    # iii. Method to calculate total value
    def calculate_stock_value(self):
        return self.price * self.copies

    # iv. Method to check availability
    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"

# v. Create two objects with the given information
book1 = Book("Python Basics", "John Simiyu", 1200, 5)
book2 = Book("Database Systems", "Mary Mueni", 2500, 0)

# Display each book's stock value and availability status
print(f"Book 1: {book1.title}")
print(f"Stock Value: {book1.calculate_stock_value()}")
print(f"Status: {book1.check_stock()}")

print()

print(f"Book 2: {book2.title}")
print(f"Stock Value: {book2.calculate_stock_value()}")
print(f"Status: {book2.check_stock()}")
