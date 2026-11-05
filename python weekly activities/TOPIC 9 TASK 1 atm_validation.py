# ATM Input Validation
# This program handles invalid withdrawal input.

try:
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    print(f"Withdrawal Amount: KSh {withdrawal_amount}")

except ValueError:
    print("Invalid amount. Please enter a number.")
