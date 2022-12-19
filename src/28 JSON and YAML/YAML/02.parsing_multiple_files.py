'''
This example shows how to work with YAML files that contain multiple documents
'''

import yaml
from yaml.loader import SafeLoader


# return a generator
with open('data/multiple_doc.yaml') as f:
    g = yaml.load_all(f, Loader=SafeLoader)
    print(type(g))
    for n, d in enumerate(g):
        print(f"document #{n} is: {d}")

# convert to a list
with open('data/multiple_doc.yaml') as f:
    g = yaml.load_all(f, Loader=SafeLoader)
    for n, d in enumerate(list(g)):
        print(f"document #{n} is: {d}")


