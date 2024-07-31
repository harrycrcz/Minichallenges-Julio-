class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def to_deposit(self):
        to_deposit = int(input('How much you want to deposit'))
        self.balance = self.balance + to_deposit
        return self.balance

    def check_balance(self):
        check_balance = print(f'You have a balance of {self.balance} dollars')
        return check_balance


harry_account = BankAccount(25000)
harry_account.to_deposit()
harry_account.check_balance()
