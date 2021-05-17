class Accumulate:
    def __init__(self):
        self.total = 0
        
    def __call__(self, n):
        self.total += n
        
    def __str__(self):
        return str(self.total)
    
runningTotal = Accumulate() 
runningTotal(15)
runningTotal(30)
runningTotal(45)
runningTotal(60)
runningTotal(75)
print(runningTotal)

