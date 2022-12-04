'''
Comprehensions
==============

lambdas are often used in comprehensions.  Although lambdas use lazy evaluation, inside the list comprehension
we use:
            (lambda x: x**2)(x)

to evaluate the lambda immediately.
'''

sequence = list(range(1, 10))
result = [(lambda x: x**2)(x) for x in sequence if x > 5]
print(result)
