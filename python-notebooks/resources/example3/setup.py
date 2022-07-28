import sys
import platform
from distutils.core import setup, Extension

if(platform.system() == 'Darwin'):
    extra_compile_args=["-stdlib=libc++"]
    extra_link_args=["-lc++", "-mmacosx-version-min=10.9"]
else:
    extra_compile_args=[]
    extra_link_args=[]

# normal setup code
example_module = Extension('_myexample',
                           language='c++',
                           swig_opts=['-c++'],
                           sources=['myexample.i'],
                           extra_compile_args=extra_compile_args,
                           extra_link_args=extra_link_args
                           )

setup (
       name = 'CPP SWIG example',
       version = '1.0',
       author = "CRS Enterprises Ltd",
       author_email='seddon-software@keme.co.uk',
       maintainer = "CRS Enterprises Ltd",
       maintainer_email ='seddon-software@keme.co.uk',
       url='http://www.keme.co.uk/~seddon-software',
       description = "CPP SWIG example",
       long_description = """This is a SWIG example that defines
            two C++ functions and uses the STL""",
       download_url = "local",
       classifiers = ["Developers", "Python Programming Course"],
       platforms = sys.platform,
       license = "none",
       ext_modules = [example_module],
       py_modules = ["myexample"],
       )
