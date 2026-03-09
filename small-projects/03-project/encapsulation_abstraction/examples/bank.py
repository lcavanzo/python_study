class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # public attribute
        self.balance = balance  # public attribute

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Witdraw {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


# Demonstration
account = BankAccount("Alice", 1000)
print(
    f"Owner: {account.owner}, Balance: {account.balance}"
)  # Direct access to public attributes


account.deposit(500)
account.withdraw(200)

# Modifying public attribute directly (discouraged if internal logic depends on it)
account.balance = (
    -100
)  # This bypasses the deposit/withdraw logic and can lead to invalid state
print(f"Balance after direct modification: {account.balance}")
