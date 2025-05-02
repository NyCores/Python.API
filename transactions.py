import json
import os
from datetime import datetime

DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def record_transaction(username, account_type, transaction_type, amount):
    users = load_users()
    if username not in users:
        print("User not found.")
        return
    if account_type not in users[username]['accounts']:
        print(f"{account_type.capitalize()} account does not exist.")
        return
    transaction = {
        'type': transaction_type,
        'amount': amount,
        'date': datetime.now().isoformat()
    }
    users[username]['accounts'][account_type]['transactions'].append(transaction)
    save_users(users)
    print(f"Recorded {transaction_type} of ${amount:.2f} for {username}'s {account_type} account.")

def get_transaction_history(username, account_type):
    users = load_users()
    if username not in users:
        print("User not found.")
        return []
    if account_type not in users[username]['accounts']:
        print(f"{account_type.capitalize()} account does not exist.")
        return []
    transactions = users[username]['accounts'][account_type]['transactions']
    print(f"Transaction history for {username}'s {account_type} account:")
    for txn in transactions:
        print(f"{txn['date']}: {txn['type'].capitalize()} of ${txn['amount']:.2f}")
    return transactions
