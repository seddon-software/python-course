import sys
from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext, Extension

name = 'MyCython_Package'
version = '2.0'

extensions = [
    Extension("*", 
              ["*.pyx"], 
              extra_compile_args=["-w"],
              )
]

setup(
    name = name,
    version = version,
    author = "CRS Enterprises Ltd",
    author_email='seddon-software@keme.co.uk',
    maintainer = "CRS Enterprises Ltd",
    maintainer_email ='seddon-software@keme.co.uk',
    url='http://www.keme.co.uk/~seddon-software',
    description = "Cython example",
    long_description = """This is a simple example,
        using Cython""",
    download_url = "local",
    classifiers = ["Developers", "Python Programming Course"],
    platforms = sys.platform,
    license = "none",
    ext_modules = cythonize(extensions)
)

