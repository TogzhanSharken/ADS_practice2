from bank_account import BankAccount

fixed_accounts = [
    BankAccount(1, "Ali", 150000),
    BankAccount(2, "Sara", 220000),
    BankAccount(3, "John", 100000)
]

def show_fixed():
    print("Fixed accounts:")
    for acc in fixed_accounts:
        print(acc.username, acc.balance)