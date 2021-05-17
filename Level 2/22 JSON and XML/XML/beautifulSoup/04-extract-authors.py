from ReadFile import readFile
from bs4 import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc, features='html5lib')

# extract fragments
tags = soup.findAll("author")
newSoup = BeautifulSoup(str(tags), features='html5lib')
print(newSoup.prettify())

1
    


