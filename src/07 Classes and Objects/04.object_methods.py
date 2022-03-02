'''
Methods of Object Class
=======================

Every Python class is derived from the object class.  This means every class has access to the methods in the
object class.  Here we list every such method together with their doc string.

This example produces a lot of output and is best run on the command line.
'''


for method in dir(object):
    def heading(s):
        print(f"{s}")
        print("="*len(s))
    heading(method)
    print(f'''{eval(f'{f"""object.{method}.__doc__"""}')}\n\n''')
