from distutils.core import setup

setup(name = "mymodule",
    version = "1.0",
    description = "very simple example of a python module",
    author = "CRS Enterprises Ltd",
    author_email = "email@abc.com",
    url = "http://localhost:8000/repo",
    packages = ['mypackage', 'mypackage/mysubpackage'],
    scripts = [],
    long_description = """Really long text here.""" 
)
