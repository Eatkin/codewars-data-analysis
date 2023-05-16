# https://www.codewars.com/kata/5a03af9606d5b65ff7000009
2023-04-19T18:22:15.910+0000
class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def withdraw(self, withdrawal):
        if self.balance >= withdrawal:
            self.balance -= withdrawal
            return f"{self.name} has {self.balance}."
        else:
            raise ValueError("Insufficient funds")
        
    def check(self, user, money):
        # wtf does "check" mean?
        # I have to take that amount of money of user and add it to our balance
        if user.balance >= money and user.checking_account:
            user.balance -= money
            self.balance += money
            return f"{self.name} has {self.balance} and {user.name} has {user.balance}."
        else:
            if not user.checking_account:
                raise ValueError(f"{user.name} doesn't have a checking account")
            raise ValueError(f"{user.name} has insuffient funds")
        
    def add_cash(self, money):
        self.balance += money
        return f"{self.name} has {self.balance}."
        