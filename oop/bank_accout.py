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
class User:
    def __init__(self, first, last, email, age, int, balance) -> None:
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.account = BankAccount(int, balance)
    def make_deposit(self, amount):
        self.account.money += amount
        self.account.balance = f"${str(self.account.money)}"
        return self
    def make_withdraw(self, amount):
        self.account.money -= amount
        self.account.balance = f"${str(self.account.money)}"
        return self
    def display_account_info(self):
        display = f"{self.first_name} {self.last_name}'s balance: {self.account.balance}"
        print(display)
        return display
    def yield_interest(self):
        if (self.account.int_rate > 0):
            self.account.money += float(self.account.money) * self.account.int_rate
            self.account.balance = f"${str(self.account.money)}"
            return self
user1 = User('Cameron', 'Shaffer', 'Cameron@email.com', 27, 5, 500)
user1.account.deposit(800).yield_interest().display_account_info()
user1.account.withdraw(200).yield_interest().display_account_info()