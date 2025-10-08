

# Bank Account System with Inheritance

from datetime import datetime

# Base Account Class
class BankAccount:
    def __init__(self, owner_name, account_number, starting_balance=0):
        self.owner = owner_name
        self.account_number = account_number
        self.balance = starting_balance
        self.transactions = []

        if starting_balance > 0:
            self._record_transaction("Initial deposit", starting_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive")
            return False

        self.balance += amount
        self._record_transaction("Deposit", amount)
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False

        if amount > self.balance:
            print(f"Error: Insufficient funds. Current balance: ${self.balance}")
            return False

        self.balance -= amount
        self._record_transaction("Withdrawal", -amount)
        print(f"Withdrew ${amount}. New balance: ${self.balance}")
        return True

    def transfer_to(self, destination_account, amount):
        print(f"Attempting to transfer ${amount} to {destination_account.owner}'s account...")

        if not self.withdraw(amount):
            print("Transfer failed")
            return False

        destination_account.deposit(amount)

        # Update transaction descriptions
        self.transactions[-1]["description"] = f"Transfer to {destination_account.owner}"
        destination_account.transactions[-1]["description"] = f"Transfer from {self.owner}"

        print("Transfer completed successfully!")
        return True

    def _record_transaction(self, description, amount):
        """Internal method to record a transaction"""
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "amount": amount,
            "balance_after": self.balance
        }
        self.transactions.append(transaction)

    def print_statement(self):
        print(f"\nAccount Statement for {self.owner} (#{self.account_number})")
        print(f"Account Type: {self.__class__.__name__}")
        print("-" * 60)
        print(f"{'Date':<20} {'Description':<20} {'Amount':>10} {'Balance':>10}")
        print("-" * 60)

        for t in self.transactions:
            amount_str = f"${t['amount']}" if t['amount'] >= 0 else f"-${abs(t['amount'])}"
            print(f"{t['date']:<20} {t['description']:<20} {amount_str:>10} ${t['balance_after']:>9}")

        print("-" * 60)
        print(f"Current Balance: ${self.balance}")

        # Display any special account information
        self._display_account_info()

    def _display_account_info(self):
        """Hook for subclasses to override and display special information"""
        pass

# Savings Account - Inherits from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner_name, account_number, starting_balance=0, interest_rate=0.01):
        # Call the parent class constructor first
        super().__init__(owner_name, account_number, starting_balance)

        # Add savings-specific attributes
        self.interest_rate = interest_rate
        self.interest_earned = 0

    def apply_interest(self):
        """Apply interest to the account balance"""
        interest = self.balance * self.interest_rate
        self.interest_earned += interest
        self.deposit(interest)
        self.transactions[-1]["description"] = "Interest payment"
        print(f"Applied interest: ${interest:.2f} at rate {self.interest_rate*100}%")
        return interest

    def _display_account_info(self):
        """Override to show interest rate information"""
        print(f"Interest Rate: {self.interest_rate*100:.2f}%")
        print(f"Total Interest Earned: ${self.interest_earned:.2f}")

# Checking Account - Inherits from BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, owner_name, account_number, starting_balance=0, overdraft_limit=0):
        # Call the parent class constructor
        super().__init__(owner_name, account_number, starting_balance)

        # Add checking-specific attributes
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Override withdraw to allow overdrafts up to the limit"""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False

        # Check if withdrawal would exceed overdraft limit
        if amount > (self.balance + self.overdraft_limit):
            print(f"Error: This would exceed your overdraft limit. "
                  f"Maximum withdrawal: ${self.balance + self.overdraft_limit}")
            return False

        # Process the withdrawal
        is_overdraft = amount > self.balance

        self.balance -= amount

        if is_overdraft:
            self._record_transaction("Overdraft withdrawal", -amount)
            print(f"Withdrew ${amount} (OVERDRAFT). New balance: ${self.balance}")
        else:
            self._record_transaction("Withdrawal", -amount)
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

        return True

    def _display_account_info(self):
        """Override to show overdraft information"""
        print(f"Overdraft Limit: ${self.overdraft_limit}")
        if self.balance < 0:
            print(f"ALERT: Account is currently overdrawn by ${abs(self.balance)}")

# Demonstration
def inheritance_demo():
    # Create accounts of different types
    savings = SavingsAccount("Alice Smith", "S12345", 1000, 0.05)
    checking = CheckingAccount("Alice Smith", "C67890", 500, 200)

    print("Initial account info:")
    print(f"Savings balance: ${savings.balance}")
    print(f"Checking balance: ${checking.balance}")

    # Standard transactions
    checking.deposit(300)
    checking.withdraw(200)

    # Savings-specific: apply interest
    savings.apply_interest()

    # Checking-specific: overdraft
    print("\nTesting overdraft protection:")
    checking.withdraw(700)  # This should work with overdraft

    # Try transferring between accounts
    print("\nTransferring from savings to checking:")
    savings.transfer_to(checking, 200)

    # Print statements to see the different account types
    savings.print_statement()
    checking.print_statement()

# Run the demonstration
if __name__ == "__main__":
    inheritance_demo()
