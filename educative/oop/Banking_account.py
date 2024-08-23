#! python3
# Banking_account.py

"""
Problem statement
In this challenge, we will implement methods in the parent class and its corresponding child class.

The initializers for both classes have been defined for you.

Task 1
In the Account class, implement the getBalance() method that returns balance.

Task 2
In the Account class, implement the deposit(amount) method that adds amount to the balance. It does not return anything.

Sample input

balance = 2000
deposit(500)
getbalance()
Sample output

2500
Task 3
In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance. It does not return anything.

Sample input

balance = 2000
withdrawal(500)
getbalance()
Sample output

1500
Task 4
In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current balance. Below is the formula for calculating the interest amount:



Sample input

balance = 2000
interestRate = 5
interestAmount()
Sample output

100
The following figure shows what the result should logically look like:
"""


class Account:
    """docstring for Account."""

    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class SavingsAccount(Account):
    """docstring for SavingsAccount."""

    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100


obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())
