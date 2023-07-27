'''
Ordered Dictionaries
====================
Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering 
operations. They have become less important now that the built-in dict class gained the ability to remember 
insertion order (this new behavior became guaranteed in Python 3.7).


The ordered_dict is a subclass of dict that has methods specialized for rearranging dictionary order.
'''

import collections
od = collections.OrderedDict({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6})
print(od)
od.move_to_end('one')
print(od)
od.move_to_end('two', last=False)
print(od)
