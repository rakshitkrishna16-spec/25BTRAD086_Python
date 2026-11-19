class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Current Balance: {self.balance}")
        else:
            print("Insufficient balance!")

acc = BankAccount("ACC123", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)