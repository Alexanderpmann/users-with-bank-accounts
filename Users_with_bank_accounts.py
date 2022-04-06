

class BankAccount:
    bank_name = "Doja Bank" 
    all_accounts = [] 
    
    def __init__(self, balance, int_rate): 
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += (amount)
        return self
    def withdrawl(self, amount):
        self.balance -= (amount)
        return self
    def display_account_info(self):
        print(f"BankAccount: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate) 
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance, int_rate)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.display_account_info}")
        return self
    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.account += amount
        return self


