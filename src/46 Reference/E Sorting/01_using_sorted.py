'''
Using Sorted
============

The sorted built-in function allows you to sort different Python collections.  In this example we sort a set of
cards, each defined as a list of two values, e.g. 
            [ 5, 'H']

Sorted can take up to 3 parameters:
            sorted(iterable, key=key, reverse=reverse)

where the iterable is often a list (as in this example) and the key determines how to sort.  The key can be a 
function object; this function object returns the value to be sorted.  In our case the keyFunction takes in a
card and calculates a rank of the card, with the 2 of clubs being the lowest ranked card (rank = 1) and Ace of
spades being the highest (rank = 52).  The ranking value is then used by sorted.
'''

cards = [[ 5, 'Hearts'],
         ['King', 'Spades'],
         ['Ace', 'Hearts'],
         [ 3, 'Diamonds'],
         [ 3, 'Hearts'],
         [ 8, 'Clubs'],
         ['Jack', 'Diamonds'],
         [ 2, 'Hearts'],
         [ 2, 'Clubs'],
         [ 9, 'Spades']]

def keyFunction(card):
    suits = {'Spades':3, 'Hearts':2, 'Diamonds':1, 'Clubs':0}
    pips = {'Jack':11, 'Queen':12, 'King':13, 'Ace':14} # convert honour card to a pip value (Ace is high)
    pip = card[0]
    suit = card[1]
    if pip in pips: pip = pips[pip]
    rank = suits[suit]*13 + pip - 1
    return rank

sortedData = sorted(cards, key=keyFunction)
for d in sortedData: 
    print(f"{d[0]} of {d[1]}")
print()
