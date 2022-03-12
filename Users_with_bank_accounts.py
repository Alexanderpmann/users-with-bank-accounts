from bank import BankAccount


class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = 0.1
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self


class User:
    def __init__(self, data):
        self.name = data["name"]
        self.email = dta["email"]
        self.account = BankAccount()

    def make_deposit(self, amount):

        self.account.deposit(amount)

        return self

    def transfer_money(self, other_user, amount):


    user1 = User("Guido", "gman@gmail.com")
    user2 = User("Monty", "m&m@gmail.com")

