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

def register():
    users = load_users()
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists.")
        return False
    password = input("Enter a new password: ")
    users[username] = {'password': password, 'balance': 0.0}
    save_users(users)
    print("Registration successful.")
    return True

def login():
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid credentials.")
        return None
