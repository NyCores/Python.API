import json
import os

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def deposit(username):
    users = load_users()
    amount = float(input("Enter amount to deposit: "))
    users[username]['balance'] += amount
    save_users(users)
    print(f"${amount} deposited successfully.")

def withdraw(username):
    users = load_users()
    amount = float(input("Enter amount to withdraw: "))
    if users[username]['balance'] >= amount:
        users[username]['balance'] -= amount
        save_users(users)
        print(f"${amount} withdrawn successfully.")
    else:
        print("Insufficient balance.")

def check_balance(username):
    users = load_users()
    balance = users[username]['balance']
    print(f"Your current balance is: ${balance}")
