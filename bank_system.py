# Demo script for the OOP-based Banking System.
# Creates multiple account objects and performs deposits,
# withdrawals, transfers, and interest-reward examples.

from bank_accounts import *

# Base accounts
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(1000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(100)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(200, Sara)

# Interest rewards account
Jim = InterestRewardsAcct(1000, "Jim")
Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100, Dave)

# Savings account (includes fee)
Blaze = SavingsAcct(1000, "Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(200, Sara)
