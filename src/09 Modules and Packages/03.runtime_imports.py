'''
Normally you know the name of the module you are importing, but sometimes you determine the name at run-time.  A
good example is when you are writing a multi-lingual application and want to load a module for the correct
language.  You won't know which language the user of your application uses until you ask at run-time.

Here we load the module at runtime by specifying a variable (string) that would in practice be determined at 
runtime.
'''

import sys
sys.path.append("modules")

# simulate asking for package name at run-time
nameOfPackage = "mylib"
m = __import__(nameOfPackage)

m.f1()
m.f2()
m.f3()
m.f4()
