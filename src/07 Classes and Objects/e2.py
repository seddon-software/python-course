class BankAccount:
    list_of_accounts = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.list_of_accounts.append(self)

    def getDetails(self):
        return self.name, self.balance
    
BankAccount("hubert", 25000)
BankAccount("hilda",  33000)
BankAccount("susan",  17500)
BankAccount("sheena", 41000)

for account in BankAccount.list_of_accounts:
    print(account.getDetails())

