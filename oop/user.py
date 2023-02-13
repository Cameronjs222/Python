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
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
    def spend_points(self,amount):
        self.gold_card_points -= amount
cameron = User("Cameron", "Shaffer", "cameronjs@email.com", 27)
alex = User("Alex", "Schaffer", "Alex@email.com", 25)
cameron.display_info()
cameron.enroll()
cameron.spend_points(50)
