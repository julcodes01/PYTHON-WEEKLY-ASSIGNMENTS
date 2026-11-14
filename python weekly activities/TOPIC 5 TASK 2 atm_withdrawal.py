# ATM Withdrawal System
# This program processes a simple ATM withdrawal.

# Initial account balance
balance = 50000

# Ask the customer for the withdrawal amount
withdrawal = int(input("Enter withdrawal amount: "))

# Check the withdrawal conditions
if withdrawal <= 0:
    print("Error: Withdrawal amount must be greater than zero.")

elif withdrawal > balance:
    print("Error: Insufficient account balance.")

elif withdrawal % 500 != 0:
    print("Error: Withdrawal amount must be a multiple of KSh 500.")

else:
    # Deduct the withdrawal amount
    balance = balance - withdrawal

    # Display remaining balance
    print("Withdrawal successful.")
    print(f"Remaining Balance: KSh {balance}")
