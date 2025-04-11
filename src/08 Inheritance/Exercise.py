'''
Create a base class that represents a bank account.  Add methods to allow a customer to deposit() and withdraw() 
money and provide a method display_balance().

Then add two derived classes: SavingsAccount and CheckingAccount
In the SavingsAccount provide a method 
    apply_interest()

In the CheckingAccount provide
    order_statement()

Then test you code with the following code:
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
'''
