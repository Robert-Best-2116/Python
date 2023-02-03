class User:
    def __init__(self, first_name, last_name, email, age): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age 
        self.is_rewards_member = False
        self.gold_card_points = 0


    def display_info(self):
        print( f'''
        {self.first_name}
        {self.last_name}
        {self.email}
        {self.age}
        {self.is_rewards_member}
        {self.gold_card_points}
        ''')


    def enroll(self):
        self.is_rewards_memeber = self.is_rewards_member = True
        self.gold_card_points = 200
        return self.is_rewards_member, self.gold_card_points


    def points(self, amount):
        if amount > 0: 
            self.gold_card_points = self.gold_card_points + amount
            return self.gold_card_points
        if amount < 0:
            # the reason its plus amount because if you plus a negative number it subtacts, while if you subtact a negative number it adds, if its a useage of points then it should reduce the number
            self.gold_card_points = self.gold_card_points + amount
            return self.gold_card_points


User_Robert = User("Robert", "Best", "RB@email.com", 30)
#test to be sure information is passed
#print(User_Robert)
#testing method(class function display_info)
#User.display_info(User_Robert)
#testing enroll
User.enroll(User_Robert)
#print(User.enroll(User_Robert))
#testing enroll feature actually working
User.display_info(User_Robert)
#add points
User.points(User_Robert, 50)
#add points worked
#User.display_info(User_Robert)
#subtact points
#User.points(User_Robert, -50)
#test, amount is 200 because the 50 points that were added in the above function is returned. but to double check 
#User.display_info(User_Robert)

User.points(User_Robert, -50)
# success, also i commented out the postitive ammount and it immediatley changed the points total. 
User.display_info(User_Robert)

User_Arthur = User("King", "Arthur", "isdaking@camelot.com", 15)

User.enroll(User_Arthur)
User.points(User_Arthur, -80)

User.display_info(User_Robert)
User.display_info(User_Arthur) 
