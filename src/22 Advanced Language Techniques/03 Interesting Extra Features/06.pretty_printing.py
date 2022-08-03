'''
Pretty Printing
===============
The pprint module “pretty prints” arbitrary Python data structures in a form which can be used as input to the 
interpreter and is easy to read.
'''

import pprint as pp

string = "supercalafragilisticexpialidocious"
dictionary = {char:string.count(char) for char in string}
print(dictionary)
pp.pprint(dictionary)


