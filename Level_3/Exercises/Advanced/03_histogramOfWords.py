import matplotlib.pyplot as plt

def displayPlot():
    plt.title('Frequency of word lengths in /usr/share/dict/words')
    plt.xlabel('word length', fontsize=16)
    plt.ylabel('frequency', fontsize=16)
    plt.show()

def generateStepPlot(occurances):
    keys = sorted(occurances.keys())
    values = [occurances[key] for key in keys]
    keys = [key+0.5 for key in keys] # adjust x axis legend by 0.5
    plt.step(keys, values, color='red')
    old_key = keys[0]
    for key, value in zip(keys, values):
        plt.fill_between([old_key, key], [value, value], [0, 0])
        old_key = key

def calculateOccurancesOfWords(words):
    occurances = {}
    for word in words:
        length = len(word)
        if length in occurances:
            occurances[length] += 1
        else:
            occurances[length] = 1
    return occurances

def readInputFile(fileName):
    try:
        with open(fileName, "r") as f:
            allLines = f.readlines()
            return allLines
    except IOError as e:
        print(e)


words = readInputFile("/usr/share/dict/words")
occurances = calculateOccurancesOfWords(words)
generateStepPlot(occurances)
displayPlot()

