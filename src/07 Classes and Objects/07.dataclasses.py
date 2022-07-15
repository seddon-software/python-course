from dataclasses import dataclass

@dataclass
class DataClassCard:
    # note annotations are reqired
    rank: str
    suit: str

# class attributes
for item in DataClassCard.__dict__:
    print(item)

# object attributes
for item in DataClassCard("4", "spades").__dict__:
    print(item)

# info
print(DataClassCard.__dict__['__dataclass_params__'])
print(DataClassCard.__dataclass_params__)

print(DataClassCard.__dict__['__dataclass_fields__'])
print(DataClassCard.__dataclass_fields__)
