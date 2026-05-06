''' 
The sorted() function in Python returns a new sorted list from the elements of any iterable, 
using a key function.  The key function is often defined as a lambda as in:
            sortedHand = sorted(hand, key=lambda card: rank(card))
'''

def rank(card):
    "suits '♣'->rank 1-13, '♦'->14-26, '♥'->27-39, '♠'->40-52"
    pip, suit =card[:-1], card[-1]
    match pip:
        case 'J': rank = 10
        case 'Q': rank = 11
        case 'K': rank = 12
        case 'A': rank = 13
        case _: rank = int(pip) - 1
    match suit:
        case '♣': rank += 0
        case '♦': rank += 13
        case '♥': rank += 26
        case '♠': rank += 39
    return rank

hand = ['A♠','10♥','3♣','K♦','7♠','J♣','2♥','Q♠','5♦','9♣','4♠','8♥','6♦']

sortedHand = sorted(hand, key=lambda card: rank(card))
print(hand)
print(sortedHand)
