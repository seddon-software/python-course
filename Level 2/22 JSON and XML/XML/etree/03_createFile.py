############################################################
#
#    createFile.py
#
############################################################

from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import _namespace_map

"""
Code to generate the following document:

<book:book xmlns:book="http://www.demo.com/book">
    <book:title>XMLBeans</book:title>
    <book:author first="John" last="Smith" />
    <book:publisher>Wiley</book:publisher>
    <book:pubdate>2007-06+01:00</book:pubdate>
    <book:cost>23.79</book:cost>
</book:book>
"""

# setup namespace and alias
ns = "http://www.demo.com/book"
uri = "{" + ns + "}"
_namespace_map[ns] = 'book'
            
# define elements
root = Element(uri + "book")
title = Element(uri + "title")
author = Element(uri + "author")
publisher = Element(uri + "publisher")
pubdate = Element(uri + "pubdate")
cost = Element(uri + "cost")

# add attributes
author.attrib["first"] = "John"
author.attrib["last"] = "Smith"

# add text
title.text = "XMLBeans"
publisher.text = "Wiley"
pubdate.text = "2007-06+01:00"
cost.text = "23.79"

# build tree
root.append(title)
root.append(author)
root.append(publisher)
root.append(pubdate)
root.append(cost)

# write to file
tree =  ElementTree(root)
tree.write("xml/new_book.xml")


