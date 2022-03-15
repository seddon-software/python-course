'''
Closures
========

Python allows nested functions as the example below.  Note that when calling the nested function "g" we don't
pass the x and y lists to "g" as parameters even though we modify x and y in "g".  This is because of closures.

The function "g" sees variables defined in its environment (or closure).  The environment "encloses" the 
surrounding scope of "g".  Python allows us to explicity see the closure with
            <function>.__closure__

In this example, the closure has 2 items (x and y).  Note that only mutable items referenced in "g" will be
included in this closure (so a is not part of the closure).
'''

def f():
    a = [100]
    x = [200]
    y = [300]
    def g():
        x.append(201)
        y.append(301)
    g()
    for c in g.__closure__:
        print(f"closure for g: {c.cell_contents}")

f()