import sys
from skbuild import setup  # This line replaces 'from setuptools import setup'
 
mymodule = Extension('Lib02', sources = ['Lib02.so'])

setup (name = 'Lib02Package',
        version = '1.0',
        # author = "CRS Enterprises Ltd",
        # author_email='seddon-software@keme.co.uk',
        # maintainer = "CRS Enterprises Ltd",
        # maintainer_email ='seddon-software@keme.co.uk',
        # url='http://www.keme.co.uk/~seddon-software',
        # description = "simple example",
        # long_description = """This is a simple example,
        #     to wrap up a C module""",
        # download_url = "local",
        # classifiers = ["Developers", "Python Programming Course"],
        # platforms = sys.platform,
        # license = "none",
        ext_modules = [mymodule]
        )
