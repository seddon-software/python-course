############################################################
#
#    find.py
#
############################################################

from xml.etree.ElementTree import *
from xml.etree.ElementTree import _namespace_map

filename = "xml/book.xml"
tree = parse(filename)
root = tree.getroot()

author = tree.find("{http://www.demo.com/book}author");
print("first=", author.get("first"))
print("last=", author.get("last"))




