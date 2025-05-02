import json
import os
from datetime import datetime

DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')

class Account:
    def __init__(self, account_type, balance=0.0):
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self.transactions.append({
            'type': 'deposit',
            'amount': amount,
            'date': datetime.now().isoformat()
        })
        print(f"Deposited ${amount:.2f} to {self.account_type} account.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append({
            'type': 'withdrawal',
            'amount': amount,
            'date': datetime.now().isoformat()
        })
        print(f"Withdrew ${amount:.2f} from {self.account_type} account.")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def create_account(username, account_type):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    if account_type in users[username]['accounts']:
        print(f"{account_type.capitalize()} account already exists.")
        return
    users[username]['accounts'][account_type] = {
        'balance': 0.0,
        'transactions': []
    }
    save_users(users)
    print(f"{account_type.capitalize()} account created for {username}.")

def deposit(username, account_type, amount):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    if account_type not in users[username]['accounts']:
        print(f"{account_type.capitalize()} account does not exist.")
        return
    if amount <= 0:
        print("Deposit amount must be positive.")
        return
    users[username]['accounts'][account_type]['balance'] += amount
    users[username]['accounts'][account_type]['transactions'].append({
        'type': 'deposit',
        'amount': amount,
        'date': datetime.now().isoformat()
    })
    save_users(users)
    print(f"Deposited ${amount:.2f} to {account_type} account for {username}.")

def withdraw(username, account_type, amount):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    if account_type not in users[username]['accounts']:
        print(f"{account_type.capitalize()} account does not exist.")
        return
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return
    if amount > users[username]['accounts'][account_type]['balance']:
        print("Insufficient funds.")
        return
    users[username]['accounts'][account_type]['balance'] -= amount
    users[username]['accounts'][account_type]['transactions'].append({
        'type': 'withdrawal',
        'amount': amount,
        'date': datetime.now().isoformat()
    })
    save_users(users)
    print(f"Withdrew ${amount:.2f} from {account_type} account for {username}.")

def get_balance(username, account_type):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    if account_type not in users[username]['accounts']:
        print(f"{account_type.capitalize()} account does not exist.")
        return
    balance = users[username]['accounts'][account_type]['balance']
    print(f"{account_type.capitalize()} account balance for {username}: ${balance:.2f}")
    return balance

def get_transactions(username, account_type):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    if account_type not in users[username]['accounts']:
        print(f"{account_type.capitalize()} account does not exist.")
        return
    transactions = users[username]['accounts'][account_type]['transactions']
    print(f"Transaction history for {account_type} account of {username}:")
    for txn in transactions:
        print(f"{txn['date']}: {txn['type'].capitalize()} of ${txn['amount']:.2f}")
    return transactions

from storage import save_accounts, load_accounts
from utils import generate_account_id

class Account:
    def __init__(self, account_id, owner, balance=0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance

def create_account(owner, acc_type):
    """Create a new account for a user."""
    acc_id = generate_account_id(acc_type)
    account = Account(acc_id, owner, 0.0)
    accounts = load_accounts()
    accounts[acc_id] = account
    save_accounts(accounts)
    return account
