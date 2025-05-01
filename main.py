from auth import login
from account import CheckingAccount, SavingsAccount
from transactions import deposit, withdraw, transfer
from visualizer import plot_balances
import sys

def main():
    print("Welcome to the CLI Banking Application")
    user = login()
    account_type = input("Select account type (Checking/Savings): ").lower()
    
    if account_type == "checking":
        account = CheckingAccount(user)
    elif account_type == "savings":
        account = SavingsAccount(user)
    else:
        print("Invalid account type. Exiting.")
        return

    while True:
        print("\nMain Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Transactions")
        print("4. Show Balance")
        print("5. View Monthly Balance Plot")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            deposit(account, amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account, amount)
        elif choice == "3":
            show_transactions(account)
        elif choice == "4":
            print(f"Balance: {account.get_balance()}")
        elif choice == "5":
            plot_balance(account)
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")
