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
    listOfBooks = []
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.listOfBooks.append(self)
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def getAllTitles():
        print("\nTitles")
        print("======")
        for book in Book.listOfBooks:
            print(book.title)
    
    def findAuthor(title):
        heading = f"Finding author of {title}"
        underline = "="*len(heading)
        print(f"\n{heading}")
        print(underline)

        for book in Book.listOfBooks:
            if book.title == title:
                print(book)
                return
        print("Book not found")

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
