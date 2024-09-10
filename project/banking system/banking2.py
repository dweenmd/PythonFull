class User:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.transactions = []
        self.loan = None  # Loan amount and status (approved/pending/rejected)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            print(f'After withdraw, your current balance: {self.balance}')
        else:
            print("Insufficient funds. Withdrawal declined.")

    def transfer(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.deposit(amount)
            self.transactions.append(
                f"Transfer: -{amount} to {other_user.name}")
            other_user.transactions.append(
                f"Transfer: +{amount} from {self.name}")
            print(f"After transfer {amount}, your current balance: {self.balance}")
        else:
            print("Insufficient funds. Transfer declined.")

    def check_balance(self):
        print(f"Your current balance: {self.balance}")

    def view_transactions(self):
        print('Transaction history:')
        for transaction in self.transactions:
            print(transaction)

    def request_loan(self, amount):
        if not self.loan:  # Check if user already has a pending/approved loan
            self.loan = {"amount": amount, "status": "pending"}
            print("Loan request submitted. Waiting for admin approval.")


class Admin:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name):
        # Generate account number
        account_number = len(self.users) + 1000
        new_user = User(name, account_number)
        self.users.append(new_user)
        print(f"Account created successfully. Account Number: {account_number}")

    def check_total_balance(self):
        self.total_balance = sum(user.balance for user in self.users)
        print(f"Total Bank Balance: {self.total_balance}")

    def check_total_loan_amount(self):
        total_loan = sum(user.loan["amount"] for user in self.users if user.loan)
        self.total_loan_amount = total_loan
        print(f"Total Loan Amount: {total_loan}")

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        print(f"Loan feature {'enabled' if self.loan_feature_enabled else 'disabled'}")

    def approve_loan(self, user):
        if self.loan_feature_enabled and user.loan and user.loan["status"] == "pending":
            if user.loan["amount"] <= user.balance * 2:
                user.loan["status"] = "approved"
                user.balance += user.loan["amount"]
                user.transactions.append(f"Loan Approved: +{user.loan['amount']}")

               
                self.total_balance += user.loan["amount"]

                self.total_loan_amount -= user.loan["amount"]
                print(f"Loan for {user.name} approved. New balance: {user.balance}")
            else:
                user.loan["status"] = "rejected"
                print(f"Loan request for {user.name} rejected. Loan amount exceeds limit.")


user1 = User("Dween Mohammad", 1001)
user1.deposit(1000)
user2 = User("Jankar Mahbub", 1002)
user2.deposit(10000)

admin = Admin()

admin.create_account("Phitron")  

user1.check_balance()
user1.withdraw(500)
user1.transfer(user2, 300)
user1.view_transactions()

admin.check_total_balance()  

user1.request_loan(1500)
admin.approve_loan(user1)
user1.check_balance()

#for user2
print('\n')
user2.request_loan(4000)
admin.approve_loan(user2)


