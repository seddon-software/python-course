'''
1. Create the BankAccount class with deposit, withdraw, display.  Create 3 sample objects and
deposit, withdraw followed by display

2. Create a class attribute: accountsList and a method printAllAccounts

3. Add overdraft to account and test

'''

class Overdrawn(Exception): pass
class UnknownAccount(Exception): pass
class InvalidAmount(Exception): pass

class BankAccount:
    accounts = {}
    def transfer(*, toAccountName, fromAccountName, value):
        toAccount = BankAccount.getAccount(toAccountName)
        fromAccount = BankAccount.getAccount(fromAccountName)
        fromAccount.balance -= value
        if fromAccount.isOverdrawn():
            fromAccount.balance += value
            fromAccount.withdraw(value)      # just to generate error message
        else:
            toAccount.balance += value


    def __init__(self, name, openingBalance, overdraftLimit=-1000):
        self.name = name
        self.balance = openingBalance
        self.overdraftLimit = overdraftLimit
        BankAccount.accounts[name] = self

    def deposit(self, value):
        if value < 0: raise InvalidAmount()
        self.balance += value

    def isOverdrawn(self):
        return self.balance < self.overdraftLimit

    def withdraw(self, value):
        balance = self.balance          # take a snapshot in case we need to roll back
        try:
            self.balance -= value
            if self.balance < self.overdraftLimit:
                raise Overdrawn()
        except Overdrawn as e:
            errorMessage = (f"{self.name}: can't withdraw {value} - would go overdrawn," 
                            f" current balance = {balance} and overdraft limit is {self.overdraftLimit}")
            print(errorMessage)
            self.balance = balance
            
    def printAllAccounts():
        for name,account in BankAccount.accounts.items():
            print(f"{name}: balance = {account.balance}")

    def getAccount(name):
        return BankAccount.accounts[name]

print("\n***** set up 3 sample accounts with default overdraft limits of £1000")
johnsAccount = BankAccount("John", 10000)
alisAccount = BankAccount("Ali", 25000)
suesAccount = BankAccount("Sue", 840)
BankAccount.printAllAccounts()

print("\n***** deposit money in accounts")
johnsAccount.deposit(1000)
alisAccount.deposit(2000)
suesAccount.deposit(150)
BankAccount.printAllAccounts()

print("\n***** withdraw money in accounts")
johnsAccount.withdraw(6000)
alisAccount.withdraw(5000)
suesAccount.withdraw(2500)
BankAccount.printAllAccounts()

print("\n***** attempt a transfer of funds")
BankAccount.transfer(fromAccountName="John", toAccountName="Ali", value=1000)
BankAccount.transfer(fromAccountName="Sue", toAccountName="John", value=2000)
BankAccount.printAllAccounts()

print("\n***** perform a deposit")
try:
    accountName = input("who's account are you working with? ")
    theValue = int(input("how much do you want to deposit? "))
    theAccount = BankAccount.getAccount(accountName)
    theAccount.deposit(theValue)
except InvalidAmount:
    print("Invalid amount entered: ignoring transaction")

BankAccount.printAllAccounts()


    
