import matplotlib.pyplot as plt
import pandas as pd

def plot_balance(account):
    # Dummy data for example
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    balances = [account.balance for _ in months]  # Should be dynamic based on transactions

    data = pd.DataFrame({
        'Month': months,
        'Balance': balances
    })

    plt.plot(data['Month'], data['Balance'])
    plt.title(f"Balance History for {account.user}")
    plt.xlabel('Month')
    plt.ylabel('Balance')
    plt.show()
