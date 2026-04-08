transaction_stack = []

def add_transaction(action):
    transaction_stack.append(action)

def undo_transaction():
    if transaction_stack:
        print("Undo:", transaction_stack.pop())
    else:
        print("No transactions")

def last_transaction():
    if transaction_stack:
        print("Last:", transaction_stack[-1])