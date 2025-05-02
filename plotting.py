import matplotlib.pyplot as plt
import pandas as pd

def plot_monthly_transactions(user):
    """Plot monthly transactions for a user."""
    transactions_data = []

    for account in user.accounts:
        for transaction in account.transactions:
            transactions_data.append({
                "amount": float(transaction.amount),
                "type": transaction.transaction_type,
                "date": transaction.date
            })

    if not transactions_data:
        print("No transactions to plot.")
        return

    df = pd.DataFrame(transactions_data)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["month_year"] = df["date"].dt.to_period("M")

    summary = df.groupby(["month_year", "type"])["amount"].sum().unstack(fill_value=0)
    summary.plot(kind="bar", figsize=(14, 7))
    plt.title("Monthly Transactions Summary")
    plt.xlabel("Month")
    plt.ylabel("Total Amount ($)")
    plt.legend(title="Transaction Type")
    plt.show()
