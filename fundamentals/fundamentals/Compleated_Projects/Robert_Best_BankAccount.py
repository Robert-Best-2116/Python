

class BankAccount:
    # don't forget to add some default values for these parameters!
    all_account_balances = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account_balances.append(self)

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            return self
        else:
            print("Insufficent funds: Charging a 5$ fee")
            self.balance = self.balance - 5
            return self
        
    def display_account_info(self):
        print("Balance: $",self.balance)
        print(self.int_rate)
        return self
    #inlitally forgot to add the self.balance + took all the money lol
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


Account1 = BankAccount(0.01, 100)
#testing to see if account information was passed through properly. 
#Account1.display_account_info()
#checked deposit functions, checked withdrawl checks & balance
#Account1.deposit(100).deposit(100).deposit(100).withdraw(50).display_account_info()
#checked withdrawl else function, deducted 5 bucks, 
#Account1.deposit(100).deposit(100).deposit(100).withdraw(450).display_account_info()

Account2 = BankAccount(0.01, 100)
#checked to see if information properly passed through
Account2.display_account_info()
Account2.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(50).withdraw(50).yield_interest().display_account_info()
# added in all acounts together, dont really have time to figure out how to print all instances of the bank accounts info, will check solutions to see how its done. 
BankAccount.all_balances()