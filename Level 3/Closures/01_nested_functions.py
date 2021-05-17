def getStats(myList):
    def getSum():       # no need to pass myList as a parameter
        total = 0
        for i in myList:
            total += i
        return total
    def getLength():
        return len(myList)
    
    print(f"sum of list = {getSum()}")
    print(f"length of list = {getLength()}")

getStats(list(range(10)));