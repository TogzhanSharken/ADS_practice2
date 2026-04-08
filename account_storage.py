from bank_account import BankAccount

accounts = []

def add_account():
    acc_num = input("Account number: ")
    username = input("Username: ")
    balance = float(input("Balance: "))
    accounts.append(BankAccount(acc_num, username, balance))
    print("Account added successfully")

def display_accounts():
    for acc in accounts:
        print(f"{acc.username} – Balance: {acc.balance}")

def search_account(username):
    for acc in accounts:
        if acc.username == username:
            return acc
    return None

def deposit():
    username = input("Username: ")
    acc = search_account(username)
    if acc:
        amount = float(input("Deposit: "))
        acc.balance += amount
        print("New balance:", acc.balance)

def withdraw():
    username = input("Username: ")
    acc = search_account(username)
    if acc:
        amount = float(input("Withdraw: "))
        if acc.balance >= amount:
            acc.balance -= amount
            print("New balance:", acc.balance)
        else:
            print("Not enough money")