import json

def save_accounts(accounts, filename='accounts.json'):
    with open(filename, 'w') as f:
        json.dump([acc.__dict__ for acc in accounts], f)

def load_accounts(filename='accounts.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
        return [Account(**acc) for acc in data]

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open('data/users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

    if username in users and users[username] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid credentials. Please try again.")
        return login()
