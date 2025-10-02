class Account:
    def __init__(self, title, balance) -> None:
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
        else:
            print("error")


class SavingsAccount(Account):
    def __init__(self, title=None, balance=None, interestRate=None) -> None:
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100


# demo1 = Account("Mark", 2000)
# print(demo1.title, demo1.balance)
# print(demo1.getBalance())
# demo1.deposit(500)
# print(demo1.getBalance())
# print(demo1.getBalance())
# demo1.withdrawal(3000)
# print(demo1.getBalance())
#
demo2 = SavingsAccount("Mark", 2000, 5)
print(demo2.title, demo2.balance, demo2.interestRate)
print(demo2.interestAmount())
