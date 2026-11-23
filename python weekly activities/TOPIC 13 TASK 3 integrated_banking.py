# Integrated Simple Banking System
# This program demonstrates classes, objects, functions,
# exception handling and file handling.


# Create BankAccount class
class BankAccount:

    # Set account details
    def setAccountDetails(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance += amount

    # Withdraw money
    def withdraw(self, amount):

        if amount > self.balance:
            print(
                f"Withdrawal failed for {self.customer_name}: "
                "Insufficient balance."
            )
        else:
            self.balance -= amount
            print(
                f"Withdrawal of KSh {amount:.2f} "
                f"successful for {self.customer_name}."
            )

    # Display account details
    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: KSh {self.balance:.2f}")


# Function to perform transactions
def performTransaction(account, transaction_type, amount):

    try:

        if transaction_type == "deposit":
            account.deposit(amount)
            print(
                f"Deposit of KSh {amount:.2f} "
                f"successful."
            )

        elif transaction_type == "withdraw":
            account.withdraw(amount)

        else:
            print("Invalid transaction type.")

    except ValueError:
        print("Invalid transaction amount.")


# Create first bank account
account1 = BankAccount()
account1.setAccountDetails(
    "ACC001",
    "Juliet Wambui",
    50000
)


# Create second bank account
account2 = BankAccount()
account2.setAccountDetails(
    "ACC002",
    "John Kamau",
    30000
)


# Perform transactions
performTransaction(account1, "deposit", 5000)
performTransaction(account1, "withdraw", 10000)

performTransaction(account2, "deposit", 3000)
performTransaction(account2, "withdraw", 5000)


# Display updated account balances
print("\n--- Updated Bank Accounts ---")

account1.displayAccount()

print()

account2.displayAccount()


# Save account information to a file
f = open("accounts.txt", "w")

print(
    f"Account Number: {account1.account_number}",
    file=f
)
print(
    f"Customer Name: {account1.customer_name}",
    file=f
)
print(
    f"Balance: KSh {account1.balance:.2f}",
    file=f
)
print("-------------------------", file=f)

print(
    f"Account Number: {account2.account_number}",
    file=f
)
print(
    f"Customer Name: {account2.customer_name}",
    file=f
)
print(
    f"Balance: KSh {account2.balance:.2f}",
    file=f
)

# Close the file
f.close()

print("\nAccount details saved to accounts.txt")
