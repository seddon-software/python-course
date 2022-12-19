'''
    YAML documents start with --- and end with ...
    YAML files can contain multiple documents.  They contains blocks with individual items stored as a key-value 
    pairs, like Python dictionaries.  A key is usually a string, the value can be any type.  Indentation is used 
    to indicate the nesting of items.  Use a hyphen to define a subitem.
'''

import yaml
from yaml.loader import SafeLoader

# SafeLoader: Loads subset of the YAML safely, mainly used if the input is from an untrusted source.
with open('data/single_doc.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
