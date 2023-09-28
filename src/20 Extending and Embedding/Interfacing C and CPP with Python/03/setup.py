from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

mymodule = "hello_goodbye_cpp"

ext_modules = [
    Pybind11Extension(
        f"{mymodule}",
        sorted(glob("*.cpp")),  # Sort source files for reproducibility
    ),
]
try:
    from pybind11.setup_helpers import Pybind11Extension
except ImportError:
    from setuptools import Extension as Pybind11Extension

setup (
       name = f'{mymodule}',
       version = '1.0',
       author = "CRS Enterprises Ltd",
       author_email='seddon_software@btinternet.com',
       maintainer = "CRS Enterprises Ltd",
       maintainer_email ='seddon_software@btinternet.com',
       url='http://btinternet.com/~seddon-software',
       description = "pybind11 example",
       long_description = """This is a simple example,
           using pybind11 to wrap up a C++ extension module""",
       download_url = "local",
       classifiers = ["Developers", "Python Programming Course"],
       license = "none",
       ext_modules=ext_modules,
       package_data={f'{mymodule}_wrapper': glob(f'{mymodule}*.so'),
                     'lib': [f'lib{mymodule}.so']},
)
