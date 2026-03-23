'''
Add methods to the Book class below such that the remaining code executes successfully.
Note some of attributes should be static (class attributes).

The expected output from your program is:
            Titles
            ======
            The Silent Echo
            Whispers in the Wind
            Beneath the Stars
            The Last Ember
            Through the Mist
            Eclipsed Horizons
            The Unbroken Path
            Echoes of Tomorrow
            The Timekeeper's Secret
            Shattered Dreams

            Finding author of Eclipsed Horizons
            ===================================
            Eclipsed Horizons by Richard Hayes

            Finding author of Maybe Good, Maybe Bad
            =======================================
            Book not found
'''

class Book:
    pass

book1 = Book("The Silent Echo", "Emily Thompson")
book2 = Book("Whispers in the Wind", "Jared Walker")
book3 = Book("Beneath the Stars", "Samantha Lee")
book4 = Book("The Last Ember", "David Carter")
book5 = Book("Through the Mist", "Hannah Scott")
book6 = Book("Eclipsed Horizons", "Richard Hayes")
book7 = Book("The Unbroken Path", "Rachel Adams")
book8 = Book("Echoes of Tomorrow", "Lucas Greene")
book9 = Book("The Timekeeper's Secret", "Olivia Bell")
book10 = Book("Shattered Dreams", "Michael Rivers")

Book.getAllTitles()
Book.findAuthor("Eclipsed Horizons")
Book.findAuthor("Maybe Good, Maybe Bad")
