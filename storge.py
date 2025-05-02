import json
import os
import csv

# Ensure the data directory exists
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_users():
    """Load user data from a JSON file."""
    file_path = os.path.join(DATA_DIR, "users.json")
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return json.load(file)

def save_users(users):
    """Save user data to a JSON file."""
    file_path = os.path.join(DATA_DIR, "users.json")
    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)

def load_accounts():
    """Load account data from a JSON file."""
    file_path = os.path.join(DATA_DIR, "accounts.json")
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as file:
        return json.load(file)

def save_accounts(accounts):
    """Save account data to a JSON file."""
    file_path = os.path.join(DATA_DIR, "accounts.json")
    with open(file_path, "w") as file:
        json.dump(accounts, file, indent=4)

def append_transaction_to_csv(transaction):
    """Append a transaction to a CSV file."""
    file_path = os.path.join(DATA_DIR, "transactions.csv")
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Type", "Amount", "Account ID"])
        writer.writerow([transaction.date, transaction.transaction_type, transaction.amount, transaction.account_id])
