

class BankAccount:
    # don't forget to add some default values for these parameters!
    all_account_balances = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account_balances.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print(self.balance)
            return self
        else:
            print("Insufficent funds: Charging a 5$ fee")
            self.balance = self.balance - 5
            print(self.balance)
            return self
        
    def display_account_info(self):
        print("Balance: $",self.balance)
        print(self.int_rate)
        return self
    
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_account_balances:
            sum += account.balance
        print(sum)
        return sum





class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance= 0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        #print statement is showing that the account is an object but the F format isnt showing any actuall information, keeps saying invalid syntax. 
        #print(f{self.account.display_account_info})
        print(self.account.deposit)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

Account1 = User("Robert", "notimportant@gmail.com")
#it seems like everthings linked properly, im not getting any errors, but nothings showing up. going to check solutions page to see if im missing anything important. my code looks exzactley like the solutions, so i desided to put print statments inside of all the class features :D becaue mine wont print for some reason. not anythin i can read anyways. 
Account1.make_deposit(100).display_user_balance()#no idea why this dosent print anything but the deposit does.
Account1.make_withdrawl(20).make_withdrawl(81)#this kicks back the print statment for its else statment, so not sure whats going on there. 
Account1.display_user_balance#it wasent working because i dident have the () on the end of the .display_account_info, genious move. forgot that it needed it even though im not passing in an argument, going to be soon but this was fun, lost track of some time. it was nice. 
