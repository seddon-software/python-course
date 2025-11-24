'''
Create a class that represents a BankAccount.  Give each object a name and a balance.  Add a method to 
getDetails of these attributes.

Create a few BankAccount objects.

Add a class attribute (list) to keep track of the list of BankAccount objects.

Write a loop to print out the details of every BankAccount object
'''

class BankAccount:
    list_of_accounts = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.list_of_accounts.append(self)

    def getDetails(self):
        return self.name, self.balance
    
    def getBalance(self):
        return self.balance
    
BankAccount("hubert", 25000)
BankAccount("hilda",  33000)
BankAccount("susan",  17500)
BankAccount("sheena", 41000)
BankAccount("fiona", 37000)
BankAccount("stanley", 38000)
BankAccount("peter", 21000)

print("\nUnsorted list of accounts")
for account in BankAccount.list_of_accounts:
    print(account.getDetails())

print("\nSorted list of accounts")
sortedList = sorted(BankAccount.list_of_accounts, key=BankAccount.getBalance)
for account in sortedList:
    print(account.getDetails())

