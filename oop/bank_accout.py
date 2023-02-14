class BankAccount:
    def __init__(self, int_rate, balance): 
        self.money = 0 + balance
        self.int_rate = int_rate/100
        self.balance = f"${str(self.money)}"
    def deposit(self, amount):
        self.money += amount
        self.balance = f"${str(self.money)}"
    def withdraw(self, amount):
        self.money -= amount
        self.balance = f"${str(self.money)}"
    def display_account_info(self):
        print(f"Balnce: {self.balance}")
    def yield_interest(self):
        if (self.int_rate > 0):
            self.money += float(self.money) * self.int_rate
            self.balance = f"${str(self.money)}"
user1=BankAccount(5, 500)
user1.deposit(500)
print(user1.balance)
user1.withdraw(200)
print(user1.balance)
user1.display_account_info()
user1.yield_interest()
user1.display_account_info()