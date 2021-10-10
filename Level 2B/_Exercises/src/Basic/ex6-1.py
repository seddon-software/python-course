'''
Create a class that represents a bank account.  
Add methods to allow a customer to deposit() and withdraw() money 
and provide a method getBalance().  
Write a test program to check out your class.
'''

class BankAccount:
    def __init__(self, accountName):
        self.accountName = accountName
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return self.balance

johnsAccount = BankAccount("johns")
johnsAccount.deposit(350.00)
johnsAccount.deposit(250.00)
johnsAccount.deposit(500.00)
johnsAccount.withdraw(100.00)
print(johnsAccount.getBalance())



