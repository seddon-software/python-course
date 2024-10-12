'''
build
=====
Python packaging is in a state of change.  Formely, packages were built and installed using distutils, but
distutils is now deprecated and will be removed in future versions of Python.

Instead, Python packaging is being driven by PEP 517 which recommends using a build system that utilises
a pyproject.toml file to specify how to build the module and a backend system such as pip to install 
the package.

Unfortunately, details are still a little sketchy, so in the interim I'm building C/C++ extension modules with
the PEP 517 build tool:
            python -m build ...

and installing wheel files with 
            python -m pip install ...

The build system will run code in
            ../src/setup.py

and use attributes from
            ../src/setup.cfg

This interim solution is not deprecated and should work for the forseeable future.
Note: You must install build for these scripts to work:
    python -m pip install build --user
'''

import subprocess

subprocess.call("python -m build ../src".split())
