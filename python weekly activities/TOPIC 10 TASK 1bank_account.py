# Bank Account System
# This program demonstrates classes and objects using a bank account.

class BankAccount:
    # Method to set account details
    def setAccountDetails(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount

    # Method to withdraw money
    def withdraw(self, amount):
        self.balance -= amount

    # Method to display account information
    def displayAccount(self):
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer_name)
        print(f"Current Balance: KSh {self.balance:.2f}")


# Main section
account = BankAccount()

# Assign account details
account.setAccountDetails("ACC001", "Juliet Wambui", 20000)

# Deposit KSh 5,000
account.deposit(5000)

# Withdraw KSh 2,000
account.withdraw(2000)

# Display account details
print("--- Bank Account Details ---")
account.displayAccount()
