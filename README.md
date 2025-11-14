# mini-banking-app-python
A simple OOP-based bank system built in Python, featuring custom exceptions, inheritance, and basic account operations. Created for practicing clean and modular object-oriented design and getting familiar with python.

## Features

* Create accounts
* Deposit and withdraw money
* Check balance
* Handle errors using custom exceptions

## Project Structure

```
project_folder/
├── bank_accounts.py
├── bank_system.py
└── README.md
```

## Example Usage

```python
from bank import BankAccount

account = BankAccount("Büşra", 1000)
account.deposit(200)
account.withdraw(150)
print(account.get_balance())
```

## Custom Exceptions

Custom error types are placed inside `exceptions.py` for clarity.

```python
class InsufficientFundsError(Exception):
    pass
```

## Requirements

* Python 3.10+

