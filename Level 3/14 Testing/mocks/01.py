from unittest.mock import MagicMock

class MyDiary:
    def setDay(day): pass
    def messageOfTheDay(self): pass
    def nextDay(): pass

diary = MagicMock()
diary.setDay(4)
diary.nextDay.return_value = 5

print(diary.nextDay())
