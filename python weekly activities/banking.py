
import logging

# 1. Configure logging to save errors in a file
logging.basicConfig(
    filename="bank_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 2. Define a custom exception
class InsufficientFundsError(Exception):
    pass


# 3. Create an account balance
balance = 5000


# 4. Function to withdraw money
def withdraw_money():

    global balance

    try:
        # Ask the user to enter withdrawal amount
        amount = float(input("Enter amount to withdraw: "))

        # Check if amount is positive
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        # Check if there is enough money
        if amount > balance:
            raise InsufficientFundsError(
                "Insufficient funds! Your account balance is too low."
            )

    except ValueError as e:
        print("Invalid input:", e)
        logging.error("ValueError occurred: %s", e)

    except InsufficientFundsError as e:
        print("Withdrawal failed:", e)
        logging.error("InsufficientFundsError occurred: %s", e)

    else:
        # Execute if no exception occurs
        balance -= amount
        print("Withdrawal successful!")
        print("Amount withdrawn: Ksh.", amount)
        print("Remaining balance: Ksh.", balance)

    finally:
        # Always execute whether an error occurs or not
        print("Thank you for using our banking application. Goodbye!")


# 5. Call the withdrawal function
withdraw_money()
