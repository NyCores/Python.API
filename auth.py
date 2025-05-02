import json
import os
import bcrypt

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

def register_user():
    users = load_users()
    username = input("Enter a new username: ").strip()
    if username in users:
        print("Username already exists.")
        return None
    password = input("Enter a new password: ").strip()
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = {
        'password': hashed.decode('utf-8'),
        'accounts': {}
    }
    save_users(users)
    print("User registered successfully.")
    return username

def login_user():
    users = load_users()
    username = input("Enter your username: ").strip()
    if username not in users:
        print("Username not found.")
        return None
    password = input("Enter your password: ").strip()
    stored_hash = users[username]['password'].encode('utf-8')
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        print("Login successful.")
        return username
    else:
        print("Incorrect password.")
        return None
from storage import load_users, save_users
from utils import hash_password, is_valid_username, is_valid_password

class User:
    def __init__(self, username, name, password_hash, balance=0.0):
        self.username = username
        self.name = name
        self.password_hash = password_hash
        self.balance = balance
        self.accounts = []

def register_user(username, password, name):
    """Register a new user."""
    users = load_users()
    if username in users:
        return False, "Username already exists."
    if not is_valid_username(username):
        return False, "Invalid username."
    user = User(username, name, hash_password(password), 0)
    users[username] = user
    save_users(users)
    return True, "User registered successfully."
