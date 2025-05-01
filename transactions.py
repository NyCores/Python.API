def deposit(account, amount):
    account.deposit(amount)
    print(f"Deposited ${amount}. New balance: ${account.get_balance()}")

def withdraw(account, amount):
    account.withdraw(amount)
    print(f"Withdrew ${amount}. New balance: ${account.get_balance()}")

def show_transactions(account):
    print("\nTransaction History:")
    for transaction in account.transactions:
        print(transaction)

import csv
from datetime import datetime

def log_transaction(user, transaction_type, amount):
    with open('data/transactions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user.username, transaction_type, amount])
