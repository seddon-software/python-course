from setuptools import setup
from Cython.Build import cythonize

setup(
    name='cythonRoots',
    ext_modules=cythonize("cythonRoots.pyx"),
)
