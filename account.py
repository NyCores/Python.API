class Account:
    def __init__(self, user):
        self.user = user
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, user):
        super().__init__(user)

class SavingsAccount(Account):
    def __init__(self, user):
        super().__init__(user)
