from collections import deque
from bank_account import BankAccount
from account_storage import accounts

bill_queue = deque()
account_requests = deque()

def request_account():
    username = input("Enter username: ")
    account_requests.append(username)
    print("Request submitted")

def process_request():
    if account_requests:
        username = account_requests.popleft()
        new_acc = BankAccount(len(accounts)+1, username, 0)
        accounts.append(new_acc)
        print("Account created for", username)
    else:
        print("No requests")

def show_requests():
    print("Requests:", list(account_requests))


def add_bill():
    bill = input("Enter bill: ")
    bill_queue.append(bill)
    print("Added:", bill)

def process_bill():
    if bill_queue:
        print("Processing:", bill_queue.popleft())
    else:
        print("No bills")

def show_bills():
    print("Remaining:", list(bill_queue))