from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.transactions = []

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, other_account, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def view_transactions(self):
        pass

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class User(Account):
    def __init__(self, name, account_number):
        super().__init__(name, account_number)
        self.loan = 0

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.add_transaction(f"Withdrawal: -{amount}")
            print(f'After withdrawal, your current balance: {self.balance}')
        else:
            print("Insufficient funds. Withdrawal declined.")

    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_account.deposit(amount)
            self.add_transaction(
                f"Transfer: -{amount} to {other_account.name}")
            other_account.add_transaction(
                f"Transfer: +{amount} from {self.name}")
            print(f"After transfer of {amount}, your current balance: {self.balance}")
        else:
            print("Insufficient funds. Transfer declined.")

    def check_balance(self):
        print(f"Your current balance: {self.balance}")

    def view_transactions(self):
        print('Transaction history:')
        for transaction in self.transactions:
            print(transaction)

    def request_loan(self, amount):
        if self.balance == 0:
            print("This bank is bankrupt. Try another bank.")
            return
        if amount <= 2 * self.balance:
            self.loan += amount
            self.balance -= amount  # Deduct loan amount from user's balance
            print("Loan approved. Loan amount deposited into your account.")
            print(f"Updated balance after loan: {self.balance}")
        else:
            print("Loan request rejected. Loan amount exceeds limit.")


class Admin(Account):
    def __init__(self):
        super().__init__("Admin", "0")
        self.users = []

    def create_account(self, name):
        account_number = len(self.users) + 1001
        new_user = User(name, account_number)
        self.users.append(new_user)
        print(f"Account created successfully. Account Number: {account_number}")

    def deposit(self, amount):
        self.balance += amount

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.users) + self.balance
        print(f"Total Bank Balance: {total_balance}")

    def check_total_loan_amount(self):
        total_loan = sum(user.loan for user in self.users)
        print(f"Total Loan Amount: {total_loan}")

    def toggle_loan_feature(self):
        print("Loan feature toggled.")
        # Additional logic can be added here to toggle loan feature

    def check_balance(self):
        print(f"Admin balance: {self.balance}")

    def transfer(self, other_account, amount):
        print("Admin cannot transfer funds.")

    def view_transactions(self):
        print("Admin transaction history:")
        for transaction in self.transactions:
            print(transaction)

    def withdraw(self, amount):
        if self.balance == 0:
            print("This bank is bankrupt. Try another bank.")
            return
        if amount <= self.balance:
            self.balance -= amount
            self.add_transaction(f"Admin withdrawal: -{amount}")
            print(f"After withdrawal, admin balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal declined.")


admin = Admin()
admin.deposit(100000)  # Initial bank balance

user1 = User("Dween Mohammad", "1001")
user1.deposit(1000)
user2 = User("Jankar Mahbub", "1002")
user2.deposit(10000)

admin.create_account("Phitron")  # Admin creating an account

user1.check_balance()
user1.withdraw(500)
user1.transfer(user2, 300)
user1.view_transactions()

admin.check_total_balance()

user1.request_loan(1500)
user1.check_balance()

user2.request_loan(4000)

admin.check_total_balance()
admin.check_total_loan_amount()
#1) if any one take lone . remove amount from bank balance and update bank balance.
#2 ) if bank balance is 0 and any one try to take lone from bank ..Show the message "this bank Is Bankkrupt , Try others bank"?
