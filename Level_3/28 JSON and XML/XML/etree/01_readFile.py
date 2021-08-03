############################################################
#
#    readFile.py
#
############################################################

from xml.etree.ElementTree import dump, parse

filename = "xml/book.xml"
tree = parse(filename)
root = tree.getroot()
print(root)
dump(tree)


