class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    # i. The deposit method should return the amount deposited
    def deposit(self, amount):
        self.balance += amount
        return amount

    # ii. The withdraw method
    def withdraw(self, amount):
        if self.balance < amount:
            return "insufficient balance"
        else:
            self.balance -= amount
            return amount

    # iii. The check_balance method should print the current balance
    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    # iv. The customer_details method should print customer details
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Example how to use it
acc1 = BankAccount("123456", 1000, "2024-01-10", "Juliet Wambui")

print(acc1.deposit(500))      # returns 500
print(acc1.withdraw(200))     # returns 200
print(acc1.withdraw(2000))    # returns insufficient balance

acc1.check_balance()          # prints Current Balance: 1300
acc1.customer_details()
