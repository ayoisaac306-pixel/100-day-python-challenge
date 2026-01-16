class BankAccount:
    def __init__(self, person, balance = 0):
        self.person = person
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
        return self.balance
    

account = BankAccount("ayotunde", 100)

account.deposit(1000)
account.withdraw(500)
print(f"Account holder: {account.person}, Balance: {account.balance}")