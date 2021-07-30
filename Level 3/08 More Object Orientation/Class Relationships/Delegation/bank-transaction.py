############################################################
#
#    Delegation
#
############################################################

class Bank:
    def GetApproval(self, accountName):
        if accountName == "john":
            return True
        else:
            return False
        
class Transaction:
    def __init__(self, bank, accountName):
        self.bank = bank
        self.accountName = accountName
         
    def Withdraw(self, amount):
        ok = self.bank.GetApproval(self.accountName)
        if ok:
            return amount
        else:
            return 0
    
        

bank = Bank()

transaction1 = Transaction(bank, "john")
transaction2 = Transaction(bank, "sue")

request = 500
johnReceived = transaction1.Withdraw(request)
sueReceived = transaction2.Withdraw(request)


1 

