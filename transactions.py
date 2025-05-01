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
