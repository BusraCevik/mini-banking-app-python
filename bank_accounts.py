# This module defines a small OOP-based banking system.
# It includes:
# - A custom BalanceException for insufficient funds
# - A base BankAccount class
# - Two derived account types with special behaviors
# - Deposit, withdrawal, and transfer methods


class BalanceException(Exception):
    """Raised when an account has insufficient balance for a transaction."""
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = float(initial_amount)
        self.name = account_name

        print(f"\nAccount '{self.name}' created.")
        print(f"Balance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        """Checks if the account has enough balance for a transaction."""
        if self.balance < amount:
            raise BalanceException(
                f"Sorry, account '{self.name}' has only ${self.balance:.2f} available."
            )

    def withdraw(self, amount):
        """Withdraws money after verifying sufficient balance."""
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw failed. {error}")

    def transfer(self, amount, account):
        """Transfers money to another account."""
        try:
            print("\n*************\nBeginning transfer...")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer complete.")
            print("*************\n")
        except BalanceException as error:
            print(f"\nTransfer failed. {error}")


class InterestRewardsAcct(BankAccount):
    """Account type that earns 5% bonus on deposits."""
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit complete (with 5% reward).")
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    """Savings account with transaction fee."""
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5

    def withdraw(self, amount):
        """Withdraws money including a fixed fee."""
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete (fee applied).")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw failed. {error}")
