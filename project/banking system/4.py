class Bank:
    def __init__(self):
        self.balance = 0
        self.users = []
        self.loan_feature_enabled = True
        self.total_loan_amount = 0

    def deposit(self, amount):
        self.balance += amount

    def check_total_balance(self):
        print("Total balance of the bank:", self.balance)

    def check_total_loan_amount(self):
        print("Total loan amount in the bank:", self.total_loan_amount)

    def toggle_loan_feature(self, enabled=True):
        self.loan_feature_enabled = enabled

    def is_bankrupt(self):
        return self.balance <= 0


class User:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"{self.name} deposited ${amount}")

    def _perform_transaction(self, amount, transaction_type, receiver=None):
        if transaction_type == 'withdraw' and self.balance < amount:
            print("Bank is bankrupt. Cannot withdraw.")
            return False
        elif transaction_type == 'transfer' and self.balance < amount:
            print("Bank is bankrupt. Cannot transfer.")
            return False

        if transaction_type == 'transfer':
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"{self.name} transferred ${amount} to {receiver.name}")
            receiver.transactions.append(f"{self.name} received ${amount} from {self.name}")
        else:
            if transaction_type == 'withdraw':
                self.balance -= amount
            elif transaction_type == 'loan':
                self.balance += amount

            self.transactions.append(f"{self.name} {transaction_type.capitalize()} ${amount}")
        return True

    def withdraw(self, amount):
        return self._perform_transaction(amount, 'withdraw')

    def transfer(self, receiver, amount):
        return self._perform_transaction(amount, 'transfer', receiver)

    def check_balance(self):
        print(f"Available balance for {self.name}: ${self.balance}")

    def view_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def request_loan(self, amount, bank):
        if bank.loan_feature_enabled and not bank.is_bankrupt():
            if amount <= self.balance * 2:
                if self._perform_transaction(amount, 'loan'):
                    bank.total_loan_amount += amount
                    self.transactions.append(f"{self.name} got a loan of ${amount}")
            else:
                print("Loan amount exceeds twice the available balance.")
        else:
            print("Loan feature is currently disabled by the admin or the bank is bankrupt.")


class Admin:
    def __init__(self):
        self.bank = Bank()

    def deposit(self, amount):
        self.bank.deposit(amount)

    def create_account(self, user_name, account_number):
        user = User(user_name, account_number)
        self.bank.users.append(user)
        print(f"Account created for {user_name} with account number {account_number}")

    def check_total_balance(self):
        self.bank.check_total_balance()

    def check_total_loan_amount(self):
        self.bank.check_total_loan_amount()

    def toggle_loan_feature(self, enabled=True):
        self.bank.toggle_loan_feature(enabled)

#driver code
admin = Admin()
admin.deposit(100000)  

admin.create_account("Dween Mohammad", "1001")
admin.create_account("Jankar Mahbub", "1002")

user1 = admin.bank.users[0]
user1.deposit(1000)
user2 = admin.bank.users[1]
user2.deposit(8000)

user1.check_balance()
user1.withdraw(500)
user1.transfer(user2, 300)
user1.view_transactions()
print('\n')
admin.check_total_balance()
print('\n')
admin.toggle_loan_feature()
user1.request_loan(1500, admin.bank)
user1.check_balance()

user2.request_loan(4000, admin.bank)
user2.view_transactions()
print('\n')
admin.check_total_loan_amount()
