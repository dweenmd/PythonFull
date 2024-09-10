class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, ammount):
        if ammount > 0:
            self.balance += ammount
            print(f'after deposite {ammount} your balance is: {self.get_balance()}') 

    def withdraw(self, ammount):
        if ammount < self.min_withdraw:
            print(f'you can\'t withdraw bellow {self.min_withdraw}')
        elif ammount > self.max_withdraw:
            print(f'you cant\'t withdraw more than {self.max_withdraw}')
        else:
            self.balance -= ammount
            print(f'after withdraw {ammount}, your current balance is {self.get_balance()}')

jamuna= Bank(20000)
print(f'your primary balance: {jamuna.get_balance()}')
jamuna.deposit(5689)
jamuna.withdraw(6789)
jamuna.deposit(10000)
jamuna.withdraw(75)
jamuna.deposit(7945)
jamuna.withdraw(5000000)
jamuna.withdraw(7858)

