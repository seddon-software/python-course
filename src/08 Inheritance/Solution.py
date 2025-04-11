class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of ${interest:.2f}. New balance: ${self.balance:.2f}")


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
        
    def order_statement(self):
        print(f"statement ordered for {self.account_holder}'s account")

# Example usage
if __name__ == "__main__":
    savings = SavingsAccount("Alice", 1000, 0.05)
    savings.display_balance()
    savings.withdraw(200)
    savings.apply_interest()

    checking = CheckingAccount("Bob", 500, 200)
    checking.display_balance()
    checking.withdraw(600)
    checking.withdraw(200)
    checking.order_statement()
    