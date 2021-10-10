############################################################
# 
# Subclassing built in types - e.g. dict
# 
############################################################

# define a dictionary type that won't allow duplicate values

class DistinctError(Exception):
    pass

class DictionaryWithUniqueValues(dict):
    def __setitem__(self, key, value):
        try:
            values = list(self.values())  # get existing values
            value_index = values.index(value) # this should fail if value doesn't exist
            existing_key = list(self.keys())[value_index]
            if existing_key != key:
                message = "This value already exists for '{0}'".format(self[existing_key])
                raise DistinctError(message)
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
    d['other_key'] = 'value4'   # this will cause problems
except Exception as e:
    print(e)

