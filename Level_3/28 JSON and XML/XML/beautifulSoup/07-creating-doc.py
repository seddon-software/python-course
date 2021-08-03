from bs4 import BeautifulSoup, NavigableString


soup =  BeautifulSoup(features='html5lib')

# create tags
tag1 = soup.new_tag("person")
tag2 = soup.new_tag("name")
tag3 = soup.new_tag("location")

# add attributes
tag2['first'] = 'John'
tag2['last'] = 'Smith'
tag3['country'] = 'uk'

# add text
text = NavigableString("John Gary Smith")

# build soup
soup.insert(0, tag1)
tag1.insert(0, tag2)
tag1.insert(1, tag3)
tag2.insert(0, text)

print(soup)
print("----------------")
print(soup.prettify())


1
    


