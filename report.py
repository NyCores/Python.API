from datetime import datetime

def generate_transaction_summary(user):
    """Generate a summary report of transactions for a user."""
    report = ""
    for account in user.accounts:
        deposits, withdrawals, transfers, dates = [], [], [], []
        report += f"\n==============================\nAccount Number: {account.account_id}\n"
        report += f"Account Type: {account.__class__.__name__}\nBalance: ${account.balance:.2f}\n"
        report += "------------------------------\n"

        for transaction in account.transactions:
            report += f"{transaction}\n"
            if transaction.transaction_type == "deposit":
                deposits.append(float(transaction.amount))
            elif transaction.transaction_type == "withdrawal":
                withdrawals.append(float(transaction.amount))
            elif transaction.transaction_type == "transfer":
                transfers.append(float(transaction.amount))
            try:
                dates.append(datetime.strptime(transaction.date, "%Y-%m-%d"))
            except ValueError:
                continue

        if dates:
            report += f"First Transaction Date: {min(dates).strftime('%Y-%m-%d')}\n"
            report += f"Most Recent Transaction Date: {max(dates).strftime('%Y-%m-%d')}\n"

        if deposits:
            report += f"Total Deposits: {len(deposits)}, Avg Deposit: ${sum(deposits)/len(deposits):.2f}\n"

    return report
