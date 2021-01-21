############################################################ 
#
# various ways of sorting using the sorted function
#
############################################################ 

def basicSorting():
    weekdays = [ "monday", "Tuesday", "wednesday", "Thursday", "friday", "Saturday", "sunday"]
    print(sorted(weekdays))

def sortingWithAKey():
    weekdays = [ "monday", "Tuesday", "wednesday", "Thursday", "friday", "Saturday", "sunday"]
    print(sorted(weekdays, key=str.lower))

def sortingDictionaryUsingAKeyAndFunction():
    salary = {
              "tim": 27000,
              "zak": 34000, 
              "jon": 52000,
              "sue": 12500,
              "zoe": 46000
             }
    def getSalary(key): 
        return salary[key]
    
    for key in sorted(salary, key=getSalary):
        print(key, salary[key], end=' ')
    print()

def sortingDictionaryUsingAKeyAndLambda():
    salary = {
              "tim": 27000,
              "zak": 34000, 
              "jon": 52000,
              "sue": 12500,
              "zoe": 46000
             }
    for key in sorted(salary, key=lambda key:salary[key]):
        print(key, salary[key], end=' ')
    print()
    
def usingACompareFunction():
    def rank(card):
        pip = card[0]
        suit = card[1]
        suits = "CDHS"
        return suits.find(suit) * 13 + pip
    print(sorted([(8,'H'), (5,'H'), (2,'S'), (4,'D'), (7,'D'), (7,'C'), (3,'H')], key=rank))

####################################################################

basicSorting()
sortingWithAKey()
sortingDictionaryUsingAKeyAndFunction()
sortingDictionaryUsingAKeyAndLambda()
usingACompareFunction()
