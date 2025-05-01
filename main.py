 from auth import register, login
from account import deposit, withdraw, check_balance

def main():
    while True:
        print("\nWelcome to the Banking CLI App")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        deposit(username)
                    elif user_choice == '2':
                        withdraw(username)
                    elif user_choice == '3':
                        check_balance(username)
                    elif user_choice == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Thank you for using the Banking CLI App.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
