class User:
    def __init__(self, first, last, email, age) -> None:
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
    is_rewards_member = False
    gold_card_points = 0