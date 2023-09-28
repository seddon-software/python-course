from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

ext_modules = [
    Pybind11Extension(
        "hello_goodbye",
        sorted(glob("*.cpp")),  # Sort source files for reproducibility
    ),
]
setup (
       name = 'hello_goodbye',
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
       license = "none",
       ext_modules=ext_modules,
       package_data={'hello_goodbye_wrapper': ['hello_goodbye.cpython-39-x86_64-linux-gnu.so'],
                     'lib': ['libhello_goodbye.so']},
)
