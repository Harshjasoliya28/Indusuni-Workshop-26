class Bank:
    
    def __init__(self,amount):
        self.amount = amount
    def getBalance(self):
        print("Balance is :",self.amount)
    def getdiposite(self,amount):
        self.amount = self.amount + amount
    def withdraw(self,amount):
        self.amount -= amount
    
myobj = Bank(1000)
myobj.getBalance()
myobj.getdiposite(50000)
myobj.getBalance()
myobj.withdraw(5000)
myobj.getBalance()