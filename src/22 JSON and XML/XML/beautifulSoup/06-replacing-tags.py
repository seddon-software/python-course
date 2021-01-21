from ReadFile import readFile
from bs4 import BeautifulSoup, Tag


doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc, features='html5lib')

# replace all authors with new tags of the form:
#    <newTag id="5" class="myclass">
#       text #5
#    </newTag>
tags = soup.findAll("author")
i = 0
for oldTag in tags:
    i = i + 1
    newTag = soup.new_tag('newTag')
    newTag['id'] = i
    newTag['class'] = 'myclass'
    newTag.insert(0, "text #{}".format(i))
    oldTag.replaceWith(newTag)

print(soup.prettify())

# mylist = soup2.find_all('li')
# mylist[i]['class'] = 'active'
1
    


