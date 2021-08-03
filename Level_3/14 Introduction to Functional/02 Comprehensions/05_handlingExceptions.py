def catch(fn):  # fn captures n in the call
    try:
        return fn()  # fn = the lambda which takes no parameters
    except Exception as e:
        return e

# create a list containing zero
numbers = [float(n) for n in range(-5, 5)]
print(numbers)

# comprehension will raise an exception for a zero entry
reciprocals = [catch(lambda : 1/n) for n in numbers]
print(reciprocals)
