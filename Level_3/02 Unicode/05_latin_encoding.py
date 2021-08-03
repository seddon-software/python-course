#!/usr/bin/env python
# -*- coding: latin-1 -*-

# the second line of this script defines the default unicode encoding (normally UTF-8)

# find code point for last character in string
u = 'abcdé'
print(u)
print(ord(u[-1]))

# convert to bytes (see http://www.ic.unicamp.br/~stolfi/EXPORT/www/ISO-8859-1-Encoding.html)
b = u.encode('latin1')
print(b)


