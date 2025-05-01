import matplotlib.pyplot as plt
import pandas as pd

def plot_balances(transaction_file):
    df = pd.read_csv(transaction_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly = df.groupby('Month')['Amount'].sum()
    monthly.plot(kind='bar', title='Monthly Balance Overview')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.tight_layout()
    plt.show()
