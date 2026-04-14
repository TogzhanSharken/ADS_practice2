from account_storage import *
from transactions import *
from queues import *

def bank_menu():
    while True:
        print("\n--- Bank Menu ---")
        print("1 - Request account")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Back")

        choice = input("Choose: ")

        if choice == "1":
            request_account()

        elif choice == "2":
            deposit()
            add_transaction("Deposit")

        elif choice == "3":
            withdraw()
            add_transaction("Withdraw")

        elif choice == "4":
            break

        else:
            print("Invalid choice")


def atm_menu():
    while True:
        print("\n--- ATM Menu ---")
        print("1 - Balance enquiry")
        print("2 - Withdraw")
        print("3 - Back")

        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            acc = search_account(username)
            if acc:
                print("Balance:", acc.balance)
            else:
                print("Account not found")

        elif choice == "2":
            withdraw()
            add_transaction("Withdraw")

        elif choice == "3":
            break

        else:
            print("Invalid choice")


def admin_menu():
    while True:
        print("\n--- Admin Area ---")
        print("1 - Process account request")
        print("2 - View account requests")
        print("3 - Add bill")
        print("4 - Process bill payment")
        print("5 - View bill queue")
        print("6 - Transaction history")
        print("7 - Undo last transaction")
        print("8 - Back")

        choice = input("Choose: ")

        if choice == "1":
            process_request()

        elif choice == "2":
            show_requests()

        elif choice == "3":
            add_bill()

        elif choice == "4":
            process_bill()

        elif choice == "5":
            show_bills()

        elif choice == "6":
            last_transaction()

        elif choice == "7":
            undo_transaction()

        elif choice == "8":
            break

        else:
            print("Invalid choice")

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1 - Enter Bank")
        print("2 - Enter ATM")
        print("3 - Admin Area")
        print("4 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            bank_menu()

        elif choice == "2":
            atm_menu()

        elif choice == "3":
            admin_menu()

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()