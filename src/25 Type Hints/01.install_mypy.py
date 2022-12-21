'''
Static Type Checking
====================

Starting from version 3.5, support of optional static typing was added to Python. PEP 484 -- Type Hints was 
approved and implemented. This PEP adds support of optional declaration of types for method and function 
arguments and their return values. Later, PEP 526 -- Syntax for Variable Annotations was implemented in Python 3.6,
PEP 526 added the possibility to specify a variable type. 

Type annotations for variables and methods can be used by static code analyzers and IDEs. They do not impact 
runtime performance (annotations are ignored at runtime).  For now (2022) mypy is the most popular static type 
checker for Python. Static typing can be useful not only for big projects, but also for smaller scripts.

Install Mypy
============
Mypy is a static type checker for Python and will use type hints to validate programs.  Mypy is already available 
at DLS provided you are using python 3.8 or later.  On other systems you can install with:
            python -m pip install mypy --user
'''

pass
