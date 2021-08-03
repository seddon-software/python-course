"""
Word prefixes are also called stems. Write a program that reads the file 
/usr/share/dict/words and finds the most popular stems of size 2 to 29 
(if you get a tie, just pick one).    
"""


def DetermineStems():
    '''
       build a dictionary of (stem, count) pairs
    '''
    for word in lines:
        word = word.rstrip()
        for i in range(2, len(word)+1):
            stem = word[:i]
            if stem in stems:
                stems[stem] += 1
            else:
                stems[stem] = 1

def openTestData():
    '''
       build an list containing the test data
    '''
    inFile = None
    lines = list()
    
    try:
        inFile = open("words.txt", "r")
    
        for line in inFile:
            lines.append(line)
    except IOError as reason:
        print(reason)
    finally:        
        if inFile: inFile.close()
    
    return lines

def ProcessStems():
    '''
       build a list containing (stem, count) tuples
       - element 2 contains the most popular 2 stem 
       - element 3 contains the most popular 3 stem 
       - element 4 contains the most popular 4 stem ...
    ''' 
    for i in range(120): #assume word never exceed 19 characters
        popularStems.append(("", 0))
        
    for key, value in stems.items():
        #print key, value
        index = len(key)
        if popularStems[index][1] < value:
            popularStems[index] = (key, value)
    return popularStems
    
def PrintResults():
    '''
       popularStems contains a set of tuples
    '''
    for i in range(2,30):
        stem = popularStems[i][0] 
        count = popularStems[i][1]
        if stem != None:
            print(f"Most popular stem of size {i} {stem} (occurs {count} times)") 
     
stems = dict()
popularStems = list()
lines = openTestData()
DetermineStems()
ProcessStems()
PrintResults()

1
