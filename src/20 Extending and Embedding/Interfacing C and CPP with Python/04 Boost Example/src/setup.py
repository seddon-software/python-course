import sys
from setuptools import setup, Extension


mymodule = Extension('boost_example',
        include_dirs = ['/usr/include/boost'],
        libraries = ['boost_python3'],
#        library_dirs = ['/Users/seddon/work/boost_1_57_0/stage/lib'],
        sources = ['greeting.cpp'])

setup (name = 'GreetingPackage',
        version = '1.0',
        author = "CRS Enterprises Ltd",
        author_email='seddon-software@keme.co.uk',
        maintainer = "CRS Enterprises Ltd",
        maintainer_email ='seddon-software@keme.co.uk',
        url='http://www.keme.co.uk/~seddon-software',
        description = "simple example",
        long_description = """This is a simple example,
            to wrap up a C module""",
        download_url = "local",
        classifiers = ["Developers", "Python Programming Course"],
        platforms = sys.platform,
        license = "none",
        ext_modules = [mymodule])

