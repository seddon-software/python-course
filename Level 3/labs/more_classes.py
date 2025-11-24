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

# define Exception classess
class Overdrawn(Exception): pass
class InvalidAmount(Exception):
    def __init__(self, value):
        super().__init__(value)
class UnknownAccount(Exception): 
    def __init__(self, name):
        super().__init__(name)

class BankAccount:
    pass 
    # add your methods here 

# part 1
print("\n***** set up sample accounts with default overdraft limits of £1000")
johnsAccount = BankAccount("John", 10000)
alainsAccount = BankAccount("Alain", 25000)
suesAccount = BankAccount("Sue", 840)
billsAccount = BankAccount("Bill", 17000)

# part 2
print("\ndetails of each account")
# add your code here

# part 3
print("\n***** deposit money in accounts")
# add your code here

# part 4
print("\n***** withdraw money from accounts with some going overdrawn")
# add your code here

# part 5
print("\n***** attempt a transfer of funds with rollback when transfer fails")
# add your code here

# part 6
print("\n**** try some invalid operations that generate exceptions")
alainsAccount.deposit(-3000)
johnsAccount.withdraw(-1000)
BankAccount.transfer(fromAccountName="Jim", toAccountName="John", value=1000)


    
