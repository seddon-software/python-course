'''
Dictionary Comprehension
========================

The full set of comprehensions is:
    list comprehension
    dict comprehension
    set comprehension
    generator comprehension

with the following syntax
    list        [ fn(item) for item in sequence ]
    dict        { key:value for item in sequence }
    set         { fn(item) for item in sequence }
    generator   ( fn(item) for item in sequence )

Here we investigate creating a dict comprehension.    
'''

cubes = {f"cube_of_{x}": x**3 for x in range(10)}
print(cubes)

