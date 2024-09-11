#!/usr/bin/python3
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("The current balance of account# {} is {}.".format(self.account_number, self.balance))

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance *= self.interest_rate + 100

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, transaction_fee):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        self.balance = self.balance - amount - self.transaction_fee

Savings1 = SavingsAccount(1234, 50000, 8.5)
Checkings1 = CheckingAccount(2345, 1000, 25)
Savings1.display_balance()
Checkings1.display_balance()
Savings1.apply_interest()
Checkings1.withdraw(5)
Savings1.display_balance()
Checkings1.display_balance()
