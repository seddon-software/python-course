'''
In the final example in this chapter we take a look at subclassing built in types (e.g. dict).
Here we define a dictionary type that doesn't allow duplicate values by overloading the "__setitem__" method.
'''

class DistinctError(Exception):     # define our own exception class
    pass

class DictionaryWithUniqueValues(dict):     # our class derives from dict
    def __setitem__(self, key, value):
        try:
            values = list(self.values())  # get existing values
            value_index = values.index(value) # this should fail if value doesn't exist
            existing_key = list(self.keys())[value_index]
            if existing_key != key:
                message = f"This value already exists for '{existing_key}'"
                raise DistinctError(message)    # this exception is not caught in this method
        except ValueError:
            pass    # eat exception because value is new
        # update dict in super class with new value
        super(DictionaryWithUniqueValues, self).__setitem__(key, value)

d = DictionaryWithUniqueValues()
d['key1'] = 'value1'
d['key2'] = 'value2'
d['key3'] = 'value3'
d['key4'] = 'value4'
d['key5'] = 'value5'
try:
    d['other_key'] = 'value4'   # this will cause problems and raise a DistinctError object
except DistinctError as e:
    print(e)

