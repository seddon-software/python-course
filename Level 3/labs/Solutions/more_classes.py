'''
1. Create the BankAccount class with methods: deposit(), withdraw(), display().
   Each BankAccount object should store a name, balance and a default overdraftLimit of £1000
   Create several sample objects and then call deposit(), withdraw() followed by display() for each of the objects.

2. Create a class attribute: 'accounts' to keep track of every account.  Hint: use a dict with the account name as the key.
   The add a method: printAllAccounts() that uses the accounts class attribute to print out details of each account

3. Write code to deposit money in each of the accounts

4. Now write some code to withdraw money from some of the accounts.  Make some of the withdrawals large enough to make some of the accounts go overdrawn.  In those cases
   refuse to withdraw any funds and throw an exception instead

5. Now add a static method to your class to transfer funds between two accounts.  Attempt to make several transfers and include som that would cause one of the accounts to go overdrawn
   Make sure this results in exceptions being thrown and the transaction is rolled back  

6. Finally add exceptions to your code to cope with a) negative deposits and withdrawals b) using invalid account names in transfers
'''

class Overdrawn(Exception): pass
class InvalidAmount(Exception):
    def __init__(self, value):
        super().__init__(value)
class UnknownAccount(Exception): 
    def __init__(self, name):
        super().__init__(name)

class BankAccount:
    accounts = {}
    def transfer(*, toAccountName, fromAccountName, value):
        try:
            # get accounts
            toAccount = BankAccount.getAccount(toAccountName)
            fromAccount = BankAccount.getAccount(fromAccountName)

            # perform snapshot in case of rollback
            fromAccount_balance = fromAccount.balance
            toAccount_balance = toAccount.balance
            
            # attempt transfer
            fromAccount.withdraw(value)
            toAccount.deposit(value)

            # check for rollback
            if fromAccount.isOverdrawn():
                fromAccount.balance = fromAccount_balance
                toAccount.balance = toAccount_balance
        except UnknownAccount as e:
            print(f"Unknown account: {e}")

    def __init__(self, name, openingBalance, overdraftLimit=1000):
        self.name = name
        self.balance = openingBalance
        self.overdraftLimit = overdraftLimit
        BankAccount.accounts[name] = self

    def isOverdrawn(self):
        return self.balance < self.overdraftLimit
    
    def deposit(self, value):
        try:
            if value < 0: raise InvalidAmount(value)
            self.balance += value
        except InvalidAmount as e:
            print(f"invalid amount in deposit(): {e}")

    def withdraw(self, value):
        try:            
            if value < 0: raise InvalidAmount(value)
            balance = self.balance          # take a snapshot in case we need to roll back
            try:
                self.balance -= value
                if self.balance < -self.overdraftLimit:
                    raise Overdrawn()
            except Overdrawn as e:
                errorMessage = (f"{self.name}: can't withdraw {value} - would go overdrawn," 
                                f" current balance = {balance} and overdraft limit is {self.overdraftLimit}")
                print(errorMessage)
                self.balance = balance      # reset balance
        except InvalidAmount as e:
            print(f"invalid amount in withdraw(): {e}")

    def printAllAccounts():
        for name,account in BankAccount.accounts.items():
            print(f"{name}: balance = {account.balance} overdraftLimit = {account.overdraftLimit}")

    def getAccount(name):
        if not name in BankAccount.accounts:
            raise UnknownAccount(name)
        return BankAccount.accounts[name]

# part 1
print("\n***** set up sample accounts with default overdraft limits of £1000")
johnsAccount = BankAccount("John", 10000)
alainsAccount = BankAccount("Alain", 25000)
suesAccount = BankAccount("Sue", 840)
billsAccount = BankAccount("Bill", 17000)

# part 2
print("\ndetails of each account")
BankAccount.printAllAccounts()

# part 3
print("\n***** deposit money in accounts")
johnsAccount.deposit(1000)
alainsAccount.deposit(2000)
suesAccount.deposit(150)
billsAccount.deposit(2500)
BankAccount.printAllAccounts()

# part 4
print("\n***** withdraw money from accounts with some going overdrawn")
johnsAccount.withdraw(6000)
alainsAccount.withdraw(5000)
suesAccount.withdraw(2500)
billsAccount.withdraw(25000)
BankAccount.printAllAccounts()

# part 5
print("\n***** attempt a transfer of funds with rollback when transfer fails")
BankAccount.transfer(fromAccountName="John", toAccountName="Alain", value=1000)
BankAccount.transfer(fromAccountName="Sue", toAccountName="John", value=2000)
BankAccount.transfer(fromAccountName="Bill", toAccountName="John", value=1000)
BankAccount.printAllAccounts()

# part 6
print("\n**** try some invalid operations that generate exceptions")
alainsAccount.deposit(-3000)
johnsAccount.withdraw(-1000)

BankAccount.transfer(fromAccountName="Jim", toAccountName="John", value=1000)


    
