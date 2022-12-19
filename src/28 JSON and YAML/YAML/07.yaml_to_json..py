import json
import yaml
from yaml.loader import SafeLoader

JSON_FILE = 'data/single_doc.json'
YAML_FILE = 'data/single_doc.yaml'
with open(YAML_FILE) as f:
    try:
        data = yaml.load(f, Loader=SafeLoader)
        print(data)
        # Write YAML object to JSON format
        with open(JSON_FILE, 'w') as f:
            json.dump(data, f, sort_keys=False)    
    except yaml.YAMLError as e:
        print(f"*****{e}")

import os
os.system(f"cat {JSON_FILE}")