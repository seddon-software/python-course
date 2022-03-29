'''
assert
======
Assert statements can be used to define function preconditions.  In this example, the "CalculateQuartile()" 
function expects its parameter "percent" to be an instance of "int" and to lie between 0 and 100.  The
assert statement is an excellent way of enforcing these preconditions.

If the conditions are not met, as in:
            CalculateQuartile(104)

then an exception is raised.  Although you can write an exception handler to catch the exception this is not
normal practice because "assert" is meant to catch problems during development and not in production code.
'''

def CalculateQuartile(percent):
    # define and document function preconditions
    assert isinstance(percent, int)
    assert percent >= 0 and percent <= 100

    quartile = 1
    if percent > 25:
        quartile = 2
    if percent > 50:
        quartile = 3
    if percent > 75:
        quartile = 4
    print(f"{percent} is in quartile {quartile}")

CalculateQuartile(17)
CalculateQuartile(34)
CalculateQuartile(56)
CalculateQuartile(87)
CalculateQuartile(104)
