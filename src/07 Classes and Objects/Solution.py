class BankAccount:
    accounts = {}
    def __init__(self, name, openingBalance):
        self.name = name
        self.balance = openingBalance
        BankAccount.accounts[name] = self
    def deposit(self, value):
        self.balance += value
    def withdraw(self, value):
        self.balance -= value
    def printAllAccounts():
        for name,account in BankAccount.accounts.items():
            print(f"{name}: {account.balance}")
    def getAccount(name):
        return BankAccount.accounts[name]

johnsAccount = BankAccount("John", 10000)
alisAccount = BankAccount("Ali", 25000)
suesAccount = BankAccount("Sue", 31000)

BankAccount.printAllAccounts()

accountName = input("who's account are you working with? ")
theValue = int(input("how much do you want to deposit? "))
theAccount = BankAccount.getAccount(accountName)
theAccount.deposit(theValue)
BankAccount.printAllAccounts()


    