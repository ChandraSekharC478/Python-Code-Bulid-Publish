# We'll build a Banking System where different types of bank accounts inherit from a base class.

# 🏦 Real-World Scenario: Banking System with Inheritance
# Requirements:
# Base Class BankAccount

# Common attributes: account_number, holder_name, balance

# Common methods: deposit(), withdraw(), get_balance()

# Derived Classes:

# SavingsAccount: Has an interest rate and a minimum balance requirement.

# CurrentAccount: Allows overdraft (negative balance).

# FixedDepositAccount: No withdrawals allowed before maturity.

class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def get_balance(self):
        return self.balance
class SavingsAccount(BankAccount):
    minimum_balance = 1000
    interest_rate = 0.04  # 4% interest rate
    def __init__(self,account_number,holder_name,balance):
        super().__init__(account_number,holder_name,balance)
    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Withdrawal would result in balance below minimum required.")
        
        return super().withdraw(amount)
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -5000  # Allows overdraft up to -5000

    def withdraw(self, amount):
        if self.balance - amount < self.OVERDRAFT_LIMIT:
            return "Overdraft limit reached! Cannot withdraw."
        return super().withdraw(amount)
    
class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, tenure):
        super().__init__(account_number, holder_name, balance)
        self.tenure = tenure  # Lock-in period in years

    def withdraw(self, amount):
        return "Withdrawal not allowed in Fixed Deposit before maturity."

    def maturity_amount(self):
        rate = 0.07  # 7% interest
        maturity_value = self.balance * (1 + rate) ** self.tenure
        return f"Maturity Amount after {self.tenure} years: {maturity_value}"
# Creating objects
savings = SavingsAccount("SAV123", "Alice", 1000)
current = CurrentAccount("CUR456", "Bob", 2000)
fixed_deposit = FixedDepositAccount("FD789", "Charlie", 5000, 5)

# Testing functionalities
print(savings.deposit(500))         # Deposited 500. New Balance: 1500
print(savings.withdraw(1100))       # Cannot withdraw! Maintaining minimum balance is required.
print(savings.add_interest-())     # Interest applied! New Balance: XXXX

print(current.withdraw(6000))       # Overdraft limit reached! Cannot withdraw.
print(current.withdraw(4000))       # Withdrawn 4000. New Balance: -2000

print(fixed_deposit.withdraw(1000)) # Withdrawal not allowed in Fixed Deposit before maturity.
print(fixed_deposit.maturity_amount())  # Maturity Amount after 5 years: XXXX
