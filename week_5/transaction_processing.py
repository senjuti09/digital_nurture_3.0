import logging
from datetime import datetime

def process_transaction(amount):
    try:
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount. Please enter a numeric value.")
        
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")

        print(f"Processing transaction of ${amount:.2f}...")
        
    except ValueError as e:
        log_error(e)
        print(e)
    except Exception as e:
        log_error(e)
        print("An unexpected error occurred. Please try again later.")

def validate_transaction_data(amount):
    try:
        if amount.strip() == "":
            raise ValueError("Amount cannot be empty.")
        
        amount = float(amount)

        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        return amount

    except ValueError as e:
        log_error(e)
        print(f"Error: {e}")
        return None

def log_error(error):
    with open('error_log.txt', 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"[{timestamp}] {error}\n")

def user_interaction():
    while True:
        amount = input("Enter transaction amount (or 'q' to quit): ")

        if amount.lower() == 'q':
            print("Exiting the application.")
            break

        validated_amount = validate_transaction_data(amount)

        if validated_amount is not None:
            process_transaction(validated_amount)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    print("Welcome to the Financial Transaction Processing System")
    user_interaction()
