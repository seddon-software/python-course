'''
Normally you know the name of the module you are importing, but sometimes you determine the name at run-time.  A
good example is when you are writin a multi-lingual application and want to load a module for the correct
language.  You won't know which language the user of your application uses until you ask at run-time.

Here we load the module at runtime by specifying a variable (string).
'''

import sys
sys.path.append("mylib")

# simulate asking for package name at run-time
nameOfPackage = "mypackage"
mp = __import__(nameOfPackage)

mp.f1()
mp.f2()
mp.f3()
mp.f4()
