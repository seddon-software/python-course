cards = [[ 5, 'H'],
         ['K', 'S'],
         ['A', 'H'],
         [ 3, 'D'],
         [ 3, 'H'],
         [ 8, 'C'],
         ['J', 'D'],
         [ 2, 'H'],
         [ 2, 'C'],
         [ 9, 'S']]

def keyFunction(card):
    suits = {'S':4, 'H':3, 'D':2, 'C':1}
    pips = {'A':1, 'J':11, 'Q':12, 'K':13}
    pip = card[0]
    suit = card[1]
    if pip in pips: pip = pips[pip]
    rank = suits[suit]*13 + pip
    return rank

sortedData = sorted(cards, key=keyFunction)
for d in sortedData: 
    print(f"{d[0]} {d[1]}")
print()
