import matplotlib.pyplot as plt
import pandas as pd

def plot_balances(csv_file):
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().plot(kind='bar')
    plt.title('Monthly Balance Overview')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.tight_layout()
    plt.show()
