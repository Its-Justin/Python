class User:

    def __init__(self, first_name, last_name, email, age, is_reward_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_reward_member
        self.gold_card_points = gold_card_points
        
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Current points: {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points+= 200
        elif self.is_rewards_member == True:
            print("This user is already a member.")
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        if self.gold_card_points < 0:
            self.gold_card_points += amount
            print("Not enough points.")
            
        else:
            print("The transaction was succesful.")
            print(f"You now have {self.gold_card_points} points left.")
        return self

account1 = User("Jane", "Doe", "Jane@gmail.com", 30, True, 200)
account2 = User("Joe", "Doe", "Joe@gmail.com", 32)
account3 = User("Justin", "Ramirez", "Justin@gmail.com", 28)

account1.spend_points(50).display_info().enroll()

account2.enroll().spend_points(80).display_info()

account3.spend_points(40).display_info()