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
        return self


    def enroll(self):
        self.is_rewards_memeber = self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def points(self, amount):
        if amount > 0: 
            self.gold_card_points = self.gold_card_points + amount
            return self
        if amount < 0:
            # the reason its plus amount because if you plus a negative number it subtacts, while if you subtact a negative number it adds, if its a useage of points then it should reduce the number
            self.gold_card_points = self.gold_card_points + amount
            return self


User_Robert = User("Robert", "Best", "RB@email.com", 30)

User_Arthur = User("King", "Arthur", "isdaking@camelot.com", 15)

#so in my previous code i had it returning what it did so that way the information was still in there. i think that with just return self it should sitll be in there lets see. 
User_Robert.display_info().enroll().points(-50).display_info().points(200).display_info()
#it does after adding the new points amount, so the extra code i had in there was unnessasary, though this way of calling the function instead of the Class_Name.method(object/instace_name) also works the same, in the way that it saves the information

User_Arthur.enroll().points(-80).display_info()


