# Savings Account System
# This program demonstrates inheritance and interest calculation.

# Parent class
class Account:

    def setAccountDetails(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def displayAccount(self):
        print("Account Number:", self.account_number)
        print(f"Balance: KSh {self.balance:.2f}")


# Child class
class SavingsAccount(Account):

    def setInterestRate(self, interest_rate):
        self.interest_rate = interest_rate

    def calculateInterest(self):
        return self.balance * self.interest_rate / 100


# Main section
account = SavingsAccount()

# Assign account details
account.setAccountDetails("ACC1001", 100000)

# Assign interest rate
account.setInterestRate(5)

# Calculate interest
interest = account.calculateInterest()

# Display account details
print("--- Savings Account ---")
account.displayAccount()
print(f"Interest Rate: {account.interest_rate}%")
print(f"Calculated Interest: KSh {interest:.2f}")
