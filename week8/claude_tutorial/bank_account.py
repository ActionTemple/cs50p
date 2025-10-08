# A more practical example: BankAccount class

class BankAccount:
    def __init__(self, owner_name, starting_balance=0):
        # Store account information
        self.owner = owner_name
        self.balance = starting_balance
        self.transaction_history = []  # List to track all transactions

        # Record the opening deposit if there is one
        if starting_balance > 0:
            self.transaction_history.append(f"Initial deposit: +${starting_balance}")

    def deposit(self, amount):
        # Make sure amount is positive
        if amount <= 0:
            print("Error: Deposit amount must be positive")
            return False

        # Add to balance
        self.balance += amount

        # Record the transaction
        self.transaction_history.append(f"Deposit: +${amount}")

        print(f"Deposited ${amount}. New balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        # Check if amount is positive
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False

        # Check if there's enough money
        if amount > self.balance:
            print(f"Error: Insufficient funds. Current balance: ${self.balance}")
            return False

        # Subtract from balance
        self.balance -= amount

        # Record the transaction
        self.transaction_history.append(f"Withdrawal: -${amount}")

        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return True


    def transfer_to(self, destination_account, amount):
        # Try to withdraw from this account
        if not self.withdraw(amount):
            return False

        # Deposit to the destination account
        destination_account.deposit(amount)

        # Record the transaction in both accounts' history
        self.transaction_history.append(f"Transfer to {destination_account.owner}...")
        destination_account.transaction_history.append(f"Transfer from {self.owner}...")

        return True

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print(f"\nAccount Statement for {self.owner}")
        print("-" * 40)

        # Print each transaction
        for transaction in self.transaction_history:
            print(transaction)

        print("-" * 40)
        print(f"Current Balance: ${self.balance}")

# Let's demonstrate how this works
def bank_demo():
    # Create two accounts
    alice_account = BankAccount("Alice Smith", 1000)
    bob_account = BankAccount("Bob Jones")
    # Third account
    charlie_account = BankAccount("Charlie Munger", 500)

    print("Initial account info:")
    print(f"Alice's balance: ${alice_account.get_balance()}")
    print(f"Bob's balance: ${bob_account.get_balance()}")
    print(f"Charlie's balance: ${charlie_account.get_balance()}")

    # Make some transactions
    print("\nMaking transactions:")
    alice_account.withdraw(250)
    bob_account.deposit(500)
    alice_account.deposit(75)
    bob_account.withdraw(100)
    alice_account.transfer_to(bob_account, 300)
    charlie_account.transfer_to(alice_account, 150)

    # Try some invalid transactions
    print("\nTrying some invalid transactions:")
    alice_account.withdraw(2000)  # More than available balance
    bob_account.deposit(-50)      # Negative deposit amount

    # Print statements
    alice_account.print_statement()
    bob_account.print_statement()
    charlie_account.print_statement()

    # Transfer money between accounts (using existing methods)
    print("\nTransferring $200 from Alice to Bob:")
    if alice_account.withdraw(200):
        bob_account.deposit(200)
        print("Transfer completed")

# Run the demonstration
if __name__ == "__main__":
    bank_demo()
