class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self._name = name
        self._account_number = account_number
        self._balance = balance
        self._loan = 0
        self._transactions = []

    def deposit(self, amount):
        self._balance += amount
        self._transactions.append(('Deposit', amount))

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self._transactions.append(('Withdraw', amount))
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self._balance

    def transfer(self, other_account, amount):
        if self._balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)
            self._transactions.append(('Transfer', amount, other_account._account_number))
        else:
            return "Insufficient funds"

    def view_transactions(self):
        return self._transactions

    def request_loan(self, amount):
        if self._loan == 0 and amount <= self._balance * 2:
            self._loan = amount
            Bank._total_loan_amount += amount
            Bank._balance -= amount
            return "Loan granted"
        else:
            return "Loan denied"

class Bank(BankAccount):
    _balance = 0
    _total_loan_amount = 0
    _loan_feature = True

    @classmethod
    def deposit(cls, amount):
        cls._balance += amount

    @classmethod
    def check_total_balance(cls):
        return cls._balance

    @classmethod
    def check_total_loan_amount(cls):
        return cls._total_loan_amount

    @classmethod
    def toggle_loan_feature(cls, status):
        cls._loan_feature = status

    def create_account(self, name):
        # This method would generate an account number and create a new account
        pass

# Sample driver code
admin = Bank('Admin', '0000')
admin.deposit(100000)  # Initial bank balance

user1 = BankAccount("Dween Mohammad", "1001")
user1.deposit(1000)
user2 = BankAccount("Jankar Mahbub", "1002")
user2.deposit(10000)

# Admin creating an account
admin.create_account("Phitron")

print(user1.check_balance())
print(user1.withdraw(500))
print(user1.transfer(user2, 300))
print(user1.view_transactions())

print(admin.check_total_balance())

print(user1.request_loan(1500))
print(user1.check_balance())

print(user2.request_loan(4000))
