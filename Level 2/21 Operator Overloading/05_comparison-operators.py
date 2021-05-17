
def findBiggestCard(myHand):
    keyCard = myHand[0]
    for card in myHand:
        if card > keyCard:
            keyCard = card
    print(keyCard)
    
def findSmallestCard(myHand):
    keyCard = myHand[0]
    for card in myHand:
        if card < keyCard:
            keyCard = card
    print(keyCard)

class Card:
    cardinality = {
        "A":12, "K":11, "Q":10, "J":9, "10":8, "9": 7, 
        "8":6,  "7":5,  "6":4,  "5":3,  "4":2, "3": 1,
        "2":0,  "C":0,  "D":13, "H":26, "S":39 
    }

    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit

    def value(self):
        return Card.cardinality[self.suit] + Card.cardinality[self.pip]  
        
    def __gt__(self, rhs):
        return self.value() > rhs.value()
        
    def __lt__(self, rhs):
        return self.value() < rhs.value()
        
    def __str__(self):
        return str(self.pip) + str(self.suit)

# create cards
five_of_clubs    = Card("5", "C")
king_of_diamonds = Card("K", "D")
queen_of_spades  = Card("Q", "S")
three_of_hearts  = Card("3", "H")
six_of_diamonds  = Card("6", "D")

# examine standard attributes
myHand = [five_of_clubs, king_of_diamonds, queen_of_spades, three_of_hearts, six_of_diamonds]

findBiggestCard(myHand)
findSmallestCard(myHand)
 
1