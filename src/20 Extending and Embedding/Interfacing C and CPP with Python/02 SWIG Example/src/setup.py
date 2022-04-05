import sys
from setuptools import setup, Extension


example_module = Extension('_myhello',
            sources=['hello.c', 'hello.i'],
            include_dirs=[],
            extra_compile_args=[])
#            language="c")
setup (
       name = 'SWIG C Example',
       version = '1.0',
       author = "CRS Enterprises Ltd",
       author_email='seddon-software@keme.co.uk',
       maintainer = "CRS Enterprises Ltd",
       maintainer_email ='seddon-software@keme.co.uk',
       url='http://www.keme.co.uk/~seddon-software',
       description = "SWIG example",
       long_description = """This is a simple example,
           using SWIG to wrap up a C module""",
       download_url = "local",
       classifiers = ["Developers", "Python Programming Course"],
       platforms = sys.platform,
       license = "none",
       ext_modules = [example_module],
       py_modules = ["_myhello", "myhello"],
#       data_files=["myhello.py"]
       )
