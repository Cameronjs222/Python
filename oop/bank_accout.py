class BankAccount:
    def __init__(self, int_rate, balance): 
        self.money = 0 + balance
        self.int_rate = int_rate/100
        self.balance = f"${str(self.money)}"
    def deposit(self, amount):
        self.money += amount
        self.balance = f"${str(self.money)}"
        return self
    def withdraw(self, amount):
        self.money -= amount
        self.balance = f"${str(self.money)}"
        return self
    def display_account_info(self):
        display = f"Balance: {self.balance}"
        print(display)
        return display
    def yield_interest(self):
        if (self.int_rate > 0):
            self.money += float(self.money) * self.int_rate
            self.balance = f"${str(self.money)}"
            return self
user1=BankAccount(5, 500)
user2=BankAccount(5, 10000)
user1.deposit(100).deposit(500).deposit(50).withdraw(70).yield_interest().display_account_info()
user2.deposit(1000).deposit(5000).withdraw(500).withdraw(100).withdraw(400).withdraw(1000).yield_interest().display_account_info()