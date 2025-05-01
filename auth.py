import json

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
