import yaml
from yaml.loader import UnsafeLoader

with open('data/errors_in_file.yaml', "r") as f:
    try:
        data = f.read()
        config = yaml.safe_load(data)
    except yaml.YAMLError as e:
        print(f"*****{e}")
