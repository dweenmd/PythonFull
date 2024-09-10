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

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

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
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
        else:
            print("Bank is bankrupt. Cannot withdraw.")

    def transfer(self, receiver, amount):
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"Transferred ${amount} to {receiver.name}")
            receiver.transactions.append(f"Received ${amount} from {self.name}")
        else:
            print("Bank is bankrupt. Cannot transfer.")

    def check_balance(self):
        print(f"Available balance for {self.name}: ${self.balance}")

    def view_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def request_loan(self, amount, bank):
        if bank.loan_feature_enabled:
            if not bank.is_bankrupt():
                if amount <= self.balance * 2:
                    self.balance += amount
                    bank.total_loan_amount += amount
                    self.transactions.append(f"Got a loan of ${amount}")
                else:
                    print("Loan amount exceeds twice the available balance.")
            else:
                print("This bank is bankrupt. Try other banks.")
        else:
            print("Loan feature is currently disabled by the admin.")


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


# Sample driver code
admin = Admin()
admin.deposit(100000)  # Initial bank balance

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
user1.request_loan(1500, admin.bank)
user1.check_balance()

user2.request_loan(4000, admin.bank)
user2.view_transactions()


admin.check_total_loan_amount()

