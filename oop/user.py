class User:
    def __init__(self, first, last, email, age) -> None:
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
    is_rewards_member = False
    gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        return self
    def spend_points(self,amount):
        self.gold_card_points -= amount
        return self
cameron = User("Cameron", "Shaffer", "cameron@email.com", 27)
alex = User("Alex", "Schaffer", "Alex@email.com", 25)
cameron.enroll().spend_points(50).display_info()
alex.enroll().spend_points(80).display_info()